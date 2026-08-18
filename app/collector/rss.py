"""Adaptador RSS/Atom basado en feedparser."""
from __future__ import annotations

import email.utils
from datetime import datetime, timezone

import feedparser
import requests

from app.utils import text as t
from app.utils.logging import get_logger

from .base import FetchError, NormalizedArticle, SourceAdapter

logger = get_logger("collector")

UA = "Mozilla/5.0 (compatible; TechIntelligence/0.1; +local)"

_DT_FORMATS = ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M",
               "%Y-%m-%d %H:%M:%S", "%Y-%m-%d")


def _parse_date(value) -> str | None:
    if not value:
        return None
    if isinstance(value, (tuple, list)):
        try:
            return datetime(*value[:6]).replace(tzinfo=timezone.utc).isoformat(timespec="seconds")
        except Exception:
            return None
    s = str(value)
    # RFC 2822 (pubDate) -> struct_time ya convertido por feedparser
    if isinstance(value, __import__("time").struct_time):
        return datetime(*value[:6]).replace(tzinfo=timezone.utc).isoformat(timespec="seconds")
    try:
        parsed = email.utils.parsedate_to_datetime(s)
        if parsed:
            return parsed.astimezone(timezone.utc).isoformat(timespec="seconds")
    except Exception:
        pass
    for fmt in _DT_FORMATS:
        try:
            return datetime.strptime(s[: len(fmt)], fmt).replace(tzinfo=timezone.utc).isoformat(timespec="seconds")
        except ValueError:
            continue
    return None


class RSSAdapter(SourceAdapter):
    """Fuente RSS/Atom."""

    def __init__(self, source, timeout: int = 30):
        super().__init__(source)
        self.timeout = timeout

    def fetch(self) -> list[NormalizedArticle]:
        if not self.source.url:
            raise FetchError(f"Fuente '{self.source.id}' sin URL configurada")

        logger.info("RSS fetch: %s (%s)", self.source.id, self.source.url)
        try:
            resp = requests.get(self.source.url, timeout=self.timeout, headers={"User-Agent": UA})
            resp.raise_for_status()
        except requests.RequestException as e:
            raise FetchError(f"Error HTTP al leer {self.source.url}: {e}") from e

        parsed = feedparser.parse(resp.content)
        if parsed.get("bozo") and not parsed.entries:
            raise FetchError(f"Feed no válido: {parsed.get('bozo_exception')}")

        articles = []
        for entry in parsed.entries:
            title = t.clean_whitespace(t.strip_html(entry.get("title", "")))
            if not title:
                continue

            # contenido: content:encoded > summary > description
            content = ""
            if entry.get("content"):
                content = entry.content[0].get("value", "")
            if not content:
                content = entry.get("summary", "") or entry.get("description", "")
            content = t.clean_whitespace(t.strip_html(content))

            url = entry.get("link")
            published = _parse_date(entry.get("published_parsed") or entry.get("updated_parsed")
                                    or entry.get("published") or entry.get("updated"))

            articles.append(NormalizedArticle(
                source_id=self.source.id,
                source_name=self.source.name,
                source_type="rss",
                title=title,
                url=url,
                external_id=str(entry.get("id") or entry.get("guid") or url or ""),
                content=content,
                published_at=published,
            ))
        logger.info("RSS %s: %d entradas", self.source.id, len(articles))
        return articles