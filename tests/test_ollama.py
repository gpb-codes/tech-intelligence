import pytest

from app.ollama.client import OllamaClient, OllamaError, parse_json_loose
from app.ollama.modules import Classifier, Translator, load_prompt


def test_parse_json_loose():
    assert parse_json_loose('{"a": 1}') == {"a": 1}
    assert parse_json_loose('```json\n{"a": 1}\n```') == {"a": 1}
    assert parse_json_loose('Texto\n{"a": 1}\nMás texto') == {"a": 1}
    with pytest.raises(OllamaError):
        parse_json_loose("no json aquí")


def test_generate_success(monkeypatch):
    class FakeResp:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {"response": "hola"}

    def fake_post(url, **kwargs):
        assert url.endswith("/api/generate")
        assert kwargs["json"]["model"] == "llama3"
        assert kwargs["json"]["stream"] is False
        return FakeResp()

    monkeypatch.setattr("app.ollama.client.requests.post", fake_post)
    client = OllamaClient("http://x:11434", "llama3", timeout=30)
    assert client.generate("prompt") == "hola"


def test_generate_json_format(monkeypatch):
    class FakeResp:
        status_code = 200

        def raise_for_status(self):
            pass

        def json(self):
            return {"response": '{"category": "AI"}'}

    def fake_post(url, **kwargs):
        assert kwargs["json"]["format"] == "json"
        return FakeResp()

    monkeypatch.setattr("app.ollama.client.requests.post", fake_post)
    client = OllamaClient("http://x:11434", "llama3")
    assert client.generate_json("p") == {"category": "AI"}


def test_generate_timeout(monkeypatch):
    import requests

    def fake_post(url, **kwargs):
        raise requests.Timeout("slow")

    monkeypatch.setattr("app.ollama.client.requests.post", fake_post)
    client = OllamaClient("http://x:11434", "llama3", timeout=5)
    with pytest.raises(OllamaError, match="Timeout"):
        client.generate("p")


def test_is_available(monkeypatch):
    class FakeResp:
        status_code = 200

    monkeypatch.setattr("app.ollama.client.requests.get", lambda *a, **k: FakeResp())
    assert OllamaClient("http://x", "m").is_available() is True


def test_classifier_validates_invalid_values(monkeypatch):
    def fake_generate_json(prompt, system=None):
        return {"category": "Categoría Inexistente", "pricing": "gratis", "tags": ["a"]}

    client = OllamaClient("http://x", "m")
    monkeypatch.setattr(client, "generate_json", fake_generate_json)
    c = Classifier(client, __import__("pathlib").Path("app/ollama/prompts"))
    out = c.classify("contenido")
    assert out["category"] == "General Tech"
    assert out["pricing"] == "unknown"


def test_prompts_exist():
    from pathlib import Path

    prompts_dir = Path("app/ollama/prompts")
    for name in ("translate", "summarize", "classify", "extract", "importance", "alternative", "insights"):
        assert (prompts_dir / f"{name}.txt").exists()
        text = load_prompt(prompts_dir, name)
        assert "{{CONTENT}}" in text


def test_insights_generator(monkeypatch):
    from pathlib import Path

    from app.ollama.modules import InsightsGenerator

    def fake_generate_json(prompt, system=None):
        return {
            "what_is": "Lenguaje de programación.",
            "why_development": "Automatiza infraestructura.",
            "profiles": [
                {"role": "Trainee", "relevance": "Baja", "must_know": ["Conceptos"]},
                {"role": "Ingeniero en Redes", "relevance": "Alta", "must_know": ["Configuración"]},
                {"role": "Rol Inexistente", "relevance": "Muy Alta", "must_know": ["x"]},
            ],
        }

    client = OllamaClient("http://x", "m")
    monkeypatch.setattr(client, "generate_json", fake_generate_json)
    gen = InsightsGenerator(client, Path("app/ollama/prompts"))
    out = gen.generate("contenido")
    assert out["what_is"] == "Lenguaje de programación."
    roles = [p["role"] for p in out["profiles"]]
    assert roles == ["Trainee", "Ingeniero en Redes", "Rol Inexistente"]
    assert out["profiles"][1]["relevance"] == "Alta"
    assert len(out["profiles"]) <= 8


def test_translator_prompt(monkeypatch):
    from pathlib import Path

    captured = {}

    def fake_generate(prompt):
        captured["prompt"] = prompt
        return "traducido"

    client = OllamaClient("http://x", "m")
    monkeypatch.setattr(client, "generate", fake_generate)
    tr = Translator(client, Path("app/ollama/prompts"))
    assert tr.translate("Hello world") == "traducido"
    assert "Hello world" in captured["prompt"]
    assert "Traduce el siguiente contenido al español" in captured["prompt"]


def test_openrouter_client(monkeypatch):
    from app.ollama.client import OpenRouterClient

    class FakeResp:
        def raise_for_status(self):
            pass

        def json(self):
            return {"choices": [{"message": {"content": '{"ok": true}'}}]}

    captured = {}

    def fake_post(url, **kwargs):
        captured["url"] = url
        captured["headers"] = kwargs.get("headers", {})
        captured["payload"] = kwargs.get("json", {})
        return FakeResp()

    monkeypatch.setattr("app.ollama.client.requests.post", fake_post)
    client = OpenRouterClient("KEY123", "moonshotai/kimi-k2:online", timeout=30)
    out = client.generate_json("prompt")
    assert out == {"ok": True}
    assert captured["url"].endswith("/chat/completions")
    assert captured["headers"]["Authorization"] == "Bearer KEY123"
    assert captured["payload"]["model"] == "moonshotai/kimi-k2:online"

    # Sin API key -> error claro
    client2 = OpenRouterClient("", "modelo")
    with pytest.raises(OllamaError, match="OPENROUTER_API_KEY"):
        client2.generate("p")