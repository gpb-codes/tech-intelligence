"""Adaptador API genérica: REST JSON configurable.

Configuración en sources.yaml (campo extra):
  api:
    method: GET
    params: {}                  # query params fijos
    headers: {}                 # headers fijos
    json_path: "items"          # ruta (puntos) a la lista de ítems
    fields:
      id: "id"
      title: "name"
      url: "html_url"
      content: "body"
      published_at: "created_at"
"""
from __future__ import annotations

import json

import requests

from app.utils.logging import get_logger

from .base import FetchError, NormalizedArticle, SourceAdapter

logger = get_logger("collector")
UA = "TechIntelligence/0.1"


def _get_path(data, path: str | None):
    """Resuelve 'a.b.c' en dicts/listas."""
    if not path:
        return None
    cur = data
    for key in path.split("."):
        if isinstance(cur, list):
            try:
                cur = cur[int(key)]
            except (ValueError, IndexError):
                return None
        elif isinstance(cur, dict):
            cur = cur.get(key)
        else:
            return None
    return cur


class APIAdapter(SourceAdapter):
    """Fuente REST API genérica que devuelve JSON."""

    def __init__(self, source, timeout: int = 30):
        super().__init__(source)
        self.timeout = timeout

    def fetch(self) -> list[NormalizedArticle]:
        cfg = self.source.extra.get("api") or {}
        url = self.source.url or cfg.get("url")
        if not url:
            raise FetchError(f"Fuente API '{self.source.id}' sin URL")

        try:
            resp = requests.request(
                method=cfg.get("method", "GET"),
                url=url,
                params=cfg.get("params"),
                headers={"User-Agent": UA, **(cfg.get("headers") or {})},
                timeout=self.timeout,
            )
            resp.raise_for_status()
            data = resp.json()
        except (requests.RequestException, json.JSONDecodeError) as e:
            raise FetchError(f"Error API {url}: {e}") from e

        items = _get_path(data, cfg.get("json_path", "items"))
        if not isinstance(items, list):
            items = [data]

        fields = cfg.get("fields", {})
        articles = []
        for it in items:
            title = _get_path(it, fields.get("title", "title"))
            if not title:
                continue
            articles.append(NormalizedArticle(
                source_id=self.source.id,
                source_name=self.source.name,
                source_type="api",
                title=str(title),
                url=str(_get_path(it, fields.get("url")) or ""),
                external_id=str(_get_path(it, fields.get("id")) or ""),
                content=str(_get_path(it, fields.get("content")) or ""),
                published_at=_get_path(it, fields.get("published_at")),
            ))
        logger.info("API %s: %d ítems", self.source.id, len(articles))
        return articles