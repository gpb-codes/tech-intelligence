"""Generador del Dashboard Home.md (Dataview + fallback sin plugins)."""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from app.database import repository as repo
from app.utils.logging import get_logger

logger = get_logger("processor")


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _parse_classification(classification: str | None) -> dict:
    try:
        return json.loads(classification or "{}")
    except json.JSONDecodeError:
        return {}


def _entry_link(a: dict) -> str:
    title = (a.get("title") or "").replace("|", "/")
    return f"- {title} _(fuente: {a.get('source_name') or '?'})_"


def _counts(conn: sqlite3.Connection) -> dict:
    total = conn.execute("SELECT COUNT(*) FROM articles").fetchone()[0]
    processed = conn.execute("SELECT COUNT(*) FROM articles WHERE status = 'processed'").fetchone()[0]
    pending = conn.execute("SELECT COUNT(*) FROM articles WHERE status IN ('new', 'pending')").fetchone()[0]
    failed = conn.execute("SELECT COUNT(*) FROM articles WHERE status = 'failed'").fetchone()[0]
    sources = conn.execute("SELECT COUNT(*) FROM sources WHERE enabled = 1").fetchone()[0]
    return {"total": total, "processed": processed, "pending": pending, "failed": failed, "sources": sources}


def generate_dashboard(conn: sqlite3.Connection, settings) -> Path:
    """Regenera 00 - Dashboard/Home.md con Dataview y listas estáticas."""
    articles = repo.articles_with_results(conn, limit=400)

    processed = [a for a in articles if a["status"] == "processed" and not a["example"]]

    recent = processed[:15]
    by_cat: dict[str, list] = {}
    for a in processed:
        cls = _parse_classification(a.get("classification"))
        cat = cls.get("category") or "General Tech"
        by_cat.setdefault(cat, []).append(a)

    pricing = [a for a in processed if _parse_classification(a.get("classification")).get("pricing") in
               ("paid", "freemium", "free-tier", "enterprise")]
    models = [a for a in processed if (_parse_classification(a.get("classification")).get("category") == "AI"
                                       and _parse_classification(a.get("classification")).get("product"))]
    alternatives = [a for a in processed if _parse_classification(a.get("classification")).get("alternatives")]
    github = [a for a in processed if a.get("source_type") == "github"]
    research = [a for a in processed if _parse_classification(a.get("classification")).get("subcategory", "").lower()
                in ("research", "paper", "investigación")]

    counts = _counts(conn)

    lines = [
        "---",
        "type: dashboard",
        "title: Tech Intelligence",
        "aliases: [Inicio, Dashboard]",
        "cssclasses: [ti-dashboard]",
        "---",
        "",
        "# 🛰️ Tech Intelligence",
        "",
        f"_Actualizado: {_now()} · Sistema local-first · Procesado con Ollama_",
        "",
        "> [!info] Estado del sistema",
        f"> - **{counts['total']}** artículos en la base · **{counts['processed']}** procesados · "
        f"**{counts['pending']}** pendientes · **{counts['failed']}** fallidos",
        f"> - **{counts['sources']}** fuentes activas · Vault versionado en Git",
        "",
        "## 🔥 Últimas actualizaciones",
        "",
        "```dataview",
        'TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", '
        'company AS "Empresa", product AS "Producto" FROM "02 - Updates" '
        'WHERE status = "published" AND example = false SORT date DESC LIMIT 20',
        "```",
        "",
    ]
    if recent:
        lines.append("_(fallback sin Dataview: últimas 15)_")
        lines.append("")
        lines.extend(_entry_link(a) for a in recent)
    lines.append("")

    sections = [
        ("IA", by_cat.get("AI", [])),
        ("Developer Tools", by_cat.get("Developer Tools", [])),
        ("Open Source", by_cat.get("Open Source", [])),
        ("Cloud", by_cat.get("Cloud", [])),
        ("Cybersecurity", by_cat.get("Cybersecurity", [])),
        ("Hardware", by_cat.get("Hardware", [])),
        ("Productivity", by_cat.get("Productivity", [])),
        ("General Tech", by_cat.get("General Tech", [])),
    ]

    for title, items in sections:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("```dataview")
        lines.append(f'TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/{title}" WHERE contains(category, "{title}") AND example = false SORT date DESC LIMIT 10')
        lines.append("```")
        lines.append("")
        if items:
            lines.append(f"_(fallback: últimas {min(5, len(items))})_")
            lines.append("")
            lines.extend(_entry_link(a) for a in items[:5])
        lines.append("")

    lines.append("## 💸 Cambios de precio")
    lines.append("")
    lines.append('```dataview\nTABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", product AS "Producto", pricing AS "Precio" FROM "02 - Updates" WHERE pricing != "unknown" AND pricing != "open-source" AND example = false SORT date DESC LIMIT 15\n```')
    lines.append("")
    if pricing:
        lines.append(f"_(fallback: {min(5, len(pricing))} recientes)_")
        lines.append("")
        lines.extend(_entry_link(a) for a in pricing[:5])
    lines.append("")

    lines.append("## 🧠 Nuevos modelos")
    lines.append("")
    if models:
        lines.extend(_entry_link(a) for a in models[:10])
    else:
        lines.append("_Sin modelos detectados aún._")
    lines.append("")

    lines.append("## 🔁 Alternativas gratuitas / open source")
    lines.append("")
    if alternatives:
        lines.extend(_entry_link(a) for a in alternatives[:10])
    else:
        lines.append("_Sin alternativas detectadas aún._")
    lines.append("")

    lines.append("## 🐙 GitHub")
    lines.append("")
    if github:
        lines.extend(_entry_link(a) for a in github[:10])
    else:
        lines.append("_Sin actividad de GitHub aún._")
    lines.append("")

    lines.append("## 🔬 Tendencias / Investigación")
    lines.append("")
    if research:
        lines.extend(_entry_link(a) for a in research[:10])
    else:
        lines.append("_Sin investigaciones detectadas aún._")
    lines.append("")

    lines.append("## 🛰️ Tech Radar")
    lines.append("")
    lines.append("```dataview")
    lines.append('TABLE ring AS "Anillo", category AS "Categoría", file.link AS "Nota" FROM "10 - Radar" WHERE type = "trend" SORT ring ASC, date DESC')
    lines.append("```")
    lines.append("")
    lines.append("Anillos: 🟢 **ADOPT** · 🔵 **TRIAL** · 🟡 **ASSESS** · 🔴 **HOLD**  ")
    lines.append("_El Radar se actualiza manualmente en `10 - Radar/`._")
    lines.append("")

    lines.append("## 📊 Estadísticas")
    lines.append("")
    lines.append("```dataview")
    lines.append('TABLE length(rows) AS "Notas" FROM "02 - Updates" GROUP BY category SORT length(rows) DESC')
    lines.append("```")
    lines.append("")

    lines.append("## 🗂️ Navegación")
    lines.append("")
    lines.append("- 📁 `01 - Inbox/` — pendientes de revisión, fallidos y contenido largo")
    lines.append("- 📰 `02 - Updates/` — noticias procesadas por categoría")
    lines.append("- 🏢 `03 - Companies/` — perfiles de empresas")
    lines.append("- 🛠️ `04 - Tools/` — herramientas")
    lines.append("- 🔁 `05 - Alternatives/` — alternativas open source")
    lines.append("- 🧠 `06 - Models/` — modelos de IA")
    lines.append("- 💸 `07 - Pricing/` — cambios de precios")
    lines.append("- 🐙 `08 - Open Source/` — proyectos de GitHub")
    lines.append("- 🔬 `09 - Research/` — investigación y papers")
    lines.append("- 🛰️ `10 - Radar/` — Tech Radar")
    lines.append("- 📡 `11 - Sources/` — fuentes configuradas")
    lines.append("- 🧩 `12 - Templates/` — plantillas de notas")
    lines.append("- 💾 `13 - Dataset/` — exportaciones JSONL")
    lines.append("")

    dash_dir = settings.vault_path / "00 - Dashboard"
    dash_dir.mkdir(parents=True, exist_ok=True)
    path = dash_dir / "Home.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("Dashboard regenerado: %s", path)
    return path