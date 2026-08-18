"""Integración Git: versionado del Vault con seguridad."""
from __future__ import annotations

import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from app.utils.logging import get_logger

logger = get_logger("collector")

FORBIDDEN_COMMANDS = ("push --force", "reset --hard", "clean -fd")


class GitError(Exception):
    pass


def _run(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    if shutil.which("git") is None:
        raise GitError("git no está en PATH")
    return subprocess.run(args, cwd=str(cwd), capture_output=True, text=True, timeout=120)


def is_repo(path: Path) -> bool:
    try:
        r = _run(["git", "rev-parse", "--is-inside-work-tree"], path)
        return r.returncode == 0 and r.stdout.strip() == "true"
    except GitError:
        return False


def init(path: Path) -> bool:
    """Inicializa el repositorio si no existe. Devuelve True si lo creó."""
    if is_repo(path):
        return False
    r = _run(["git", "init"], path)
    if r.returncode != 0:
        raise GitError(f"git init falló: {r.stderr.strip()}")
    logger.info("Repositorio git inicializado en %s", path)
    return True


def commit(path: Path, message: str, paths: list[str] | None = None) -> bool:
    """Añade y commitea cambios. Devuelve True si hubo commit (no vacío)."""
    for bad in FORBIDDEN_COMMANDS:
        if bad in message.lower():
            raise GitError(f"Comando prohibido en mensaje: {bad}")

    r = _run(["git", "status", "--porcelain"], path)
    if r.returncode != 0:
        raise GitError(f"git status falló: {r.stderr.strip()}")
    if not r.stdout.strip():
        return False  # sin cambios -> no commit vacío

    if paths:
        _run(["git", "add", "--", *paths], path)
    else:
        _run(["git", "add", "-A"], path)

    r = _run(["git", "commit", "-m", message], path)
    if r.returncode != 0 and "nothing to commit" not in r.stderr:
        raise GitError(f"git commit falló: {r.stderr.strip()}")
    logger.info("Commit: %s", message)
    return True


def commit_after_sync(vault_path: Path, prefix: str = "tech-intelligence: sync") -> bool:
    """Commit automático tras un ciclo de sync exitoso."""
    vault = Path(vault_path)
    if not vault.exists():
        logger.warning("Vault no existe, no se commitea")
        return False

    repo_root = _find_repo_root(vault)
    if repo_root is None:
        init(vault.parent)
        repo_root = vault.parent

    message = f"{prefix} {datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
    return commit(repo_root, message, paths=[str(vault)])


def _find_repo_root(path: Path) -> Path | None:
    cur = path
    while True:
        if (cur / ".git").exists():
            return cur
        if cur.parent == cur:
            return None
        cur = cur.parent
    return None