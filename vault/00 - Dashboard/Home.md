---
type: dashboard
title: Tech Intelligence
aliases: [Inicio, Dashboard]
cssclasses: [ti-dashboard]
---

# ⚔️ Tech Intelligence

<span class="ti-runes">ᛟ ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ ᛟ</span>

_Actualizado: 2026-08-18 08:59 UTC · Forjado con Ollama + OpenRouter · local-first_

> [!info] 🛡️ Estado del sistema
> - **2620** artículos en la base · **7** procesados · **1756** pendientes · **0** fallidos
> - **29** fuentes activas · Vault versionado en Git

<span class="ti-runes">ᛉ ᛋ ᛟ ᛞ</span>

## 🔥 Últimas actualizaciones ⚔️

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", company AS "Empresa", product AS "Producto" FROM "02 - Updates" WHERE status = "published" AND example = false SORT date DESC LIMIT 20
```

_(fallback sin Dataview: últimas 15)_

- Release: Release v5.12.0 — huggingface/transformers _(fuente: Hugging Face Transformers (GitHub))_
- Release: Patch release v5.13.1 — huggingface/transformers _(fuente: Hugging Face Transformers (GitHub))_
- Release: v16.3.1-canary.14 — vercel/next.js _(fuente: Next.js (GitHub))_
- Release: v16.3.1-canary.17 — vercel/next.js _(fuente: Next.js (GitHub))_
- Release: v16.3.1-canary.21 — vercel/next.js _(fuente: Next.js (GitHub))_
- Release: v2.1.226 — anthropics/claude-code _(fuente: Claude Code (GitHub))_
- Release: v2.1.231 — anthropics/claude-code _(fuente: Claude Code (GitHub))_

## IA ᛟ

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/IA" WHERE contains(category, "IA") AND example = false SORT date DESC LIMIT 10
```


## Developer Tools ᛋ

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Developer Tools" WHERE contains(category, "Developer Tools") AND example = false SORT date DESC LIMIT 10
```


## Open Source ᛚ

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Open Source" WHERE contains(category, "Open Source") AND example = false SORT date DESC LIMIT 10
```


## Cloud ᛒ

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Cloud" WHERE contains(category, "Cloud") AND example = false SORT date DESC LIMIT 10
```


## Cybersecurity ᛞ

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Cybersecurity" WHERE contains(category, "Cybersecurity") AND example = false SORT date DESC LIMIT 10
```


## Hardware ᛏ

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Hardware" WHERE contains(category, "Hardware") AND example = false SORT date DESC LIMIT 10
```


## Productivity ᛗ

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Productivity" WHERE contains(category, "Productivity") AND example = false SORT date DESC LIMIT 10
```


## General Tech ᛉ

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/General Tech" WHERE contains(category, "General Tech") AND example = false SORT date DESC LIMIT 10
```

_(fallback: últimas 5)_

- Release: Release v5.12.0 — huggingface/transformers _(fuente: Hugging Face Transformers (GitHub))_
- Release: Patch release v5.13.1 — huggingface/transformers _(fuente: Hugging Face Transformers (GitHub))_
- Release: v16.3.1-canary.14 — vercel/next.js _(fuente: Next.js (GitHub))_
- Release: v16.3.1-canary.17 — vercel/next.js _(fuente: Next.js (GitHub))_
- Release: v16.3.1-canary.21 — vercel/next.js _(fuente: Next.js (GitHub))_

## 💸 Cambios de precio 🪙

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", product AS "Producto", pricing AS "Precio" FROM "02 - Updates" WHERE pricing != "unknown" AND pricing != "open-source" AND example = false SORT date DESC LIMIT 15
```


## 🧠 Nuevos modelos ⚔️

_Sin modelos detectados aún._

## 🔁 Alternativas gratuitas / open source

- Release: Release v5.12.0 — huggingface/transformers _(fuente: Hugging Face Transformers (GitHub))_
- Release: Patch release v5.13.1 — huggingface/transformers _(fuente: Hugging Face Transformers (GitHub))_
- Release: v16.3.1-canary.14 — vercel/next.js _(fuente: Next.js (GitHub))_
- Release: v16.3.1-canary.17 — vercel/next.js _(fuente: Next.js (GitHub))_
- Release: v16.3.1-canary.21 — vercel/next.js _(fuente: Next.js (GitHub))_
- Release: v2.1.226 — anthropics/claude-code _(fuente: Claude Code (GitHub))_
- Release: v2.1.231 — anthropics/claude-code _(fuente: Claude Code (GitHub))_

## 🐙 GitHub

_Sin actividad de GitHub aún._

## 🔬 Tendencias / Investigación

_Sin investigaciones detectadas aún._

## 🛰️ Tech Radar ᛟ

```dataview
TABLE ring AS "Anillo", category AS "Categoría", file.link AS "Nota" FROM "10 - Radar" WHERE type = "trend" SORT ring ASC, date DESC
```

Anillos: 🟢 **ADOPT** · 🔵 **TRIAL** · 🟡 **ASSESS** · 🔴 **HOLD**  
_El Radar se actualiza manualmente en `10 - Radar/`._

<span class="ti-runes">ᛉ ᛋ ᛟ ᛞ</span>

## 📊 Estadísticas

```dataview
TABLE length(rows) AS "Notas" FROM "02 - Updates" GROUP BY category SORT length(rows) DESC
```

## 🗂️ Navegación

- 📁 `01 - Inbox/` — pendientes de revisión, fallidos y contenido largo
- 📰 `02 - Updates/` — noticias procesadas por categoría
- 🏢 `03 - Companies/` — perfiles de empresas
- 🛠️ `04 - Tools/` — herramientas
- 🔁 `05 - Alternatives/` — alternativas open source
- 🧠 `06 - Models/` — modelos de IA
- 💸 `07 - Pricing/` — cambios de precios
- 🐙 `08 - Open Source/` — proyectos de GitHub
- 🔬 `09 - Research/` — investigación y papers
- 🛰️ `10 - Radar/` — Tech Radar
- 📡 `11 - Sources/` — fuentes configuradas
- 🧩 `12 - Templates/` — plantillas de notas
- 💾 `13 - Dataset/` — exportaciones JSONL
