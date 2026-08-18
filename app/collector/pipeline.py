"""Deduplicación y pipeline de recopilación."""
from __future__ import annotations

import sqlite3

from app.database import repository as repo
from app.utils.logging import get_logger

from .base import FetchError, NormalizedArticle, SourceAdapter

logger = get_logger("collector")


class Deduplicator:
    """Aplica el orden de prioridad de deduplicación.

    1. canonical_url
    2. external_id (source_id + external_id)
    3. content_hash
    4. title_hash + fecha de publicación próxima
    """

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def is_duplicate(self, article: NormalizedArticle, article_id_hint: int | None = None) -> tuple[bool, str | None, dict | None]:
        """Devuelve (es_duplicado, razón, artículo_existente)."""
        data = article.to_dict()
        if article_id_hint is not None:
            data["_id"] = article_id_hint
        dup = repo.find_duplicate(self.conn, data)
        if dup:
            existing, reason = dup
            return True, reason, existing
        return False, None, None

    def detect_update(self, article: NormalizedArticle, existing: dict) -> bool:
        """¿La fuente actualizó el contenido de un artículo existente?"""
        return bool(
            existing.get("content_hash")
            and article.to_dict().get("content_hash")
            and existing["content_hash"] != article.to_dict()["content_hash"]
        )


class CollectResult:
    def __init__(self):
        self.fetched = 0
        self.new = 0
        self.duplicates = 0
        self.updated = 0
        self.errors: list[tuple[str, str]] = []
        self.sources_checked = 0


def collect(conn: sqlite3.Connection, sources: list, settings, only: list[str] | None = None) -> CollectResult:
    """Ejecuta la recopilación de todas las fuentes habilitadas.

    Un fallo en una fuente no detiene el pipeline.
    """
    result = CollectResult()
    dedup = Deduplicator(conn)

    from app.collector.api import APIAdapter
    from app.collector.github import GitHubAdapter
    from app.collector.rss import RSSAdapter

    for source in sources:
        if only and source.id not in only:
            continue
        if not source.enabled:
            continue

        try:
            if source.type == "rss":
                adapter = RSSAdapter(source)
            elif source.type == "github":
                adapter = GitHubAdapter(source, token=settings.github_token)
            elif source.type == "api":
                adapter = APIAdapter(source)
            else:
                raise FetchError(f"Tipo de fuente desconocido: {source.type}")

            articles = adapter.fetch()
        except FetchError as e:
            logger.error("Fuente %s falló: %s", source.id, e)
            repo.log_error(conn, source.id, str(e))
            result.errors.append((source.id, str(e)))
            continue
        except Exception as e:  # nunca detener el pipeline por una fuente
            logger.exception("Error inesperado en fuente %s", source.id)
            repo.log_error(conn, source.id, str(e))
            result.errors.append((source.id, str(e)))
            continue

        result.sources_checked += 1
        result.fetched += len(articles)

        for article in articles:
            is_dup, reason, existing = dedup.is_duplicate(article)
            if is_dup:
                if existing and dedup.detect_update(article, existing):
                    # La fuente actualizó el artículo: re-procesar
                    repo.update_article(conn, existing["id"], {
                        "content": article.content,
                        "content_hash": article.to_dict()["content_hash"],
                        "title": article.title,
                        "title_hash": article.to_dict()["title_hash"],
                        "status": repo.STATUS_NEW if existing["status"] in (repo.STATUS_PROCESSED, repo.STATUS_PENDING)
                                   else existing["status"],
                        "language": None,
                        "url": article.url,
                        "canonical_url": article.to_dict()["canonical_url"],
                    })
                    repo.log_error(conn, source.id, f"Artículo actualizado (re-procesado): {article.title[:80]}")
                    result.updated += 1
                else:
                    result.duplicates += 1
                continue

            repo.insert_article(conn, article.to_dict())
            result.new += 1

        repo.touch_source(conn, source.id)

    return result