"""Scheduler: ejecución automática con protección de concurrencia."""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

from app.utils.logging import get_logger

logger = get_logger("collector")

LOCK_DIR_NAME = "database"


class Scheduler:
    """Ejecuta el sync completo cada N minutos.

    Evita ejecuciones concurrentes con un lockfile (PID + staleness).
    """

    def __init__(self, interval_minutes: int, run_sync, lock_dir: Path | None = None):
        self.interval = max(1, int(interval_minutes)) * 60
        self.run_sync = run_sync
        self.lock_path = (lock_dir or Path("database")) / "scheduler.lock"

    # ------------------------------------------------------------------

    def acquire(self) -> bool:
        if self.lock_path.exists():
            try:
                pid = int(self.lock_path.read_text().strip())
                if _pid_alive(pid):
                    logger.warning("Otro proceso del scheduler está activo (pid %s). Saltando ciclo.", pid)
                    return False
            except (ValueError, OSError):
                pass
            # Lock obsoleto: se elimina
            self.lock_path.unlink(missing_ok=True)
        self.lock_path.write_text(str(os.getpid()))
        return True

    def release(self) -> None:
        self.lock_path.unlink(missing_ok=True)

    # ------------------------------------------------------------------

    def run_forever(self) -> None:
        logger.info("Scheduler iniciado (intervalo: %ds)", self.interval)
        first = True
        try:
            while True:
                if first:
                    first = False
                else:
                    time.sleep(self.interval)

                if not self.acquire():
                    continue
                try:
                    self.run_sync()
                except KeyboardInterrupt:
                    raise
                except Exception:
                    logger.exception("Ciclo de sync falló")
                finally:
                    self.release()
        except KeyboardInterrupt:
            logger.info("Scheduler detenido.")
            self.release()


def _pid_alive(pid: int) -> bool:
    if sys.platform == "win32":
        try:
            import ctypes

            PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
            handle = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
            if not handle:
                return False
            ctypes.windll.kernel32.CloseHandle(handle)
            return True
        except Exception:
            return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False