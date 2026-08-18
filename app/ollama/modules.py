"""Módulos de Ollama: traductor, resumidor, clasificador, extractor."""
from __future__ import annotations

from pathlib import Path

from app.utils.logging import get_logger

from .client import OllamaClient, OllamaError

logger = get_logger("ollama")

_PROMPT_CACHE: dict[str, str] = {}


def load_prompt(prompts_dir: Path, name: str) -> str:
    """Carga un prompt desde app/ollama/prompts/ (caché)."""
    if name not in _PROMPT_CACHE:
        path = prompts_dir / f"{name}.txt"
        if not path.exists():
            raise OllamaError(f"Prompt no encontrado: {path}")
        _PROMPT_CACHE[name] = path.read_text(encoding="utf-8")
    return _PROMPT_CACHE[name]


class Translator:
    """Traduce contenido no español al español usando el prompt de traducción."""

    def __init__(self, client: OllamaClient, prompts_dir: Path):
        self.client = client
        self.prompts_dir = prompts_dir

    def translate(self, content: str) -> str:
        prompt = load_prompt(self.prompts_dir, "translate").replace("{{CONTENT}}", content)
        return self.client.generate(prompt)


class Summarizer:
    """Resume contenido (traducido o no) en español."""

    def __init__(self, client: OllamaClient, prompts_dir: Path):
        self.client = client
        self.prompts_dir = prompts_dir

    def summarize(self, content: str) -> str:
        prompt = load_prompt(self.prompts_dir, "summarize").replace("{{CONTENT}}", content)
        return self.client.generate(prompt)


class Classifier:
    """Clasifica: empresa, producto, categoría, precio, licencia, tags."""

    VALID_CATEGORIES = ["AI", "Developer Tools", "Open Source", "Cloud",
                        "Cybersecurity", "Hardware", "Productivity", "General Tech"]
    VALID_PRICING = ["free", "freemium", "free-tier", "paid", "open-source",
                     "self-hosted", "enterprise", "unknown"]

    def __init__(self, client: OllamaClient, prompts_dir: Path):
        self.client = client
        self.prompts_dir = prompts_dir

    def classify(self, content: str) -> dict:
        prompt = load_prompt(self.prompts_dir, "classify").replace("{{CONTENT}}", content)
        data = self.client.generate_json(prompt)
        return self._validate(data)

    def _validate(self, data: dict) -> dict:
        category = data.get("category", "General Tech")
        if category not in self.VALID_CATEGORIES:
            logger.warning("Categoría inválida '%s' -> General Tech", category)
            category = "General Tech"

        pricing = data.get("pricing", "unknown")
        if pricing not in self.VALID_PRICING:
            logger.warning("Pricing inválido '%s' -> unknown", pricing)
            pricing = "unknown"

        return {
            "company": str(data.get("company", "") or "").strip(),
            "product": str(data.get("product", "") or "").strip(),
            "category": category,
            "subcategory": str(data.get("subcategory", "") or "").strip(),
            "pricing": pricing,
            "license": str(data.get("license", "unknown") or "unknown").strip(),
            "open_source": bool(data.get("open_source", False)),
            "self_hosted": bool(data.get("self_hosted", False)),
            "tags": [str(t).strip().lower() for t in (data.get("tags") or []) if str(t).strip()][:8],
        }


class MetadataExtractor:
    """Extrae versión, fecha, precio, URLs, requisitos, cambios."""

    def __init__(self, client: OllamaClient, prompts_dir: Path):
        self.client = client
        self.prompts_dir = prompts_dir

    def extract(self, content: str) -> dict:
        prompt = load_prompt(self.prompts_dir, "extract").replace("{{CONTENT}}", content)
        data = self.client.generate_json(prompt)
        return {
            "version": str(data.get("version", "") or "").strip(),
            "release_date": str(data.get("release_date", "") or "").strip(),
            "price": str(data.get("price", "") or "").strip(),
            "license": str(data.get("license", "") or "").strip(),
            "urls": [str(u) for u in (data.get("urls") or []) if str(u)][:10],
            "requirements": str(data.get("requirements", "") or "").strip(),
            "breaking_changes": str(data.get("breaking_changes", "") or "").strip(),
            "keywords": [str(k).strip() for k in (data.get("keywords") or []) if str(k).strip()][:8],
        }


class ImportanceAnalyzer:
    """Evalúa importancia e impacto."""

    VALID_IMPORTANCE = ["critical", "high", "medium", "low"]

    def __init__(self, client: OllamaClient, prompts_dir: Path):
        self.client = client
        self.prompts_dir = prompts_dir

    def analyze(self, content: str) -> dict:
        prompt = load_prompt(self.prompts_dir, "importance").replace("{{CONTENT}}", content)
        data = self.client.generate_json(prompt)

        importance = str(data.get("importance", "medium") or "medium").strip().lower()
        if importance not in self.VALID_IMPORTANCE:
            logger.warning("Importancia inválida '%s' -> medium", importance)
            importance = "medium"

        impact = str(data.get("impact", "medium") or "medium").strip().lower()
        if impact not in self.VALID_IMPORTANCE:
            impact = "medium"

        return {
            "importance": importance,
            "impact": impact,
            "audience": str(data.get("audience", "") or "").strip(),
            "reasons": [str(r).strip() for r in (data.get("reasons") or []) if str(r).strip()][:3],
        }


class AlternativeDetector:
    """Detecta alternativas (open source, gratuitas, self-hosted, etc.)."""

    def __init__(self, client: OllamaClient, prompts_dir: Path):
        self.client = client
        self.prompts_dir = prompts_dir

    def detect(self, content: str) -> list[dict]:
        prompt = load_prompt(self.prompts_dir, "alternative").replace("{{CONTENT}}", content)
        data = self.client.generate_json(prompt)
        alts = []
        for item in data.get("alternatives") or []:
            if isinstance(item, dict):
                name = str(item.get("name", "") or "").strip()
                confidence = str(item.get("confidence", "medium") or "medium").strip().lower()
                if name and confidence in ("high", "medium"):
                    alts.append({"name": name, "confidence": confidence})
        return alts[:6]


class InsightsGenerator:
    """Genera un mini informe profesional: qué es, ayuda al desarrollo y relevancia por rol."""

    VALID_ROLES = ["Trainee", "Junior", "Semi-Senior", "Senior", "Ingeniero de Software",
                   "Ingeniero en Redes", "DevOps / SRE", "Ciberseguridad"]
    VALID_RELEVANCE = ["Alta", "Media", "Baja"]

    def __init__(self, client: OllamaClient, prompts_dir: Path):
        self.client = client
        self.prompts_dir = prompts_dir

    def generate(self, content: str) -> dict:
        prompt = load_prompt(self.prompts_dir, "insights").replace("{{CONTENT}}", content)
        data = self.client.generate_json(prompt)
        return self._validate(data)

    def _validate(self, data: dict) -> dict:
        profiles = []
        for item in data.get("profiles") or []:
            if not isinstance(item, dict):
                continue
            role = str(item.get("role", "") or "").strip()
            if not role:
                continue
            relevance = str(item.get("relevance", "Media") or "Media").strip()
            if relevance not in self.VALID_RELEVANCE:
                logger.warning("Relevancia inválida '%s' -> Media", relevance)
                relevance = "Media"
            must_know = [str(k).strip() for k in (item.get("must_know") or []) if str(k).strip()][:3]
            profiles.append({"role": role, "relevance": relevance, "must_know": must_know})
        return {
            "what_is": str(data.get("what_is", "") or "").strip(),
            "why_development": str(data.get("why_development", "") or "").strip(),
            "profiles": profiles[:8],
        }