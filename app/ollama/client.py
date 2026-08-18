"""Clientes HTTP para IA: Ollama local y OpenRouter (interfaz común).

- OllamaClient: API local /api/generate (sin dependencias externas).
- OpenRouterClient: API cloud /chat/completions (requiere OPENROUTER_API_KEY).
Ambos exponen generate(), generate_json(), is_available().
"""
from __future__ import annotations

import json

import requests

from app.utils.logging import get_logger

logger = get_logger("ollama")


class OllamaError(Exception):
    pass


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
    raise OllamaError(f"La IA no devolvió JSON válido: {raw[:300]}")


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


class OpenRouterClient:
    """Cliente para APIs cloud compatibles con OpenAI (chat completions).

    Usa OpenRouter por defecto; con base_url distinta sirve para otros
    proveedores OpenAI-compatibles (p. ej. OpenCode Zen).

    Soporta varios modelos: se rotan en cada llamada (round-robin) para
    repartir el trabajo y, si uno devuelve 429 (rate limit), se intenta
    con el siguiente automáticamente (failover).
    """

    BASE_URL = "https://openrouter.ai/api/v1"

    def __init__(self, api_key: str, model: str | None = None, models: list[str] | None = None,
                 timeout: int = 120, temperature: float = 0.1, base_url: str | None = None):
        self.api_key = api_key
        self.models = [m for m in (models or []) if m]
        if model and model not in self.models:
            self.models.insert(0, model)
        self.model = self.models[0] if self.models else (model or "")
        self.timeout = timeout
        self.temperature = temperature
        self._cursor = 0
        self.BASE_URL = (base_url or self.BASE_URL).rstrip("/")

    # ------------------------------------------------------------------

    def is_available(self, timeout: int = 5) -> bool:
        """Considera el backend disponible si el servidor responde (cualquier status)."""
        try:
            requests.get(f"{self.BASE_URL}/models", timeout=timeout)
            return True
        except requests.RequestException:
            return False

    def _next_model(self) -> str:
        """Devuelve el siguiente modelo en rotación (round-robin)."""
        model = self.models[self._cursor % len(self.models)]
        self._cursor += 1
        return model

    def _chat(self, prompt: str, system: str | None, format_json: bool) -> str:
        if not self.api_key:
            raise OllamaError("OPENROUTER_API_KEY no está configurada (.env)")
        if not self.models:
            raise OllamaError("OPENROUTER_MODEL no está configurado (.env)")

        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        # Failover: si un modelo devuelve 429, se prueba con el siguiente
        first_error: OllamaError | None = None
        for _ in range(len(self.models)):
            model = self._next_model()

            payload: dict = {
                "model": model,
                "messages": messages,
                "temperature": self.temperature,
            }
            if format_json:
                payload["response_format"] = {"type": "json_object"}

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }

            logger.info("OpenRouter generate: model=%s, prompt_len=%d", model, len(prompt))
            try:
                resp = requests.post(
                    f"{self.BASE_URL}/chat/completions",
                    json=payload,
                    headers=headers,
                    timeout=self.timeout,
                )
                if resp.status_code in (429, 502, 503, 504):
                    first_error = OllamaError(
                        f"Rate limit/sobrecarga de la API en {model} (HTTP {resp.status_code}): {resp.text[:200]}")
                    continue
                resp.raise_for_status()
                data = resp.json()
            except requests.Timeout as e:
                raise OllamaError(f"Timeout de OpenRouter ({self.timeout}s): {e}") from e
            except requests.RequestException as e:
                raise OllamaError(f"Error de conexión con OpenRouter: {e}") from e
            except json.JSONDecodeError as e:
                raise OllamaError(f"Respuesta no JSON de OpenRouter: {e}") from e

            try:
                response = data["choices"][0]["message"]["content"]
            except (KeyError, IndexError, TypeError) as e:
                raise OllamaError(f"Respuesta inesperada de OpenRouter: {data}") from e
            if not response.strip():
                raise OllamaError("OpenRouter devolvió una respuesta vacía")
            return response.strip()

        raise first_error or OllamaError("Todos los modelos de OpenRouter fallaron")

    def generate(self, prompt: str, system: str | None = None, format_json: bool = False) -> str:
        return self._chat(prompt, system, format_json)

    def generate_json(self, prompt: str, system: str | None = None) -> dict:
        raw = self._chat(prompt, system, format_json=True)
        return parse_json_loose(raw)