"""CLI de Tech Intelligence (argparse, sin dependencias extra)."""
from __future__ import annotations

import argparse
import sys

from app.orchestrator import bootstrap, sync


def _print_report(report) -> None:
    c = report.collect
    print("\n=== Sync completado ===")
    print(f"Fuentes consultadas : {c.sources_checked}")
    print(f"Artículos obtenidos: {c.fetched}")
    print(f"Nuevos             : {c.new}")
    print(f"Duplicados         : {c.duplicates}")
    print(f"Actualizados       : {c.updated}")
    if c.errors:
        print(f"Errores de fuente  : {len(c.errors)}")
        for src, err in c.errors[:5]:
            print(f"  - {src}: {err[:100]}")
    if report.process:
        print(f"\nProcesados         : {report.process.processed}")
        print(f"Fallidos           : {report.process.failed}")
        print(f"Pendientes         : {report.process.pending}")
    if report.committed:
        print("\nGit: commit creado.")
    else:
        print("\nGit: sin cambios (no se creó commit).")


def cmd_sync(args) -> int:
    report = sync(only_sources=args.sources, skip_process=args.collect_only, skip_git=args.no_git)
    _print_report(report)
    return 0


def cmd_collect(args) -> int:
    report = sync(only_sources=args.sources, skip_process=True)
    _print_report(report)
    return 0


def cmd_process(args) -> int:
    from app.database import repository as repo
    from app.processor.processor import Processor

    settings, conn = bootstrap()
    processor = Processor(conn, settings)

    if args.id:
        article = repo.get_article_by_ti_id(conn, args.id)
        if not article:
            print(f"Artículo {args.id} no encontrado.")
            return 1
        ok = processor.process(article["id"])
        print(f"Artículo {args.id}: {'OK' if ok else 'pendiente/falló (revisar logs)'}")
        return 0 if ok else 1

    result = processor.process_pending(failed=args.failed, all_articles=args.all)
    print(f"Procesados: {result.processed} | Fallidos: {result.failed} | Pendientes: {result.pending}")
    return 0


def cmd_export(args) -> int:
    from app.exporters.jsonl import export_jsonl

    settings, conn = bootstrap()
    files = export_jsonl(conn, settings)
    for name, path in files.items():
        print(f"{name}: {path}")
    conn.close()
    return 0


def cmd_health(args) -> int:
    from app.health.health import run_health

    settings, conn = bootstrap()
    report = run_health(conn, settings)
    print(report.render())
    print(f"\nResultado: {'TODO OK' if report.ok else 'HAY FALLOS'}")
    conn.close()
    return 0 if report.ok else 1


def cmd_sources(args) -> int:
    from app.sources.loader import load_sources

    settings, conn = bootstrap()
    sources = load_sources(settings.sources_path)
    print(f"{'ID':<22}{'TIPO':<10}{'ENABLED':<9}{'CATEGORÍA':<20}PRIORIDAD")
    print("-" * 80)
    for s in sources:
        if args.enabled_only and not s.enabled:
            continue
        print(f"{s.id:<22}{s.type:<10}{str(s.enabled):<9}{s.category:<20}{s.priority}")
    conn.close()
    return 0


def cmd_retry(args) -> int:
    from app.database import repository as repo
    from app.processor.processor import Processor

    settings, conn = bootstrap()
    processor = Processor(conn, settings)
    failed = repo.list_articles(conn, status=repo.STATUS_FAILED, limit=args.limit)
    ok = failed_final = 0
    for a in failed:
        repo.set_article_status(conn, a["id"], repo.STATUS_PENDING)
        good = processor.process(a["id"])
        if good:
            ok += 1
        else:
            failed_final += 1
    print(f"Reintentados: {len(failed)} | OK: {ok} | Siguen fallando: {failed_final}")
    conn.close()
    return 0


def cmd_stats(args) -> int:
    from app.database import repository as repo

    settings, conn = bootstrap()
    st = repo.stats(conn)
    print("=== Tech Intelligence — Estadísticas ===")
    for k, v in st.items():
        print(f"{k:<20}: {v}")
    conn.close()
    return 0


def cmd_scheduler(args) -> int:
    from app.scheduler.scheduler import Scheduler

    settings, conn = bootstrap()
    conn.close()
    sched = Scheduler(settings.sync_interval, run_sync=lambda: sync(settings),
                      lock_dir=settings.database_path.parent)
    sched.run_forever()
    return 0


def cmd_seed(args) -> int:
    from app.seed import seed

    settings, conn = bootstrap()
    n = seed(settings, conn)
    print(f"Datos de ejemplo insertados: {n}")
    conn.close()
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="tech-intelligence",
        description="Sistema local-first de inteligencia tecnológica (RSS/GitHub -> Ollama -> Obsidian).",
    )
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("sync", help="Pipeline completo: collect + process + export + git")
    s.add_argument("--sources", nargs="*", help="Solo estas fuentes (IDs)")
    s.add_argument("--collect-only", action="store_true", help="Solo recopilar")
    s.add_argument("--no-git", action="store_true", help="No commitear")
    s.set_defaults(func=cmd_sync)

    s = sub.add_parser("collect", help="Solo recopilar")
    s.add_argument("--sources", nargs="*")
    s.set_defaults(func=cmd_collect)

    s = sub.add_parser("process", help="Procesar pendientes con Ollama")
    s.add_argument("--id", help="Procesar un artículo por ID (ti-2026-000001)")
    s.add_argument("--failed", action="store_true", help="Reintentar fallidos")
    s.add_argument("--all", dest="all", action="store_true", help="Re-procesar todo")
    s.set_defaults(func=cmd_process)

    s = sub.add_parser("export", help="Generar JSONL en el Vault")
    s.set_defaults(func=cmd_export)

    s = sub.add_parser("health", help="Comprobar servicios")
    s.set_defaults(func=cmd_health)

    s = sub.add_parser("sources", help="Listar fuentes")
    s.add_argument("--enabled-only", action="store_true")
    s.set_defaults(func=cmd_sources)

    s = sub.add_parser("retry", help="Reintentar artículos fallidos")
    s.add_argument("--limit", type=int, default=50)
    s.set_defaults(func=cmd_retry)

    s = sub.add_parser("stats", help="Estadísticas")
    s.set_defaults(func=cmd_stats)

    s = sub.add_parser("scheduler", help="Ejecución automática en bucle")
    s.set_defaults(func=cmd_scheduler)

    s = sub.add_parser("seed", help="Insertar datos de ejemplo")
    s.set_defaults(func=cmd_seed)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print("\nInterrumpido.")
        return 130


if __name__ == "__main__":
    sys.exit(main())