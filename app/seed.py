"""Datos de ejemplo claramente marcados como example: true.

Se ejecuta con: tech-intelligence seed
Estos registros demuestran el sistema sin inventar precios ni versiones actuales:
el contenido es descriptivo y genérico, sin datos falsos.
"""
from __future__ import annotations

import sqlite3

from app.collector.base import NormalizedArticle
from app.database import repository as repo
from app.generator.markdown import build_body, build_frontmatter, _render_yaml
from app.utils.config import Settings

EXAMPLES = [
    {
        "source_id": "openai-blog",
        "source_name": "OpenAI Blog",
        "source_type": "rss",
        "title": "Ejemplo: OpenAI publica actualizaciones de su plataforma de IA",
        "url": "https://openai.com/news",
        "external_id": "example-openai-1",
        "content": ("OpenAI publica periódicamente actualizaciones de sus modelos y de su API en su blog oficial. "
                    "La plataforma ofrece modelos de lenguaje para tareas de generación de texto, razonamiento y agentes. "
                    "Las noticias del blog anuncian mejoras de producto, nuevas capacidades y cambios en la disponibilidad de los servicios."),
        "published_at": "2026-08-10T10:00:00Z",
        "classification": {
            "company": "OpenAI", "product": "ChatGPT",
            "category": "AI", "subcategory": "modelos",
            "pricing": "unknown", "license": "unknown",
            "open_source": False, "self_hosted": False,
            "tags": ["openai", "llm", "api"],
            "importance": "medium", "impact": "medium",
            "confidence": "high",
            "extracted": {"version": "", "release_date": "", "price": "", "urls": ["https://openai.com/news"]},
        },
    },
    {
        "source_id": "gh-opencode",
        "source_name": "OpenCode (GitHub)",
        "source_type": "github",
        "title": "Ejemplo: OpenCode, agente de código en terminal open source",
        "url": "https://github.com/sst/opencode",
        "external_id": "example-opencode-1",
        "content": ("OpenCode es un agente de programación para terminal, open source, distribuido en GitHub. "
                    "Permite usar distintos modelos locales y remotos para escribir y modificar código desde la línea de comandos."),
        "published_at": "2026-08-12T10:00:00Z",
        "classification": {
            "company": "SST", "product": "OpenCode",
            "category": "Developer Tools", "subcategory": "ai coding",
            "pricing": "open-source", "license": "Apache-2.0",
            "open_source": True, "self_hosted": True,
            "tags": ["cli", "ai", "open-source", "coding-agent"],
            "importance": "high", "impact": "medium",
            "confidence": "high",
            "extracted": {"version": "", "release_date": "", "price": "", "urls": ["https://github.com/sst/opencode"]},
        },
    },
    {
        "source_id": "gh-ollama",
        "source_name": "Ollama (GitHub)",
        "source_type": "github",
        "title": "Ejemplo: Ollama publica releases en su repositorio oficial",
        "url": "https://github.com/ollama/ollama",
        "external_id": "example-ollama-1",
        "content": ("Ollama es la herramienta de código abierto para ejecutar modelos de lenguaje localmente. "
                    "Su repositorio en GitHub publica releases con nuevas funcionalidades, soporte de modelos y correcciones."),
        "published_at": "2026-08-11T10:00:00Z",
        "classification": {
            "company": "Ollama", "product": "Ollama",
            "category": "AI", "subcategory": "local-llm",
            "pricing": "open-source", "license": "MIT",
            "open_source": True, "self_hosted": True,
            "tags": ["llm", "local", "inference", "open-source"],
            "importance": "medium", "impact": "medium",
            "confidence": "high",
            "extracted": {"version": "", "release_date": "", "price": "", "urls": ["https://github.com/ollama/ollama"]},
        },
    },
    {
        "source_id": "devto",
        "source_name": "DEV Community",
        "source_type": "rss",
        "title": "Ejemplo: comparativas de agentes de programación con IA",
        "url": "https://dev.to",
        "external_id": "example-devto-1",
        "content": ("La comunidad de desarrollo publica análisis comparativos de herramientas de programación asistida por IA, "
                    "como asistentes en el editor y agentes de terminal. Estas comparativas suelen cubrir coste, "
                    "open source y facilidad de uso, sin datos oficiales de precios."),
        "published_at": "2026-08-14T10:00:00Z",
        "classification": {
            "company": "", "product": "",
            "category": "Developer Tools", "subcategory": "comparativas",
            "pricing": "unknown", "license": "unknown",
            "open_source": False, "self_hosted": False,
            "tags": ["comparativa", "ai-coding", "community"],
            "importance": "low", "impact": "low",
            "confidence": "medium",
            "extracted": {"version": "", "release_date": "", "price": "", "urls": []},
        },
    },
]


def seed(settings: Settings, conn: sqlite3.Connection) -> int:
    """Inserta ejemplos (si no existen) y genera sus notas Markdown."""
    count = 0
    for ex in EXAMPLES:
        article = NormalizedArticle(
            source_id=ex["source_id"],
            source_name=ex["source_name"],
            source_type=ex["source_type"],
            title=ex["title"],
            url=ex["url"],
            external_id=ex["external_id"],
            content=ex["content"],
            published_at=ex["published_at"],
            example=True,
        )
        data = article.to_dict()
        dup = repo.find_duplicate(conn, data)
        if dup:
            continue
        row = repo.insert_article(conn, data)
        result = {
            "model": "example",
            "language": "en",
            "translated": True,
            "translation": ex["content"],
            "summary": f"- {ex['title']}.",
            "classification": ex["classification"],
            "metadata": ex["classification"].get("extracted", {}),
        }
        repo.save_result(conn, row["id"], result)

        # Nota Markdown en la carpeta de su categoría
        from app.generator.markdown import DEFAULT_FOLDERS
        from app.utils.text import safe_filename

        cat = ex["classification"].get("category", "General Tech")
        folder = DEFAULT_FOLDERS.get(cat, "02 - Updates/General Tech")
        ti_id = row["ti_id"]
        filename = f"{ti_id} - {safe_filename(row['title'])}.md"
        target = settings.vault_path / folder
        target.mkdir(parents=True, exist_ok=True)
        article_row = repo.get_processed_article(conn, row["id"])
        fm = build_frontmatter(article_row, result, folder)
        fm["example"] = True
        body = build_body(article_row, result)
        (target / filename).write_text(
            f"---\n{_render_yaml(fm)}\n---\n\n{body}\n", encoding="utf-8"
        )
        count += 1
    return count