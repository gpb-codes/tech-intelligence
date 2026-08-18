"""Utilidades de texto: limpieza de HTML, truncado, sanitización."""
from __future__ import annotations

import html
import re

_TAG_RE = re.compile(r"<[^>]+>")
_MD_RE = re.compile(r"[#>*`_\[\]~-]{1,3}")
_WS_RE = re.compile(r"\s+")


def strip_html(text: str | None) -> str:
    """Elimina etiquetas HTML y decodifica entidades."""
    if not text:
        return ""
    text = _TAG_RE.sub(" ", text)
    text = html.unescape(text)
    return text.strip()


def strip_markdown(text: str | None) -> str:
    if not text:
        return ""
    return _MD_RE.sub("", text).strip()


def clean_whitespace(text: str | None) -> str:
    if not text:
        return ""
    return _WS_RE.sub(" ", text).strip()


def truncate(text: str | None, limit: int = 500) -> str:
    if not text:
        return ""
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "…"


def safe_filename(name: str, max_len: int = 80) -> str:
    """Convierte un texto en nombre de archivo seguro (Windows/macOS/Linux)."""
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', " ", name)
    name = _WS_RE.sub(" ", name).strip().strip(".")
    if not name:
        name = "sin-titulo"
    return name[:max_len].rstrip()


def slugify(text: str, max_len: int = 60) -> str:
    """Slug para enlaces y carpetas."""
    text = re.sub(r"[^A-Za-z0-9\s-]", " ", text)
    text = _WS_RE.sub("-", text.strip().lower())
    return text[:max_len].rstrip("-") or "untitled"