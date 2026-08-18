"""Exportador JSONL: dataset limpio en vault/13 - Dataset/."""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from app.database import repository as repo
from app.utils.logging import get_logger

logger = get_logger("collector")


def _classification(article: dict) -> dict:
    try:
        return json.loads(article.get("classification") or "{}")
    except json.JSONDecodeError:
        return {}


def _base_record(article: dict, cls: dict) -> dict:
    """Registro base con calidad mínima de datos (source, url, date, title, content)."""
    return {
        "id": article.get("ti_id"),
        "type": "update",
        "title": article.get("title"),
        "original_title": article.get("title"),
        "source": article.get("source_name"),
        "source_url": article.get("url"),
        "date": (article.get("published_at") or "")[:10] or None,
        "content": article.get("translation") or article.get("content"),
        "summary": article.get("summary"),
        "category": cls.get("category"),
        "company": cls.get("company"),
        "product": cls.get("product"),
        "importance": cls.get("importance"),
        "impact": cls.get("impact"),
        "pricing": cls.get("pricing"),
        "license": cls.get("license"),
        "open_source": cls.get("open_source"),
        "self_hosted": cls.get("self_hosted"),
        "language": article.get("language"),
        "translated": bool(article.get("translated")),
        "model": article.get("model"),
        "example": bool(article.get("example")),
        "confidence": cls.get("confidence", "medium"),
        "tags": cls.get("tags", []),
        "alternatives": cls.get("alternatives", []),
        "metadata": cls.get("extracted", {}),
    }


def _is(type_name: str, article: dict, cls: dict) -> bool:
    cat = cls.get("category") or ""
    product = cls.get("product") or ""
    if type_name == "update":
        return True
    if type_name == "tool":
        return cat in ("Developer Tools", "Productivity", "Open Source")
    if type_name == "model":
        return cat == "AI" and bool(product)
    if type_name == "company":
        return bool(cls.get("company"))
    if type_name == "alternative":
        return bool(cls.get("alternatives"))
    return False


def export_jsonl(conn: sqlite3.Connection, settings) -> dict[str, Path]:
    """Genera updates/tools/models/companies/alternatives/all.jsonl."""
    articles = repo.articles_with_results(conn, limit=5000)
    out_dir = Path(settings.dataset_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    files: dict[str, Path] = {}
    for name in ("updates", "tools", "models", "companies", "alternatives", "all"):
        files[name] = out_dir / f"{name}.jsonl"

    for path in files.values():
        path.write_text("", encoding="utf-8")

    with open(files["all"], "a", encoding="utf-8") as f_all:
        for article in articles:
            cls = _classification(article)
            rec = _base_record(article, cls)
            for name in ("updates", "tools", "models", "companies", "alternatives"):
                type_name = name[:-1] if name.endswith("s") else name
                if _is(type_name, article, cls):
                    with open(files[name], "a", encoding="utf-8") as f:
                        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f_all.write(json.dumps(rec, ensure_ascii=False) + "\n")

    counts = {name: sum(1 for _ in p.open(encoding="utf-8")) for name, p in files.items()}
    logger.info("JSONL exportado: %s", counts)
    return files