"""Configuración del sistema.

Prioridad de resolución (de mayor a menor):
1. Variables de entorno (.env)
2. config/settings.yaml
3. Valores por defecto
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass
class Settings:
    # IA: backend activo (ollama | openrouter)
    ai_backend: str = "ollama"

    # Ollama
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1"
    ollama_timeout: int = 120
    ollama_temperature: float = 0.1

    # OpenRouter
    openrouter_api_key: str = ""
    openrouter_model: str = "deepseek/deepseek-chat"
    openrouter_models: list[str] = field(default_factory=list)
    openrouter_timeout: int = 180

    # Rutas
    vault_path: Path = field(default_factory=lambda: PROJECT_ROOT / "vault")
    database_path: Path = field(default_factory=lambda: PROJECT_ROOT / "database" / "tech_intelligence.db")
    config_path: Path = field(default_factory=lambda: PROJECT_ROOT / "config")
    log_dir: Path = field(default_factory=lambda: PROJECT_ROOT / "logs")
    log_level: str = "INFO"

    # Scheduler
    sync_interval: int = 60

    # Procesamiento
    max_processing_attempts: int = 3
    long_content_chars: int = 15000
    processing_workers: int = 3
    hybrid_ollama: bool = False  # añade un worker extra con Ollama local (llama)

    # Git
    git_enabled: bool = True
    git_commit_prefix: str = "tech-intelligence: sync"

    # GitHub API
    github_token: str = ""

    @property
    def prompts_dir(self) -> Path:
        return PROJECT_ROOT / "app" / "ollama" / "prompts"

    @property
    def categories_path(self) -> Path:
        return self.config_path / "categories.yaml"

    @property
    def sources_path(self) -> Path:
        return self.config_path / "sources.yaml"

    @property
    def dataset_dir(self) -> Path:
        return self.vault_path / "13 - Dataset"

    @property
    def templates_dir(self) -> Path:
        return self.vault_path / "12 - Templates"


def _resolve(value: str | None, base: Path) -> str | None:
    """Convierte rutas relativas en absolutas respecto al proyecto."""
    if not value:
        return value
    p = Path(value)
    return str(p if p.is_absolute() else (base / p))


def load_settings(env_path: Path | None = None) -> Settings:
    """Carga la configuración: .env + settings.yaml + defaults."""
    load_dotenv(env_path or PROJECT_ROOT / ".env")

    s = Settings()

    # 1. settings.yaml
    cfg_file = PROJECT_ROOT / "config" / "settings.yaml"
    if cfg_file.exists():
        with open(cfg_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        ai = data.get("settings", {}).get("ai") or {}
        o = (data.get("settings") or {}).get("ollama") or {}
        s.ai_backend = ai.get("backend", s.ai_backend)
        s.openrouter_api_key = ai.get("openrouter_api_key", s.openrouter_api_key)
        s.openrouter_model = ai.get("openrouter_model", s.openrouter_model)
        s.openrouter_models = list(ai.get("openrouter_models") or [])
        s.openrouter_timeout = int(ai.get("openrouter_timeout", s.openrouter_timeout))
        s.ollama_base_url = o.get("base_url", s.ollama_base_url)
        s.ollama_model = o.get("model", s.ollama_model)
        s.ollama_timeout = int(o.get("timeout", s.ollama_timeout))
        s.ollama_temperature = float(o.get("temperature", s.ollama_temperature))
        s.vault_path = Path(_resolve(data.get("settings", {}).get("vault_path"), PROJECT_ROOT) or s.vault_path)
        s.database_path = Path(_resolve(data.get("settings", {}).get("database_path"), PROJECT_ROOT) or s.database_path)
        s.log_dir = Path(_resolve(data.get("settings", {}).get("log_dir"), PROJECT_ROOT) or s.log_dir)
        s.log_level = data.get("settings", {}).get("log_level", s.log_level)
        s.sync_interval = int(data.get("settings", {}).get("sync_interval", s.sync_interval))
        s.max_processing_attempts = int(data.get("settings", {}).get("max_processing_attempts", s.max_processing_attempts))
        s.long_content_chars = int(data.get("settings", {}).get("long_content_chars", s.long_content_chars))
        s.processing_workers = int(data.get("settings", {}).get("processing_workers", s.processing_workers))
        s.hybrid_ollama = bool(data.get("settings", {}).get("hybrid_ollama", s.hybrid_ollama))
        s.git_enabled = bool(data.get("settings", {}).get("git_enabled", s.git_enabled))
        s.git_commit_prefix = data.get("settings", {}).get("git_commit_prefix", s.git_commit_prefix)

    # 2. Variables de entorno (prioridad máxima)
    def _env(name: str) -> str | None:
        v = os.environ.get(name)
        return v if v not in (None, "", " ") else None

    if v := _env("AI_BACKEND"):
        s.ai_backend = v
    if v := _env("OLLAMA_BASE_URL"):
        s.ollama_base_url = v
    if v := _env("OLLAMA_MODEL"):
        s.ollama_model = v
    if v := _env("OLLAMA_TIMEOUT"):
        s.ollama_timeout = int(v)
    if v := _env("OPENROUTER_API_KEY"):
        s.openrouter_api_key = v
    if v := _env("OPENROUTER_MODEL"):
        s.openrouter_model = v
    if v := _env("OPENROUTER_MODELS"):
        s.openrouter_models = [m.strip() for m in v.split(",") if m.strip()]
    if v := _env("VAULT_PATH"):
        s.vault_path = Path(_resolve(v, PROJECT_ROOT) or v)
    if v := _env("DATABASE_PATH"):
        s.database_path = Path(_resolve(v, PROJECT_ROOT) or v)
    if v := _env("SYNC_INTERVAL"):
        s.sync_interval = int(v)
    if v := _env("LOG_LEVEL"):
        s.log_level = v
    if v := _env("GITHUB_TOKEN"):
        s.github_token = v
    if v := _env("MAX_PROCESSING_ATTEMPTS"):
        s.max_processing_attempts = int(v)
    if v := _env("PROCESSING_WORKERS"):
        s.processing_workers = int(v)
    if v := _env("HYBRID_OLLAMA"):
        s.hybrid_ollama = v.lower() in ("1", "true", "yes", "si")

    return s