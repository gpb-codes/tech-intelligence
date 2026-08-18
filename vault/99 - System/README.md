# Sistema

Documentación interna del sistema Tech Intelligence.

- `README.md` (raíz del proyecto): documentación completa.
- `config/`: fuentes, categorías y ajustes.
- `database/`: SQLite (estado interno, no se versiona).
- `logs/`: logs rotativos (no se versionan).
- `vault/`: conocimiento en Markdown (se versiona).

## Notas del sistema

- El Vault funciona sin plugins; Dataview es opcional y se usa en el Dashboard.
- Los JSONL se regeneran en cada sync dentro de `13 - Dataset/`.
- Las notas con importancia `low` van a `01 - Inbox/Review/` para revisión manual.
- Los artículos fallidos van a `01 - Inbox/Failed/` (generados por el procesador).