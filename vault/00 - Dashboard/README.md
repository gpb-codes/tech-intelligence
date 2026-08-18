# Tech Intelligence

Sistema local-first de inteligencia tecnológica.

- Recopila: RSS, GitHub (releases/tags), APIs REST.
- Procesa: detección de idioma, traducción al español, resumen, clasificación,
  extracción de metadata, importancia y alternativas.
- Produce: notas Markdown en este Vault (Obsidian) + dataset JSONL.
- Estado: SQLite (`database/`).
- IA: solo Ollama local.

## Uso rápido

```bash
pip install -e ".[dev]"
cp .env.example .env        # ajustar OLLAMA_MODEL
tech-intelligence health    # comprobar servicios
tech-intelligence sync      # pipeline completo
tech-intelligence scheduler # ejecución automática cada N minutos
```

## Cómo abrir en Obsidian

Abrir Obsidian → "Open folder as vault" → seleccionar la carpeta `vault/`.

Empezar por `00 - Dashboard/Home.md`.