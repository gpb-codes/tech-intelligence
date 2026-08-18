"""Logging con rotación para los 4 logs del sistema."""
from __future__ import annotations

import logging
import logging.handlers
from pathlib import Path

LOG_FILES = {
    "collector": "collector.log",
    "processor": "processor.log",
    "ollama": "ollama.log",
    "errors": "errors.log",
}

_configured = False


def setup_logging(log_dir: Path, level: str = "INFO") -> None:
    """Configura los loggers con rotación (5 MB, 3 backups)."""
    global _configured
    if _configured:
        return

    log_dir.mkdir(parents=True, exist_ok=True)
    numeric_level = getattr(logging, level.upper(), logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Logger raíz del sistema
    root = logging.getLogger("tech")
    root.setLevel(numeric_level)
    root.propagate = False

    # Consola
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    root.addHandler(console)

    # Archivos rotativos por dominio
    for name, fname in LOG_FILES.items():
        handler = logging.handlers.RotatingFileHandler(
            log_dir / fname,
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding="utf-8",
        )
        handler.setFormatter(formatter)
        handler.setLevel(logging.ERROR if name == "errors" else numeric_level)
        root.addHandler(handler)

    # Mapeo de dominios a archivos
    for name in LOG_FILES:
        logger = logging.getLogger(f"tech.{name}")
        logger.setLevel(numeric_level)
        logger.propagate = True

    _configured = True


def get_logger(domain: str) -> logging.Logger:
    """Devuelve un logger del dominio indicado (collector|processor|ollama|errors)."""
    if domain not in LOG_FILES:
        domain = "collector"
    return logging.getLogger(f"tech.{domain}")


def get_error_logger() -> logging.Logger:
    return logging.getLogger("tech.errors")