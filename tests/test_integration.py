"""Tests de integración del pipeline completo (con Ollama simulado)."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


class FakeOllama:
    """Simula Ollama devolviendo respuestas deterministas."""

    def __init__(self):
        self.calls = []

    def generate(self, prompt, system=None, format_json=False):
        self.calls.append(prompt)
        if "Traduce el siguiente contenido" in prompt:
            return "Traducción simulada del contenido técnico."
        if "Resume el siguiente contenido" in prompt:
            return "- Punto uno simulado.\n- Punto dos simulado."
        return "respuesta genérica"

    def generate_json(self, prompt, system=None):
        self.calls.append(prompt)
        if "Clasifica el siguiente contenido" in prompt:
            return {
                "company": "Ejemplo", "product": "HerramientaX",
                "category": "Developer Tools", "subcategory": "cli",
                "pricing": "open-source", "license": "MIT",
                "open_source": True, "self_hosted": True,
                "tags": ["cli", "dev"],
            }
        if "Extrae los datos técnicos" in prompt:
            return {"version": "2.0", "release_date": "2026-08-17", "price": "",
                    "urls": [], "requirements": "", "breaking_changes": ""}
        if "Analiza la importancia" in prompt:
            return {"importance": "high", "impact": "medium", "audience": "devs",
                    "reasons": ["Lanzamiento relevante"]}
        if "Identifica posibles alternativas" in prompt:
            return {"alternatives": [{"name": "AltB", "confidence": "high"}]}
        if "MINI INFORME profesional" in prompt:
            return {
                "what_is": "Herramienta CLI para agentes de IA.",
                "why_development": "Automatiza tareas de desarrollo.",
                "profiles": [
                    {"role": "Trainee", "relevance": "Media", "must_know": ["Conceptos básicos"]},
                    {"role": "Senior", "relevance": "Alta", "must_know": ["Integración", "Arquitectura"]},
                ],
            }
        return {}


def test_full_sync_pipeline(db, settings, monkeypatch, tmp_path):
    from app.collector.pipeline import collect
    from app.generator.dashboard import generate_dashboard
    from app.processor.processor import Processor
    from app.sources.models import Source
    from app.exporters.jsonl import export_jsonl

    # 1. Collect con una fuente RSS local
    source = Source(id="test", name="Test", type="rss",
                    url="https://example.com/feed.xml", category="AI")
    repo_upsert = __import__("app.database.repository", fromlist=["upsert_source"]).upsert_source
    repo_upsert(db, source.as_dict())

    rss_xml = """<?xml version="1.0"?>
<rss version="2.0"><channel>
<item><title>Nueva herramienta CLI para agentes de IA</title>
<link>https://example.com/tool</link><guid>g1</guid>
<description><![CDATA[<p>Launch of an open source CLI tool for AI agents with new capabilities.</p>]]></description>
<pubDate>Mon, 17 Aug 2026 10:00:00 GMT</pubDate></item>
</channel></rss>"""

    def fake_get(url, timeout=30, headers=None):
        class R:
            content = rss_xml.encode()

            def raise_for_status(self):
                pass

        return R()

    monkeypatch.setattr("app.collector.rss.requests.get", fake_get)

    result = collect(db, [source], settings)
    assert result.new == 1
    assert result.duplicates == 0

    # 2. Procesar con Ollama simulado
    processor = Processor(db, settings)
    processor.set_client(FakeOllama())  # sustituimos el cliente real
    pr = processor.process_pending()
    assert pr.processed == 1

    # 3. Nota generada (categoría Developer Tools según el clasificador simulado)
    notes = list((settings.vault_path / "02 - Updates" / "Developer Tools").glob("*.md"))
    assert len(notes) == 1
    text = notes[0].read_text(encoding="utf-8")
    assert "HerramientaX" in text
    assert "importance: high" in text
    assert "pricing: open-source" in text
    assert "open_source: true" in text
    assert "translated: true" in text
    assert "Informe para desarrolladores" in text
    assert "Herramienta CLI para agentes de IA" in text
    assert "Trainee" in text
    assert "insights: true" in text

    # 4. JSONL
    files = export_jsonl(db, settings)
    assert len(files["all"].read_text(encoding="utf-8").strip().splitlines()) == 1

    # 5. Dashboard
    dash = generate_dashboard(db, settings)
    assert dash.exists()
    assert "Tech Intelligence" in dash.read_text(encoding="utf-8")


def test_sync_does_not_duplicate(db, settings, monkeypatch):
    """Un segundo sync no duplica artículos."""
    from app.collector.pipeline import collect
    from app.sources.models import Source

    source = Source(id="t2", name="T2", type="rss", url="https://example.com/f.xml")
    rss_xml = """<?xml version="1.0"?><rss version="2.0"><channel>
    <item><title>Anuncio del feed</title><link>https://example.com/a</link><guid>ga</guid>
    <description>Contenido del anuncio.</description>
    <pubDate>Mon, 17 Aug 2026 10:00:00 GMT</pubDate></item></channel></rss>"""

    def fake_get(url, timeout=30, headers=None):
        class R:
            content = rss_xml.encode()

            def raise_for_status(self):
                pass

        return R()

    monkeypatch.setattr("app.collector.rss.requests.get", fake_get)
    r1 = collect(db, [source], settings)
    r2 = collect(db, [source], settings)
    assert r1.new == 1
    assert r2.new == 0
    assert r2.duplicates == 1