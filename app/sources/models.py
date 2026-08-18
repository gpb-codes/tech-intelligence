"""Modelo de datos de una fuente configurada."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Source:
    id: str
    name: str
    type: str  # rss | github | api
    enabled: bool = True
    url: str | None = None
    repository: str | None = None  # para github: owner/repo
    category: str = "General Tech"
    priority: str = "medium"  # high | medium | low
    note: str | None = None
    extra: dict = field(default_factory=dict)

    @classmethod
    def from_dict(cls, d: dict) -> "Source":
        return cls(
            id=str(d.get("id", "")).strip(),
            name=str(d.get("name", d.get("id", ""))).strip(),
            type=str(d.get("type", "rss")).strip().lower(),
            enabled=bool(d.get("enabled", True)),
            url=d.get("url"),
            repository=d.get("repository"),
            category=d.get("category", "General Tech"),
            priority=d.get("priority", "medium"),
            note=d.get("note"),
            extra={k: v for k, v in d.items() if k not in
                   ("id", "name", "type", "enabled", "url", "repository", "category", "priority", "note")},
        )

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "enabled": self.enabled,
            "url": self.url,
            "repository": self.repository,
            "category": self.category,
            "priority": self.priority,
            "note": self.note,
            **self.extra,
        }