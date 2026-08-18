# 11 - Sources

Documentación de las fuentes configuradas (ver `config/sources.yaml`).

## Tipos soportados

- `rss`: feeds RSS/Atom (feedparser)
- `github`: releases/tags vía GitHub API
- `api`: APIs REST genéricas (JSON)

## Cómo agregar una fuente

1. Editar `config/sources.yaml`.
2. Ejecutar `tech-intelligence sync` (o `collect`).

Sin modificar código.

## Estado

_El sistema actualiza `last_checked` en SQLite tras cada consulta._