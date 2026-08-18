"""Adaptador GitHub: releases y tags de repositorios vía API REST.

No se crea una nota por cada commit: solo releases y tags.
Usa GITHUB_TOKEN (opcional) para evitar límites de rate.
"""
from __future__ import annotations

import requests

from app.utils import text as t
from app.utils.logging import get_logger

from .base import FetchError, NormalizedArticle, SourceAdapter

logger = get_logger("collector")

API = "https://api.github.com"
UA = "TechIntelligence/0.1"


class GitHubAdapter(SourceAdapter):
    def __init__(self, source, token: str | None = None, timeout: int = 30):
        super().__init__(source)
        self.token = token or ""
        self.timeout = timeout

    @property
    def repo(self) -> str:
        if not self.source.repository:
            raise FetchError(f"Fuente '{self.source.id}' sin repository configurado")
        return self.source.repository

    def _get(self, url: str, params: dict | None = None) -> list | dict:
        headers = {"Accept": "application/vnd.github+json", "User-Agent": UA}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        resp = requests.get(url, headers=headers, params=params, timeout=self.timeout)
        if resp.status_code == 403 and not self.token:
            raise FetchError("Rate limit de GitHub alcanzado. Configura GITHUB_TOKEN.")
        if resp.status_code != 200:
            raise FetchError(f"GitHub API error {resp.status_code} en {url}")
        return resp.json()

    def fetch(self) -> list[NormalizedArticle]:
        repo = self.repo
        logger.info("GitHub fetch: %s", repo)

        releases = self._get(f"{API}/repos/{repo}/releases", {"per_page": 10})
        if not isinstance(releases, list):
            raise FetchError(f"Respuesta inesperada de GitHub para {repo}")

        # Tags solo si no hay releases (evita duplicar información)
        tags = []
        if not releases:
            resp = self._get(f"{API}/repos/{repo}/tags", {"per_page": 10})
            if isinstance(resp, list):
                tags = resp

        articles: list[NormalizedArticle] = []
        for rel in releases:
            body = t.clean_whitespace(t.strip_html(rel.get("body") or ""))
            title = f"{rel.get('name') or rel.get('tag_name', 'release')}"
            articles.append(NormalizedArticle(
                source_id=self.source.id,
                source_name=self.source.name,
                source_type="github",
                title=f"Release: {title} — {repo}",
                url=rel.get("html_url"),
                external_id=f"release-{rel.get('id')}",
                content=body or f"Release {rel.get('tag_name')} de {repo}.",
                published_at=(rel.get("published_at") or "").replace("T", " ")[:19],
            ))

        for tag in tags:
            articles.append(NormalizedArticle(
                source_id=self.source.id,
                source_name=self.source.name,
                source_type="github",
                title=f"Tag: {tag.get('name')} — {repo}",
                url=f"https://github.com/{repo}/releases/tag/{tag.get('name')}",
                external_id=f"tag-{tag.get('name')}",
                content=f"Nuevo tag {tag.get('name')} en {repo}.",
                published_at=None,
            ))

        logger.info("GitHub %s: %d ítems", repo, len(articles))
        return articles