from app.collector.base import NormalizedArticle
from app.collector.pipeline import Deduplicator
from app.database import repository as repo


def _article(title="T", url="https://a.com/x", ext="ext-1", content="contenido"):
    return NormalizedArticle(
        source_id="src1", source_name="Src 1", source_type="rss",
        title=title, url=url, external_id=ext, content=content,
        published_at="2026-08-17T10:00:00Z",
    )


def test_duplicate_by_canonical_url(db):
    repo.insert_article(db, _article().to_dict())
    dup = Deduplicator(db)
    is_dup, reason, _ = dup.is_duplicate(_article())
    assert is_dup and reason == "canonical_url"


def test_duplicate_by_external_id(db):
    a = _article(url="https://a.com/different-path")
    repo.insert_article(db, a.to_dict())
    b = _article(url="https://a.com/other")
    is_dup, reason, _ = Deduplicator(db).is_duplicate(b)
    assert is_dup and reason == "external_id"


def test_duplicate_by_content_hash(db):
    a = _article(url="https://a.com/u1", ext="e1")
    repo.insert_article(db, a.to_dict())
    b = _article(url="https://a.com/u2", ext="e2")
    is_dup, reason, _ = Deduplicator(db).is_duplicate(b)
    assert is_dup and reason == "content_hash"


def test_not_duplicate(db):
    a = _article(title="Título A", url="https://a.com/1", ext="x1", content="c1")
    repo.insert_article(db, a.to_dict())
    b = _article(title="Título B", url="https://a.com/2", ext="x2", content="c2")
    is_dup, _, _ = Deduplicator(db).is_duplicate(b)
    assert not is_dup


def test_detect_update(db):
    a = _article(content="versión original del contenido")
    row = repo.insert_article(db, a.to_dict())
    changed = _article(content="contenido actualizado por la fuente")
    dup = Deduplicator(db)
    is_dup, reason, existing = dup.is_duplicate(changed)
    # Mismo canonical_url pero contenido distinto
    assert is_dup and reason == "canonical_url"
    assert dup.detect_update(changed, existing) is True
    assert row["id"] == existing["id"]