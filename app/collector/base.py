"""Base de adaptadores de fuentes y modelo interno de artículo."""
from __future__ import annotations

import abc
from dataclasses import dataclass, field

from app.utils.hashing import canonical_url, content_hash, title_hash


@dataclass
class NormalizedArticle:
    """Formato interno común devuelto por todos los adaptadores."""

    source_id: str
    source_name: str
    source_type: str
    title: str
    url: str | None = None
    external_id: str | None = None
    content: str | None = None
    published_at: str | None = None
    language: str | None = None
    status: str = "new"
    example: bool = False

    def to_dict(self) -> dict:
        return {
            "source_id": self.source_id,
            "source_name": self.source_name,
            "source_type": self.source_type,
            "title": self.title,
            "url": self.url,
            "external_id": self.external_id,
            "content": self.content,
            "published_at": self.published_at,
            "language": self.language,
            "status": self.status,
            "example": self.example,
            "canonical_url": canonical_url(self.url),
            "content_hash": content_hash(self.content),
            "title_hash": title_hash(self.title),
        }


class SourceAdapter(abc.ABC):
    """Interfaz común de adaptadores de fuente."""

    def __init__(self, source):
        self.source = source

    @abc.abstractmethod
    def fetch(self) -> list[NormalizedArticle]:
        """Devuelve los artículos normalizados de la fuente."""
        raise NotImplementedError


class FetchError(Exception):
    """Error al recopilar una fuente. No detiene el pipeline."""
    pass