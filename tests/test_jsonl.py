import json

from app.exporters.jsonl import export_jsonl
from app.database import repository as repo
from app.collector.base import NormalizedArticle


def test_jsonl_export(db, settings):
    a = NormalizedArticle(
        source_id="src", source_name="Src", source_type="rss",
        title="Nuevo modelo de IA", url="https://a.com/1", external_id="e1",
        content="Un modelo nuevo de IA para desarrolladores.",
        published_at="2026-08-17T10:00:00Z",
    )
    row = repo.insert_article(db, a.to_dict())
    repo.save_result(db, row["id"], {
        "model": "llama3.1", "language": "en", "translated": True,
        "translation": "Un modelo nuevo de IA para desarrolladores.",
        "summary": "- Nuevo modelo.",
        "classification": {
            "company": "Ejemplo Inc", "product": "Model-X",
            "category": "AI", "importance": "high", "impact": "medium",
            "pricing": "unknown", "license": "unknown",
            "open_source": False, "self_hosted": False,
            "tags": ["ai"], "alternatives": [], "extracted": {},
            "confidence": "high",
        },
        "metadata": {},
    })
    repo.set_article_status(db, row["id"], repo.STATUS_PROCESSED)

    files = export_jsonl(db, settings)

    lines = files["all"].read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1
    rec = json.loads(lines[0])
    assert rec["title"] == "Nuevo modelo de IA"
    assert rec["source"] == "Src"
    assert rec["source_url"] == "https://a.com/1"
    assert rec["date"] == "2026-08-17"
    assert rec["category"] == "AI"
    assert rec["company"] == "Ejemplo Inc"

    models_lines = files["models"].read_text(encoding="utf-8").strip().splitlines()
    assert len(models_lines) == 1  # categoría AI + producto

    updates = files["updates"].read_text(encoding="utf-8").strip().splitlines()
    assert len(updates) == 1