# Tech Intelligence

Sistema **local-first** de inteligencia tecnológica: recopila automáticamente actualizaciones del mundo tech (RSS, GitHub, APIs), las procesa localmente con **Ollama** (traducción al español, resumen, clasificación, deduplicación) y las organiza como conocimiento estructurado en un **Vault de Obsidian**, versionado con **Git**.

```text
RSS / GitHub / APIs
        ↓
     Collector
        ↓
      SQLite
        ↓
      Ollama
        ↓
 Markdown / JSONL
        ↓
     Obsidian
        ↓
        Git
```

## ¿Qué es?

Un radar automático del ecosistema tecnológico: IA, LLMs, AI agents, AI coding, developer tools, IDEs, CLI, open source, GitHub, APIs, SDKs, cloud, DevOps, cybersecurity, databases, productivity, browsers, OS, hardware, robótica, SaaS, startups, nuevos modelos, versiones, cambios de precio, alternativas gratuitas/open source, self-hosted, investigaciones, lanzamientos, vulnerabilidades y tendencias.

**No es un lector de noticias**: es una infraestructura de inteligencia tecnológica personal, automática y reproducible.

## Principios

1. Local-first (Ollama local, sin proveedores de IA externos).
2. Automatización completa (CLI + scheduler).
3. Modularidad (adaptadores de fuentes, módulos de IA, generadores).
4. Datos estructurados (Markdown + YAML + JSONL + SQLite).
5. No inventar información: la fuente original siempre tiene prioridad.
6. Mantener historial, detectar duplicados, poder re-procesar.
7. Agregar fuentes y cambiar de modelo sin modificar el código.

## Arquitectura

```text
                      ┌───────────────┐
                      │   RSS/Atom    │
                      └───────┬───────┘
                      ┌───────▼───────┐
                      │    GitHub     │  (releases + tags)
                      └───────┬───────┘
                      ┌───────▼───────┐
                      │     APIs      │  (REST JSON genérico)
                      └───────┬───────┘
                              ▼
                     ┌─────────────────┐
                     │    COLLECTOR    │  fetch → normalize → validate → dedupe
                     └────────┬────────┘
                              ▼
                     ┌─────────────────┐
                     │     SQLITE      │  sources, articles, jobs, results, hashes, errors
                     └────────┬────────┘
                              ▼
                     ┌─────────────────┐
                     │     OLLAMA      │  idioma, traducción, resumen, clasificación, extracción
                     └────────┬────────┘
                              ▼
                     ┌─────────────────┐
                     │    GENERATOR    │  Markdown (frontmatter YAML) + Dashboard + JSONL
                     └────────┬────────┘
                              ▼
                     ┌─────────────────┐
                     │   OBSIDIAN      │  vault/ (se versiona con Git)
                     └────────┬────────┘
                              ▼
                              Git (commits automáticos)
```

## Stack

| Capa       | Tecnología                     |
| ---------- | ------------------------------ |
| Lenguaje   | Python 3.10+                   |
| Collector  | requests, feedparser           |
| Estado     | SQLite (stdlib, WAL)           |
| IA         | Ollama HTTP API (local)        |
| Conocimiento | Markdown + YAML frontmatter  |
| Dataset    | JSONL                          |
| Interfaz   | Obsidian (sin plugins obligatorios) |
| Versionado | Git (subprocess, seguro)       |
| Contenedores | Docker / docker-compose      |

## Estructura de archivos

```text
tech-intelligence/
├── app/
│   ├── collector/      adaptadores RSS/GitHub/API + deduplicación + pipeline
│   ├── sources/        carga de fuentes y categorías
│   ├── database/       conexión, esquema y repositorio SQLite
│   ├── ollama/         cliente HTTP + detección de idioma + módulos IA + prompts/
│   ├── processor/      orquestación del pipeline de procesamiento
│   ├── generator/      notas Markdown + Dashboard
│   ├── exporters/      exportación JSONL
│   ├── scheduler/      ejecución automática (con lock anti-concurrencia)
│   ├── gitutils/       git init/commit seguro
│   ├── health/         health check
│   ├── cli/            interfaz de línea de comandos
│   ├── utils/          config, logging rotativo, hashing, texto
│   ├── orchestrator.py pipeline completo
│   └── seed.py         datos de ejemplo (example: true)
├── config/
│   ├── sources.yaml    fuentes (RSS/GitHub/API) — URLs verificadas
│   ├── categories.yaml categorías, niveles de importancia, precios, radar
│   └── settings.yaml   ajustes generales
├── database/           SQLite (NO versionado)
├── vault/              Vault de Obsidian (versionado)
│   ├── 00 - Dashboard/    Home.md (Dataview + fallback)
│   ├── 01 - Inbox/        Review/, Failed/, Sources/
│   ├── 02 - Updates/      AI, Developer Tools, Open Source, Cloud, Cybersecurity, Hardware, Productivity, General Tech
│   ├── 03 - Companies/ … 10 - Radar/ 11 - Sources/ 12 - Templates/ 13 - Dataset/ 99 - System/
├── logs/               logs rotativos (NO versionados)
├── tests/              pytest (unit + integración)
├── docker/             entrypoint
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Instalación

### Local (Windows/Linux/macOS)

Requisitos: Python 3.10+, [Ollama](https://ollama.com) instalado y corriendo.

```bash
git clone <repository>
cd tech-intelligence
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -e ".[dev]"

cp .env.example .env            # ajustar OLLAMA_MODEL
ollama pull llama3.1            # instalar el modelo elegido

tech-intelligence health        # comprobar servicios
tech-intelligence sync          # pipeline completo
```

### Docker

```bash
git clone <repository>
cd tech-intelligence
cp .env.example .env            # ajustar OLLAMA_MODEL
docker compose up -d            # levanta ollama + collector (scheduler)

docker compose exec collector tech-intelligence health
docker compose exec collector tech-intelligence sync
```

El Vault se monta en `./vault`, la base de datos en `./database/` y los modelos de Ollama persisten en el volumen `ollama_data`.

## Configuración

### .env

```env
OLLAMA_BASE_URL=http://localhost:11434   # en Docker: http://ollama:11434
OLLAMA_MODEL=llama3.1
OLLAMA_TIMEOUT=120
VAULT_PATH=./vault
DATABASE_PATH=./database/tech_intelligence.db
SYNC_INTERVAL=60             # minutos entre ciclos
LOG_LEVEL=INFO
GITHUB_TOKEN=                # opcional, evita rate limits de GitHub
MAX_PROCESSING_ATTEMPTS=3
```

### Fuentes (`config/sources.yaml`)

```yaml
sources:
  - id: openai-blog
    name: OpenAI Blog
    type: rss                  # rss | github | api
    enabled: true
    url: "https://openai.com/news/rss.xml"
    category: AI
    priority: high

  - id: gh-opencode
    name: OpenCode (GitHub)
    type: github
    enabled: true
    repository: sst/opencode
    category: Developer Tools
    priority: high
```

> Las URLs incluidas fueron verificadas (HTTP 200). Fuentes sin feed oficial verificable quedan marcadas `enabled: false` (pendientes).

### Cambiar de modelo

Editar `OLLAMA_MODEL` en `.env` y volver a procesar:

```bash
tech-intelligence process --all   # re-procesa con el nuevo modelo
```

### Agregar fuentes

Editar `config/sources.yaml` → `tech-intelligence sync`. Sin modificar código.

## SQLite

Estado interno del sistema (no reemplaza al Vault):

```text
sources            fuentes configuradas y last_checked
articles           artículos normalizados (status: new/pending/processing/processed/failed/review)
processing_jobs    intentos por artículo (retries)
processing_results resultado del pipeline por artículo
hashes             índices de deduplicación
errors             errores por fuente
meta               contadores (ti-YYYY-NNNNNN) y versión de esquema
```

## Deduplicación

Orden de prioridad:

```text
1. canonical_url
2. external_id (source_id + external_id)
3. content_hash
4. title_hash + fecha de publicación (±2 días)
```

Si ya existe → no se vuelve a procesar. Si la fuente actualizó el contenido → se actualiza y re-procesa (se conserva historial en Git).

## Pipeline de procesamiento (Ollama)

```text
nuevo artículo
  → detección de idioma (heurística local)
  → ¿español? no → traducción vía Ollama (prompt: prompts/translate.txt)
  → resumen en español (summarize.txt)
  → clasificación JSON (classify.txt): empresa, producto, categoría, precio, licencia, tags
  → extracción de metadata (extract.txt): versión, fecha, precio, URLs, requisitos
  → importancia (importance.txt): critical/high/medium/low + impacto
  → alternativas (alternative.txt): solo con evidencia, confidence high/medium
  → validación → nota Markdown (o Inbox/Review si es low)
```

Los prompts viven en `app/ollama/prompts/*.txt` y pueden editarse sin tocar código.

## Markdown / Obsidian

Cada artículo genera una nota con frontmatter YAML:

```yaml
---
type: update
id: ti-2026-000001
title: "..."
company: "..."
product: "..."
date: 2026-08-17
original_language: en
translated: true
importance: high
impact: medium
pricing: unknown
source: "..."
source_url: "..."
processed_by: ollama
model: llama3.1
status: published
example: false
tags: [...]
alternatives: [...]
---
```

- Importancia `low` → `01 - Inbox/Review/`.
- Contenido muy largo (> 15000 chars) → `01 - Inbox/Sources/<fuente>/` con enlace desde la nota.
- El contenido original nunca se pierde (sección "Contenido original").
- El Dashboard (`00 - Dashboard/Home.md`) funciona con Dataview **y** sin plugins (fallback con listas estáticas).
- Abrir Obsidian → "Open folder as vault" → carpeta `vault/`.

## JSONL

`vault/13 - Dataset/`: `all.jsonl`, `updates.jsonl`, `tools.jsonl`, `models.jsonl`, `companies.jsonl`, `alternatives.jsonl`. Una línea = un objeto. Sirve para RAG, análisis, búsqueda semántica o fine-tuning experimental futuro (sin entrenamiento automático).

## Git

- `git init` automático en el primer sync.
- Commit automático solo tras un ciclo exitoso: `tech-intelligence: sync YYYY-MM-DD`.
- No se crean commits vacíos.
- **Nunca** se ejecutan automáticamente `push --force`, `reset --hard` ni `clean -fd`.
- Se versionan: Markdown, JSONL, configuración, templates. No se versionan: SQLite, logs, `.env`.

## CLI

```bash
tech-intelligence sync            # pipeline completo (collect + process + export + git)
tech-intelligence collect         # solo recopilar
tech-intelligence process         # procesar pendientes
tech-intelligence process --id ti-2026-000001   # re-procesar uno
tech-intelligence process --failed              # reintentar fallidos
tech-intelligence process --all                 # re-procesar todo
tech-intelligence export          # generar JSONL
tech-intelligence health          # comprobar servicios
tech-intelligence sources         # listar fuentes
tech-intelligence retry           # reintentar artículos fallidos
tech-intelligence stats           # estadísticas
tech-intelligence scheduler       # ejecución automática (SYNC_INTERVAL minutos)
tech-intelligence seed            # datos de ejemplo (example: true)
```

## Scheduler

`SYNC_INTERVAL` en minutos. Usa un lockfile con PID para evitar ejecuciones concurrentes. En Docker corre dentro del contenedor `collector`.

## Health check

```text
SQLite       OK  1144 artículos
Ollama       OK  llama3.1 instalado
Vault        OK  ./vault
Git          OK  repo inicializado
Sources      OK  22 habilitadas de 25
Pending      OK  12
Failed       OK  1
Processed    OK  1240
```

## Datos de ejemplo

```bash
tech-intelligence seed
```

Inserta registros con `example: true` (claramente marcados) usando tecnologías reales (OpenCode, Ollama, OpenAI, etc.) **sin inventar precios ni versiones actuales**.

## Tests

```bash
pip install -e ".[dev]"
pytest
```

Cubren: RSS parsing, GitHub, deduplicación, detección de idioma, cliente Ollama, traducción, clasificación, generación Markdown, exportación JSONL, SQLite, Git, configuración e integración (pipeline completo con Ollama simulado).

## Troubleshooting

| Problema | Solución |
| -------- | -------- |
| `Ollama FAIL` en health | Arrancar Ollama (`ollama serve`) y verificar `OLLAMA_BASE_URL` |
| `model not found` | `ollama pull <modelo>` (ajustar `OLLAMA_MODEL`) |
| Artículos pendientes que no avanzan | Revisar `logs/ollama.log` y `logs/errors.log`; `tech-intelligence process` reintenta |
| Rate limit de GitHub | Configurar `GITHUB_TOKEN` en `.env` |
| El Vault no muestra nada | Abrir `vault/` en Obsidian y ejecutar `tech-intelligence sync` |

## Backups

- El Vault está versionado en Git → `git log` es el historial.
- Antes de cambios masivos, copiar `vault/` y `database/` o usar `git tag backup-<fecha>`.
- El sistema nunca elimina contenido del Vault automáticamente.

## Limitaciones

- La detección de idioma es heurística (sin modelos externos): textos muy cortos pueden quedar como `unknown` (no se traducen).
- El clasificador depende de la calidad del modelo de Ollama instalado.
- GitHub se monitorea por releases/tags (no commits).
- No hay web scraping en la primera versión (la arquitectura lo permite luego).

## Próximos pasos

- Web scraping, YouTube, Reddit, HN, Product Hunt, arXiv, NPM, PyPI, Docker Hub como adaptadores.
- RAG / Qdrant sobre el dataset JSONL.
- Web API, Discord, Telegram, WhatsApp, AI agents.
- Fine-tuning experimental con el dataset limpio.

## Privacidad

Todo el procesamiento es local: el contenido recopilado no se envía a proveedores externos de IA. No se almacenan secretos en Markdown, SQLite, JSONL, Git ni logs (`.env` está en `.gitignore`).

---

*Local-first · Automatizable · Modular · Reproducible · Preparado para crecer*