"""Generador de notas Markdown para Obsidian (diseño mejorado)."""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import yaml

from app.database import repository as repo
from app.utils.logging import get_logger
from app.utils.text import safe_filename

logger = get_logger("processor")

# Carpetas de categoría por defecto (config/categories.yaml las puede sobrescribir)
DEFAULT_FOLDERS = {
    "AI": "02 - Updates/AI",
    "Developer Tools": "02 - Updates/Developer Tools",
    "Open Source": "02 - Updates/Open Source",
    "Cloud": "02 - Updates/Cloud",
    "Cybersecurity": "02 - Updates/Cybersecurity",
    "Hardware": "02 - Updates/Hardware",
    "Productivity": "02 - Updates/Productivity",
    "General Tech": "02 - Updates/General Tech",
}

# Secciones del tipo de nota -> carpeta del Vault
TYPE_FOLDERS = {
    "update": "02 - Updates",
    "tool": "04 - Tools",
    "company": "03 - Companies",
    "model": "06 - Models",
    "alternative": "05 - Alternatives",
    "research": "09 - Research",
    "pricing": "07 - Pricing",
    "trend": "10 - Radar",
    "github": "08 - Open Source",
}

IMPORTANCE_BADGES = {
    "high": "🟢 Alta",
    "medium": "🟡 Media",
    "low": "⚪ Baja",
}

IMPACT_BADGES = {
    "high": "🚀 Alto",
    "medium": "🌐 Medio",
    "low": "🌱 Bajo",
}

PRICING_BADGES = {
    "free": "💰 Gratis",
    "open-source": "🧡 Open source",
    "freemium": "🧪 Freemium",
    "free-tier": "💧 Free tier",
    "paid": "💳 De pago",
    "enterprise": "🏢 Enterprise",
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _badge(key: str, mapping: dict, default: str = "") -> str:
    return mapping.get(key, default or key)


def _parse_json(value, default):
    try:
        return json.loads(value) if value else default
    except (json.JSONDecodeError, TypeError):
        return default


def build_frontmatter(article: dict, result: dict, category_folder: str) -> dict:
    """Construye el frontmatter YAML de la nota."""
    classification = result.get("classification") or {}
    metadata = result.get("metadata") or {}
    alternatives = classification.get("alternatives") or []
    extracted = classification.get("extracted") or metadata

    today = (article.get("published_at") or _utc_now())[:10]
    title = article.get("title", "")
    company = classification.get("company") or ""

    fm = {
        "type": "update",
        "id": article.get("ti_id"),
        "title": title,
        "aliases": [title],
        "original_title": article.get("title", ""),
        "company": company,
        "product": classification.get("product") or "",
        "version": extracted.get("version") or "",
        "date": today,
        "created": article.get("published_at") or _utc_now(),
        "updated": _utc_now(),
        "original_language": result.get("language") or "unknown",
        "translated": bool(result.get("translated", False)),
        "importance": classification.get("importance") or "medium",
        "impact": classification.get("impact") or "medium",
        "pricing": classification.get("pricing") or "unknown",
        "license": classification.get("license") or "unknown",
        "open_source": bool(classification.get("open_source", False)),
        "self_hosted": bool(classification.get("self_hosted", False)),
        "source": article.get("source_name", ""),
        "source_url": article.get("url") or "",
        "source_type": article.get("source_type", ""),
        "processed_by": "ollama" if result.get("backend", "ollama") == "ollama" else "openrouter",
        "backend": result.get("backend", "ollama"),
        "model": result.get("model") or "",
        "insights": bool((result.get("insights") or {}).get("profiles")),
        "status": "published",
        "category": classification.get("category") or "General Tech",
        "subcategory": classification.get("subcategory") or "",
        "confidence": classification.get("confidence") or "medium",
        "example": bool(article.get("example", False)),
        "tags": classification.get("tags") or [],
        "alternatives": [{"name": a["name"], "confidence": a.get("confidence", "medium")} for a in alternatives],
        "cssclasses": ["ti-note"],
    }
    return fm


def _render_yaml(data: dict) -> str:
    return yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False).strip()


def _meta_table(article: dict, result: dict) -> str:
    """Tabla de metadatos clave para la cabecera de la nota."""
    classification = result.get("classification") or {}
    extracted = classification.get("extracted") or result.get("metadata") or {}

    rows = []
    if classification.get("company"):
        rows.append(("Empresa", f"**{classification['company']}**"))
    if classification.get("product"):
        rows.append(("Producto", f"**{classification['product']}**"))
    if extracted.get("version"):
        rows.append(("Versión", extracted["version"]))
    if extracted.get("release_date"):
        rows.append(("Fecha de lanzamiento", extracted["release_date"]))
    if extracted.get("requirements"):
        rows.append(("Requisitos", extracted["requirements"]))
    if extracted.get("breaking_changes"):
        rows.append(("Cambios incompatibles", extracted["breaking_changes"]))
    if classification.get("license") and classification["license"] != "unknown":
        rows.append(("Licencia", classification["license"]))
    if classification.get("pricing") and classification["pricing"] != "unknown":
        rows.append(("Precio", _badge(classification["pricing"], PRICING_BADGES)))
    if classification.get("open_source"):
        rows.append(("Open source", "✅ Sí"))
    if classification.get("self_hosted"):
        rows.append(("Self-hosted", "✅ Sí"))
    if classification.get("platforms"):
        rows.append(("Plataformas", ", ".join(classification["platforms"])))

    if not rows:
        return ""

    lines = ["| Campo | Valor |", "| --- | --- |"]
    lines.extend(f"| {k} | {v} |" for k, v in rows)
    return "\n".join(lines)


def _badges_line(article: dict, result: dict) -> str:
    """Línea de badges de importancia/impacto/pricing."""
    classification = result.get("classification") or {}
    imp = _badge(classification.get("importance", "medium"), IMPORTANCE_BADGES)
    impa = _badge(classification.get("impact", "medium"), IMPACT_BADGES)
    pricing = classification.get("pricing") or "unknown"
    parts = [f"`{imp}`", f"`{impa}`"]
    if pricing != "unknown":
        parts.append(f"`{_badge(pricing, PRICING_BADGES)}`")
    if classification.get("confidence"):
        parts.append(f"`confianza: {classification['confidence']}`")
    return " · ".join(parts)


def _insights_section(result: dict) -> str:
    """Sección 'Informe para desarrolladores' a partir del módulo insights."""
    insights = result.get("insights") or {}
    what_is = (insights.get("what_is") or "").strip()
    why_dev = (insights.get("why_development") or "").strip()
    profiles = insights.get("profiles") or []
    if not (what_is or why_dev or profiles):
        return ""

    lines = ["## 📊 Informe para desarrolladores", ""]

    if what_is:
        lines.append("> [!info] ¿Qué es?")
        lines.append(">")
        for para in what_is.splitlines():
            lines.append(f"> {para}")
        lines.append("")

    if why_dev:
        lines.append("> [!tip] ¿En qué ayuda al desarrollo?")
        lines.append(">")
        for para in why_dev.splitlines():
            lines.append(f"> {para}")
        lines.append("")

    if profiles:
        lines.append("### Relevancia por perfil")
        lines.append("")
        lines.append("| Perfil | Relevancia | Debes saber / actualizarte |")
        lines.append("| --- | --- | --- |")
        for p in profiles:
            role = p.get("role", "")
            relevance = p.get("relevance", "")
            must_know = " · ".join(p.get("must_know") or []) or "—"
            lines.append(f"| {role} | {relevance} | {must_know} |")
        lines.append("")

    return "\n".join(lines)


def build_body(article: dict, result: dict) -> str:
    """Cuerpo Markdown de la nota según el template definido."""
    classification = result.get("classification") or {}
    metadata = result.get("metadata") or {}
    extracted = classification.get("extracted") or metadata
    alternatives = classification.get("alternatives") or []

    translation = result.get("translation") or ""
    summary = result.get("summary") or ""
    original = article.get("content") or ""

    lines: list[str] = []
    lines.append(f"# {article.get('title', '')}")
    lines.append("")

    # Badges bajo el título
    badges = _badges_line(article, result)
    if badges:
        lines.append(badges)
        lines.append("")

    # Tabla de metadatos
    meta_table = _meta_table(article, result)
    if meta_table:
        lines.append(meta_table)
        lines.append("")

    # Resumen en callout
    lines.append("> [!abstract] Resumen")
    lines.append(">")
    for para in (summary or "_Sin resumen disponible._").splitlines():
        lines.append(f"> {para}")
    lines.append("")

    if translation:
        lines.append("## ¿Qué ocurrió?")
        lines.append("")
        lines.append("> [!info] Traducción del anuncio")
        lines.append(">")
        for para in translation.splitlines():
            lines.append(f"> {para}")
        lines.append("")

    reasons = classification.get("reasons") or []
    if reasons:
        lines.append("## ¿Por qué importa?")
        lines.append("")
        lines.append("> [!success] Impacto")
        lines.append(">")
        for r in reasons:
            lines.append(f"> - {r}")
        lines.append("")

    insights_section = _insights_section(result)
    if insights_section:
        lines.append(insights_section)
        lines.append("")

    tech_parts = []
    if extracted.get("version"):
        tech_parts.append(f"- **Versión:** {extracted['version']}")
    if extracted.get("release_date"):
        tech_parts.append(f"- **Fecha de lanzamiento:** {extracted['release_date']}")
    if extracted.get("requirements"):
        tech_parts.append(f"- **Requisitos:** {extracted['requirements']}")
    if extracted.get("breaking_changes"):
        tech_parts.append(f"- **Cambios incompatibles:** {extracted['breaking_changes']}")
    if classification.get("license") and classification["license"] != "unknown":
        tech_parts.append(f"- **Licencia:** {classification['license']}")
    if classification.get("open_source"):
        tech_parts.append("- **Open source:** sí")
    if classification.get("self_hosted"):
        tech_parts.append("- **Self-hosted:** sí")
    if tech_parts:
        lines.append("## Información técnica")
        lines.append("")
        lines.extend(tech_parts)
        lines.append("")

    lines.append("## Precio")
    lines.append("")
    pricing = classification.get("pricing") or "unknown"
    price_detail = extracted.get("price") or ""
    if pricing == "unknown" and not price_detail:
        lines.append("_No se ha detectado información de precios en la fuente._")
    else:
        lines.append(f"> [!money] {_badge(pricing, PRICING_BADGES)}")
        if price_detail:
            lines.append(">")
            lines.append(f"> {price_detail}")
    lines.append("")

    if alternatives:
        lines.append("## Alternativas")
        lines.append("")
        for a in alternatives:
            conf = a.get("confidence", "medium")
            name = a.get("name", "")
            if a.get("url"):
                lines.append(f"- **[{name}]({a['url']})** — confianza: {conf}")
            else:
                lines.append(f"- **{name}** — confianza: {conf}")
        lines.append("")

    lines.append("## Fuente original")
    lines.append("")
    if article.get("url"):
        lines.append(f"[{article.get('url', '')}]({article['url']})")
    else:
        lines.append(f"_Fuente: {article.get('source_name', '')}_")
    lines.append("")

    if translation and original:
        lines.append("## Contenido original")
        lines.append("")
        lines.append("<details>")
        lines.append("<summary>Ver contenido original (no traducido)</summary>")
        lines.append("")
        lines.append(original)
        lines.append("")
        lines.append("</details>")
        lines.append("")

    return "\n".join(lines)


class NoteGenerator:
    """Genera notas Markdown dentro del Vault de Obsidian."""

    def __init__(self, conn: sqlite3.Connection, settings, categories: dict | None = None):
        self.conn = conn
        self.settings = settings
        self.vault = Path(settings.vault_path)
        self.categories = categories or {}

    # ------------------------------------------------------------------

    def _category_folder(self, category: str) -> str:
        if category in self.categories:
            return self.categories[category].get("folder", DEFAULT_FOLDERS.get(category, "02 - Updates/General Tech"))
        return DEFAULT_FOLDERS.get(category, "02 - Updates/General Tech")

    def generate(self, article_id: int, result: dict) -> Path | None:
        """Genera (o regenera) la nota de un artículo procesado."""
        article = repo.get_processed_article(self.conn, article_id)
        if not article:
            logger.warning("Artículo %s no encontrado para generar nota", article_id)
            return None

        classification = result.get("classification") or {}
        category = classification.get("category") or "General Tech"
        importance = classification.get("importance") or "medium"

        # Ruta: importancia baja -> Inbox/Review
        if importance == "low":
            folder = "01 - Inbox/Review"
        else:
            folder = self._category_folder(category)

        ti_id = article.get("ti_id") or f"ti-{article_id:06d}"
        filename = f"{ti_id} - {safe_filename(article.get('title', 'sin-titulo'))}.md"
        target_dir = self.vault / folder
        target_dir.mkdir(parents=True, exist_ok=True)
        note_path = target_dir / filename

        # Contenido largo -> Inbox/Sources con enlace
        long_content_note = None
        if article.get("content") and len(article["content"]) > self.settings.long_content_chars:
            long_content_note = self._write_long_content(article, ti_id)

        fm = build_frontmatter(article, result, folder)
        body = build_body(article, result)

        if long_content_note:
            rel = long_content_note.relative_to(self.vault).as_posix()
            rel_name = rel.rsplit("/", 1)[-1].replace(".md", "")
            body += f"\n## Contenido original completo\n\n[[{rel_name}|📄 Contenido original completo]]\n"

        content = f"---\n{_render_yaml(fm)}\n---\n\n{body}\n"
        note_path.write_text(content, encoding="utf-8")
        logger.info("Nota generada: %s", note_path.relative_to(self.vault))
        return note_path

    def _write_long_content(self, article: dict, ti_id: str) -> Path | None:
        """Guarda el contenido original completo en 01 - Inbox/Sources/."""
        source_slug = safe_filename(article.get("source_name") or article.get("source_id") or "source", 40)
        src_dir = self.vault / "01 - Inbox" / "Sources" / source_slug
        src_dir.mkdir(parents=True, exist_ok=True)
        path = src_dir / f"{ti_id} - original.md"
        path.write_text(
            f"---\ntype: source-original\nid: {ti_id}\nsource: {article.get('source_name', '')}\nurl: {article.get('url') or ''}\n---\n\n# {article.get('title', '')}\n\n{article.get('content') or ''}\n",
            encoding="utf-8",
        )
        return path