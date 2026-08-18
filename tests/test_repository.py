import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database import repository as repo


def test_insert_and_dedup(db):
    from app.collector.base import NormalizedArticle

    a = NormalizedArticle(
        source_id="s1", source_name="Src", source_type="rss",
        title="Título uno", url="https://a.com/1", external_id="e1",
        content="Contenido uno", published_at="2026-08-17T10:00:00Z",
    )
    row = repo.insert_article(db, a.to_dict())
    assert row["ti_id"].startswith("ti-")
    assert repo.count_articles(db) == 1
    assert repo.count_articles(db, status="new") == 1


def test_next_ti_id_sequence(db):
    from app.collector.base import NormalizedArticle

    for i in range(3):
        a = NormalizedArticle(
            source_id="s", source_name="S", source_type="rss",
            title=f"T {i}", url=f"https://a.com/{i}", external_id=f"e{i}",
            content="c", published_at=None,
        )
        repo.insert_article(db, a.to_dict())
    first = repo.next_ti_id(db)
    second = repo.next_ti_id(db)
    assert int(first.rsplit("-", 1)[1]) < int(second.rsplit("-", 1)[1])


def test_sources_crud(db):
    src = {"id": "x", "name": "X", "type": "rss", "url": "https://x.com/feed",
           "enabled": True, "category": "AI", "priority": "high"}
    repo.upsert_source(db, src)
    assert repo.get_source(db, "x")["name"] == "X"
    assert len(repo.list_sources(db)) == 1
    repo.upsert_source(db, {**src, "name": "X2"})
    assert repo.get_source(db, "x")["name"] == "X2"


def test_processing_flow(db):
    from app.collector.base import NormalizedArticle

    a = NormalizedArticle(
        source_id="s", source_name="S", source_type="rss",
        title="T", url="https://a.com/1", external_id="e1",
        content="Contenido a procesar", published_at="2026-08-17T10:00:00Z",
    )
    row = repo.insert_article(db, a.to_dict())
    job_id = repo.create_job(db, row["id"])
    repo.job_started(db, job_id)
    repo.save_result(db, row["id"], {
        "model": "m", "language": "en", "translated": True, "translation": "Tr",
        "summary": "- S", "classification": {"category": "AI"}, "metadata": {},
    })
    repo.job_finished(db, job_id, ok=True)
    repo.set_article_status(db, row["id"], repo.STATUS_PROCESSED)

    assert repo.count_articles(db, status="processed") == 1
    assert repo.has_result(db, row["id"])
    assert repo.stats(db)["processed"] == 1


def test_errors(db):
    repo.log_error(db, "src1", "boom")
    assert repo.count_errors(db) == 1
    repo.increment_error_retry(db, "src1")
    assert repo.list_errors(db)[0]["retry_count"] == 1