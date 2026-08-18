from app.collector.base import NormalizedArticle
from app.database import repository as repo
from app.generator.markdown import NoteGenerator


def _article():
    return NormalizedArticle(
        source_id="openai", source_name="OpenAI Blog", source_type="rss",
        title="OpenAI lanza un nuevo modelo de razonamiento",
        url="https://openai.com/index/nuevo-modelo",
        external_id="guid-1",
        content="OpenAI ha anunciado un nuevo modelo de razonamiento para su API con mejoras en código y matemáticas.",
        published_at="2026-08-17T10:00:00Z",
    )


def test_markdown_generation(db, settings):
    row = repo.insert_article(db, _article().to_dict())
    result = {
        "model": "llama3.1", "language": "en", "translated": True,
        "translation": "OpenAI ha anunciado un nuevo modelo de razonamiento para su API.",
        "summary": "- Nuevo modelo de razonamiento.\n- Mejoras en código.",
        "classification": {
            "company": "OpenAI", "product": "GPT", "category": "AI",
            "subcategory": "modelos", "pricing": "paid", "license": "unknown",
            "open_source": False, "self_hosted": False,
            "tags": ["openai", "modelo"],
            "importance": "high", "impact": "high",
            "reasons": ["Es un lanzamiento importante"],
            "confidence": "high",
            "alternatives": [], "extracted": {"version": "9.9", "price": "$20/mes"},
        },
        "metadata": {"version": "9.9", "price": "$20/mes"},
    }
    repo.save_result(db, row["id"], result)

    gen = NoteGenerator(db, settings)
    path = gen.generate(row["id"], result)

    assert path is not None
    assert path.exists()
    text = path.read_text(encoding="utf-8")

    # Frontmatter YAML
    assert "type: update" in text
    assert "id:" in text and "ti-" in text
    assert "title:" in text
    assert "original_language: en" in text
    assert "translated: true" in text
    assert "importance: high" in text
    assert "pricing: paid" in text
    assert "processed_by: ollama" in text
    assert "example: false" in text
    assert "tags:" in text

    # Cuerpo (diseño con callouts y badges)
    assert "# OpenAI lanza un nuevo modelo de razonamiento" in text
    assert "[!abstract] Resumen" in text
    assert "## ¿Qué ocurrió?" in text
    assert "[!info] Traducción del anuncio" in text
    assert "## ¿Por qué importa?" in text
    assert "[!success] Impacto" in text
    assert "## Información técnica" in text
    assert "## Precio" in text
    assert "[!money]" in text
    assert "## Fuente original" in text
    assert "## Contenido original" in text
    assert "https://openai.com/index/nuevo-modelo" in text
    assert "🟢 Alta" in text
    assert "🚀 Alto" in text
    assert "| Empresa | **OpenAI** |" in text

    # Ruta correcta: Updates/AI (importancia high)
    assert "02 - Updates" in str(path) and "AI" in str(path)


def test_markdown_low_importance_goes_to_review(db, settings):
    row = repo.insert_article(db, _article().to_dict())
    result = {
        "model": "m", "language": "es", "translated": False,
        "translation": None,
        "summary": "- Menor.",
        "classification": {
            "category": "AI", "importance": "low", "impact": "low",
            "pricing": "unknown", "license": "unknown",
            "tags": [], "alternatives": [], "extracted": {},
            "confidence": "medium",
        },
        "metadata": {},
    }
    repo.save_result(db, row["id"], result)
    gen = NoteGenerator(db, settings)
    path = gen.generate(row["id"], result)
    assert "01 - Inbox" in str(path) and "Review" in str(path)


def test_markdown_long_content_goes_to_inbox_sources(db, settings):
    settings.long_content_chars = 50
    a = _article()
    a.content = "x" * 300
    row = repo.insert_article(db, a.to_dict())
    result = {
        "model": "m", "language": "en", "translated": True,
        "translation": "traducción", "summary": "- S.",
        "classification": {
            "category": "AI", "importance": "medium", "impact": "medium",
            "pricing": "unknown", "license": "unknown",
            "tags": [], "alternatives": [], "extracted": {},
            "confidence": "high",
        },
        "metadata": {},
    }
    repo.save_result(db, row["id"], result)
    gen = NoteGenerator(db, settings)
    path = gen.generate(row["id"], result)
    assert path.exists()
    # Debe existir la nota de contenido original en Inbox/Sources
    source_dir = settings.vault_path / "01 - Inbox" / "Sources"
    assert source_dir.exists()
    assert any(source_dir.rglob("*- original.md"))