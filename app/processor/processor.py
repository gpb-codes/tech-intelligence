"""Procesador: ejecuta el pipeline de Ollama sobre artículos pendientes."""
from __future__ import annotations

import sqlite3
from pathlib import Path

from app.database import repository as repo
from app.generator.markdown import NoteGenerator
from app.ollama.client import OllamaClient, OllamaError, OpenRouterClient
from app.ollama.language import LanguageDetector, needs_translation
from app.ollama.modules import (
    AlternativeDetector,
    Classifier,
    ImportanceAnalyzer,
    InsightsGenerator,
    MetadataExtractor,
    Summarizer,
    Translator,
)
from app.utils.logging import get_logger, get_error_logger

logger = get_logger("processor")
err_log = get_error_logger()


class ProcessResult:
    def __init__(self):
        self.processed = 0
        self.failed = 0
        self.pending = 0
        self.skipped_no_content = 0


def build_client(settings):
    """Crea el cliente de IA según el backend configurado (ollama | openrouter)."""
    if settings.ai_backend == "openrouter":
        return OpenRouterClient(
            api_key=settings.openrouter_api_key,
            model=settings.openrouter_model,
            timeout=settings.openrouter_timeout,
            temperature=settings.ollama_temperature,
        )
    return OllamaClient(
        base_url=settings.ollama_base_url,
        model=settings.ollama_model,
        timeout=settings.ollama_timeout,
        temperature=settings.ollama_temperature,
    )


class Processor:
    """Orquesta la cadena: idioma -> traducción -> resumen -> clasificación -> extracción -> insights."""

    def __init__(self, conn: sqlite3.Connection, settings):
        self.conn = conn
        self.settings = settings
        self.client = build_client(settings)
        prompts_dir: Path = settings.prompts_dir
        self.detector = LanguageDetector()
        self.notes = NoteGenerator(self.conn, settings)
        self.set_client(self.client)

    def set_client(self, client) -> None:
        """Sustituye el cliente de IA y reconstruye los módulos (tests, cambio de modelo/backend)."""
        self.client = client
        self.translator = Translator(client, self.settings.prompts_dir)
        self.summarizer = Summarizer(client, self.settings.prompts_dir)
        self.classifier = Classifier(client, self.settings.prompts_dir)
        self.extractor = MetadataExtractor(client, self.settings.prompts_dir)
        self.importance = ImportanceAnalyzer(client, self.settings.prompts_dir)
        self.alternatives = AlternativeDetector(client, self.settings.prompts_dir)
        self.insights = InsightsGenerator(client, self.settings.prompts_dir)

    # ------------------------------------------------------------------

    def process(self, article_id: int) -> bool:
        """Procesa un artículo. Devuelve True si terminó OK (o se rindió tras N intentos)."""
        article = repo.get_article(self.conn, article_id)
        if not article:
            logger.warning("Artículo %s no existe", article_id)
            return False

        if not article["content"] or not article["content"].strip():
            repo.set_article_status(self.conn, article_id, repo.STATUS_IGNORED)
            logger.info("Artículo %s sin contenido -> ignorado", article_id)
            return True

        job_id = repo.create_job(self.conn, article_id)
        repo.job_started(self.conn, job_id)
        repo.set_article_status(self.conn, article_id, repo.STATUS_PROCESSING)
        attempts = self._attempts_for(article_id)

        if attempts >= self.settings.max_processing_attempts:
            logger.error("Artículo %s superó %d intentos -> failed", article_id, self.settings.max_processing_attempts)
            repo.set_article_status(self.conn, article_id, repo.STATUS_FAILED)
            repo.job_finished(self.conn, job_id, ok=False, error="max attempts")
            return True

        try:
            ok, status, error = self._run_pipeline(article, article_id)
        except OllamaError as e:
            # Ollama falló: guardar como pendiente para reintentar después
            logger.warning("Ollama falló para artículo %s: %s", article_id, e)
            err_log.error("Ollama en artículo %s: %s", article_id, e)
            repo.set_article_status(self.conn, article_id, repo.STATUS_PENDING)
            repo.job_finished(self.conn, job_id, ok=False, error=str(e)[:500])
            return False

        repo.job_finished(self.conn, job_id, ok=ok, error=error)
        if status:
            repo.set_article_status(self.conn, article_id, status)
        return ok

    # ------------------------------------------------------------------

    def _attempts_for(self, article_id: int) -> int:
        row = self.conn.execute(
            "SELECT COUNT(*) c FROM processing_jobs WHERE article_id = ?", (article_id,)
        ).fetchone()
        return row["c"]

    def _run_pipeline(self, article: dict, article_id: int) -> tuple[bool, str | None, str | None]:
        content = article["content"]
        title = article["title"]

        # 1. Idioma
        lang = self.detector.detect(content)
        repo.update_article(self.conn, article_id, {"language": lang})
        logger.info("Artículo %s: idioma=%s", article_id, lang)

        # 2. Traducción si no es español
        translated = False
        working_content = content
        if needs_translation(lang):
            logger.info("Artículo %s: traduciendo (%s -> es)", article_id, lang)
            working_content = self.translator.translate(f"{title}\n\n{content}")
            translated = True
            logger.info("Artículo %s: traducción OK (%d chars)", article_id, len(working_content))

        # 3. Resumen
        summary = self.summarizer.summarize(working_content)

        # 4. Clasificación
        classification = self.classifier.classify(working_content)

        # 5. Extracción de metadata
        metadata = self.extractor.extract(working_content)

        # 6. Importancia
        importance = self.importance.analyze(working_content)

        # 7. Alternativas
        alternatives = self.alternatives.detect(working_content)

        # 7.5. Informe profesional (qué es, ayuda al desarrollo, relevancia por rol)
        insights = {}
        try:
            insights = self.insights.generate(f"{title}\n\n{working_content}")
            logger.info("Artículo %s: insights OK (%d perfiles)", article_id, len(insights.get("profiles") or []))
        except OllamaError as e:
            logger.warning("Artículo %s: insights fallaron (%s) -> se omite la sección", article_id, e)
            err_log.error("Insights artículo %s: %s", article_id, e)

        result = {
            "model": self.settings.ollama_model if self.settings.ai_backend == "ollama" else self.settings.openrouter_model,
            "backend": self.settings.ai_backend,
            "language": lang,
            "translated": translated,
            "translation": working_content if translated else None,
            "summary": summary,
            "classification": {**classification, **importance,
                               "alternatives": alternatives, "extracted": metadata},
            "metadata": metadata,
            "insights": insights,
        }
        repo.save_result(self.conn, article_id, result)

        # 8. Generar nota Markdown
        try:
            self.notes.generate(article_id, result)
        except Exception as e:
            logger.exception("Falló la generación de la nota para artículo %s", article_id)
            err_log.error("Markdown artículo %s: %s", article_id, e)
            repo.set_article_status(self.conn, article_id, repo.STATUS_FAILED)
            return False, repo.STATUS_FAILED, f"markdown: {e}"

        return True, repo.STATUS_PROCESSED, None

    # ------------------------------------------------------------------

    def process_pending(self, only_ids: list[int] | None = None, failed: bool = False,
                        all_articles: bool = False) -> ProcessResult:
        """Procesa artículos pendientes (o fallidos, o todos)."""
        result = ProcessResult()

        if only_ids:
            articles = [repo.get_article(self.conn, a) for a in only_ids]
            articles = [a for a in articles if a]
        elif failed:
            articles = repo.list_articles(self.conn, status=repo.STATUS_FAILED, limit=1000)
        elif all_articles:
            articles = repo.list_articles(self.conn, status=repo.STATUS_PROCESSED, limit=1000) + \
                       repo.list_articles(self.conn, status=repo.STATUS_PENDING, limit=1000) + \
                       repo.list_articles(self.conn, status=repo.STATUS_NEW, limit=1000) + \
                       repo.list_articles(self.conn, status=repo.STATUS_FAILED, limit=1000)
        else:
            articles = repo.list_articles(self.conn, status=repo.STATUS_PENDING, limit=1000) + \
                       repo.list_articles(self.conn, status=repo.STATUS_NEW, limit=1000)

        for article in articles:
            ok = self.process(article["id"])
            if ok:
                result.processed += 1
            else:
                current = repo.get_article(self.conn, article["id"])
                if current and current["status"] == repo.STATUS_FAILED:
                    result.failed += 1
                else:
                    result.pending += 1

        logger.info("Procesamiento: %d OK, %d fallidos, %d pendientes",
                    result.processed, result.failed, result.pending)
        return result