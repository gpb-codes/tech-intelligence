"""Hashes y normalización para deduplicación robusta."""
from __future__ import annotations

import hashlib
import re
from urllib.parse import urlsplit, urlunsplit

_WS = re.compile(r"\s+")


def normalize_text(text: str | None) -> str:
    """Minúsculas, colapsa espacios, recorta."""
    if not text:
        return ""
    return _WS.sub(" ", text.strip().lower())


def content_hash(content: str | None) -> str | None:
    """Hash del contenido normalizado. None si no hay contenido."""
    norm = normalize_text(content)
    if not norm:
        return None
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def title_hash(title: str | None) -> str | None:
    """Hash del título normalizado. None si no hay título."""
    norm = normalize_text(title)
    if not norm:
        return None
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()


def canonical_url(url: str | None) -> str | None:
    """URL canónica: sin fragmento, sin slash final, host en minúsculas."""
    if not url:
        return None
    url = url.strip()
    try:
        parts = urlsplit(url)
        scheme = parts.scheme.lower()
        netloc = parts.netloc.lower()
        path = parts.path.rstrip("/")
        # Ignoramos query y fragmento para canonicalización
        return urlunsplit((scheme, netloc, path, "", ""))
    except Exception:
        return url