"""Health check del sistema."""
from __future__ import annotations

import shutil
import sqlite3
from pathlib import Path

from app.database import repository as repo
from app.ollama.client import OllamaClient, OpenRouterClient
from app.utils.logging import get_logger

logger = get_logger("collector")


class HealthReport:
    def __init__(self):
        self.checks: list[dict] = []

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.checks.append({"name": name, "ok": ok, "detail": detail})

    @property
    def ok(self) -> bool:
        return all(c["ok"] for c in self.checks)

    def render(self) -> str:
        lines = []
        for c in self.checks:
            status = "OK" if c["ok"] else "FAIL"
            lines.append(f"{c['name']:<12} {status:>5}  {c['detail']}")
        return "\n".join(lines)


def run_health(conn: sqlite3.Connection, settings) -> HealthReport:
    report = HealthReport()

    # SQLite
    try:
        conn.execute("SELECT 1").fetchone()
        st = repo.stats(conn)
        report.add("SQLite", True, f"{st['articles']} artículos")
    except sqlite3.Error as e:
        report.add("SQLite", False, str(e))

    # IA (backend configurado: Ollama local u OpenRouter)
    if settings.ai_backend == "openrouter":
        client = OpenRouterClient(settings.openrouter_api_key, settings.openrouter_model,
                                  timeout=settings.ollama_timeout)
        if client.is_available():
            report.add("OpenRouter", True, f"{settings.openrouter_model} (web search: {':online' in settings.openrouter_model})")
        else:
            report.add("OpenRouter", False, "sin conexión con openrouter.ai")
    else:
        client = OllamaClient(settings.ollama_base_url, settings.ollama_model,
                              timeout=settings.ollama_timeout)
        if client.is_available():
            installed = client.model_installed()
            detail = f"{settings.ollama_model} {'instalado' if installed else 'NO instalado'}"
            report.add("Ollama", installed, detail)
        else:
            report.add("Ollama", False, f"sin conexión en {settings.ollama_base_url}")

    # Vault
    vault = Path(settings.vault_path)
    vault_ok = vault.exists()
    report.add("Vault", vault_ok, str(vault) if vault_ok else "no existe")

    # Git
    git_ok = shutil.which("git") is not None
    if git_ok:
        git_repo = (vault.parent / ".git").exists() or (Path.cwd() / ".git").exists()
        report.add("Git", git_repo or True, "disponible" if git_repo else "repo no inicializado (se inicializará en sync)")
    else:
        report.add("Git", False, "git no está en PATH")

    # Sources
    st = repo.stats(conn)
    report.add("Sources", True, f"{st['sources_enabled']} habilitadas de {st['sources_total']}")
    report.add("Pending", True, str(st["pending"]))
    report.add("Failed", True, str(st["failed"]))
    report.add("Processed", True, str(st["processed"]))
    report.add("Errors", True, str(st["errors"]))

    return report