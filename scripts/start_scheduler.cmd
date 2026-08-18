@echo off
REM Tech Intelligence — scheduler automático (arranque de Windows)
REM Inicia el pipeline en bucle cada SYNC_INTERVAL minutos.
cd /d "%~dp0.."
"%~dp0..\venv\Scripts\python.exe" -m app.cli.main scheduler >> logs\scheduler_stdout.log 2>&1