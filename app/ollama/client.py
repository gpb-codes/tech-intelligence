"""Cliente HTTP de Ollama (API local, sin dependencias externas)."""
from __future__ import annotations

import json

import requests

from app.utils.logging import get_logger

logger = get_logger("ollama")


class OllamaError(Exception):
    pass


class OllamaClient:
    def __init__(self, base_url: str, model: str, timeout: int = 120, temperature: float = 0.1):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout
        self.temperature = temperature

    # ------------------------------------------------------------------
    # Estado
    # ------------------------------------------------------------------

    def is_available(self, timeout: int = 5) -> bool:
        try:
            resp = requests.get(f"{self.base_url}/api/tags", timeout=timeout)
            return resp.status_code == 200
        except requests.RequestException:
            return False

    def list_models(self) -> list[str]:
        try:
            resp = requests.get(f"{self.base_url}/api/tags", timeout=self.timeout)
            resp.raise_for_status()
            return [m.get("name", "") for m in resp.json().get("models", [])]
        except (requests.RequestException, json.JSONDecodeError) as e:
            raise OllamaError(f"No se pudo consultar los modelos: {e}") from e

    def model_installed(self, model: str | None = None) -> bool:
        model = model or self.model
        try:
            resp = requests.post(
                f"{self.base_url}/api/show",
                json={"name": model},
                timeout=self.timeout,
            )
            return resp.status_code == 200
        except requests.RequestException:
            return False

    # ------------------------------------------------------------------
    # Generación
    # ------------------------------------------------------------------

    def generate(self, prompt: str, system: str | None = None, format_json: bool = False) -> str:
        """Ejecuta una generación y devuelve el texto de respuesta."""
        if not self.model:
            raise OllamaError("OLLAMA_MODEL no está configurado (.env)")

        payload: dict = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": self.temperature},
        }
        if system:
            payload["system"] = system
        if format_json:
            payload["format"] = "json"

        logger.info("Ollama generate: model=%s, prompt_len=%d", self.model, len(prompt))
        try:
            resp = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=self.timeout,
            )
            resp.raise_for_status()
            data = resp.json()
        except requests.Timeout as e:
            raise OllamaError(f"Timeout de Ollama ({self.timeout}s): {e}") from e
        except requests.RequestException as e:
            raise OllamaError(f"Error de conexión con Ollama en {self.base_url}: {e}") from e
        except json.JSONDecodeError as e:
            raise OllamaError(f"Respuesta no JSON de Ollama: {e}") from e

        response = data.get("response", "")
        if not response.strip():
            raise OllamaError("Ollama devolvió una respuesta vacía")
        return response.strip()

    def generate_json(self, prompt: str, system: str | None = None) -> dict:
        """Generación que DEBE devolver JSON válido."""
        raw = self.generate(prompt, system=system, format_json=True)
        return parse_json_loose(raw)


def parse_json_loose(raw: str) -> dict:
    """Parsea JSON tolerando código Markdown envolvente y errores menores."""
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.strip("`")
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass
    # Intentar extraer el primer {...} balanceado
    start = raw.find("{")
    end = raw.rfind("}")
    if start != -1 and end > start:
        try:
            return json.loads(raw[start : end + 1])
        except json.JSONDecodeError:
            pass
    raise OllamaError(f"Ollama no devolvió JSON válido: {raw[:300]}")