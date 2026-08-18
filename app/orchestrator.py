"""Orquestación: pipeline completo (collect -> process -> export -> git)."""
from __future__ import annotations

import sqlite3
from pathlib import Path

from app.collector.pipeline import CollectResult, collect
from app.database import repository as repo
from app.database.connection import get_connection
from app.database.schema import init_db
from app.exporters.jsonl import export_jsonl
from app.generator.dashboard import generate_dashboard
from app.generator.markdown import NoteGenerator
from app.gitutils import git as git_utils
from app.processor.processor import ProcessResult, Processor
from app.sources.loader import load_categories, load_sources
from app.utils.config import Settings, load_settings
from app.utils.logging import get_logger, setup_logging

logger = get_logger("collector")


class SyncReport:
    def __init__(self):
        self.collect: CollectResult | None = None
        self.process: ProcessResult | None = None
        self.exported: dict[str, Path] = {}
        self.committed: bool = False
        self.dashboard: Path | None = None


def bootstrap(settings: Settings | None = None) -> tuple[Settings, sqlite3.Connection]:
    """Configura logging, carga ajustes y abre la base de datos."""
    settings = settings or load_settings()
    setup_logging(settings.log_dir, settings.log_level)
    Path(settings.vault_path).mkdir(parents=True, exist_ok=True)
    conn = get_connection(settings.database_path)
    init_db(conn)
    return settings, conn


def sync(settings: Settings | None = None, only_sources: list[str] | None = None,
         skip_process: bool = False, skip_git: bool = False) -> SyncReport:
    """Pipeline completo: collect -> process -> export -> git."""
    settings, conn = bootstrap(settings)
    report = SyncReport()

    # Sincronizar fuentes configuradas con la DB
    try:
        sources = load_sources(settings.sources_path)
    except Exception as e:
        logger.error("No se pudieron cargar las fuentes: %s", e)
        sources = []
    for s in sources:
        repo.upsert_source(conn, s.as_dict())

    # 1. Collect
    enabled = [s for s in sources if s.enabled]
    report.collect = collect(conn, enabled, settings, only=only_sources)
    logger.info("Collect: %d nuevas, %d duplicados, %d actualizadas, %d errores",
                report.collect.new, report.collect.duplicates, report.collect.updated, len(report.collect.errors))

    # 2. Process
    if not skip_process:
        processor = Processor(conn, settings)
        report.process = processor.process_pending(workers=settings.processing_workers)
        logger.info("Process: %d OK", report.process.processed)

    # 3. Export JSONL + Dashboard
    report.exported = export_jsonl(conn, settings)
    report.dashboard = generate_dashboard(conn, settings)

    # 4. Git
    if settings.git_enabled and not skip_git:
        try:
            report.committed = git_utils.commit_after_sync(settings.vault_path, settings.git_commit_prefix)
        except Exception as e:
            logger.error("Git falló: %s", e)

    conn.close()
    return report