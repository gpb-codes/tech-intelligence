"""Carga de configuración de fuentes, categorías y ajustes."""
from __future__ import annotations

from pathlib import Path

import yaml

from .models import Source


class ConfigError(Exception):
    pass


def load_sources(path: Path) -> list[Source]:
    if not path.exists():
        raise ConfigError(f"No existe el archivo de fuentes: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    raw = data.get("sources", [])
    sources = [Source.from_dict(d) for d in raw]
    ids = [s.id for s in sources]
    if len(set(ids)) != len(ids):
        raise ConfigError("IDs de fuentes duplicados en sources.yaml")
    return sources


def load_categories(path: Path) -> dict:
    """Devuelve {id_categoría: {name, folder}} y listas de valores válidos."""
    if not path.exists():
        raise ConfigError(f"No existe el archivo de categorías: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    categories = {}
    for c in data.get("categories", []):
        categories[c["id"]] = {"name": c["name"], "folder": c.get("folder", "02 - Updates/General Tech")}

    return {
        "categories": categories,
        "importance_levels": data.get("importance_levels", ["critical", "high", "medium", "low"]),
        "pricing_values": data.get("pricing_values", ["free", "freemium", "free-tier", "paid",
                                                      "open-source", "self-hosted", "enterprise", "unknown"]),
        "radar_rings": data.get("radar_rings", ["ADOPT", "TRIAL", "ASSESS", "HOLD"]),
    }


def load_settings_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}