---
type: dashboard
title: Tech Intelligence
aliases: [Inicio, Dashboard]
cssclasses: [ti-dashboard]
---

# 🛰️ Tech Intelligence

_Actualizado: 2026-08-18 07:53 UTC · Sistema local-first · Procesado con Ollama_

> [!info] Estado del sistema
> - **2429** artículos en la base · **10** procesados · **642** pendientes · **802** fallidos
> - **22** fuentes activas · Vault versionado en Git

## 🔥 Últimas actualizaciones

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", company AS "Empresa", product AS "Producto" FROM "02 - Updates" WHERE status = "published" AND example = false SORT date DESC LIMIT 20
```

_(fallback sin Dataview: últimas 15)_

- Release: 1.127.0 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.128.1 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.129.1 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.130.0 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.131.0 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.132.1 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: v1.0.0 — deepseek-ai/DeepSeek-V3 _(fuente: DeepSeek-V3 (GitHub))_

## IA

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/IA" WHERE contains(category, "IA") AND example = false SORT date DESC LIMIT 10
```

_(fallback: últimas 1)_

- Release: v1.0.0 — deepseek-ai/DeepSeek-V3 _(fuente: DeepSeek-V3 (GitHub))_

## Developer Tools

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Developer Tools" WHERE contains(category, "Developer Tools") AND example = false SORT date DESC LIMIT 10
```

_(fallback: últimas 5)_

- Release: 1.127.0 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.128.1 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.129.1 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.130.0 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.131.0 — microsoft/vscode _(fuente: VS Code (GitHub))_

## Open Source

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Open Source" WHERE contains(category, "Open Source") AND example = false SORT date DESC LIMIT 10
```


## Cloud

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Cloud" WHERE contains(category, "Cloud") AND example = false SORT date DESC LIMIT 10
```


## Cybersecurity

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Cybersecurity" WHERE contains(category, "Cybersecurity") AND example = false SORT date DESC LIMIT 10
```


## Hardware

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Hardware" WHERE contains(category, "Hardware") AND example = false SORT date DESC LIMIT 10
```


## Productivity

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/Productivity" WHERE contains(category, "Productivity") AND example = false SORT date DESC LIMIT 10
```


## General Tech

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", importance AS "Importancia", product AS "Producto" FROM "02 - Updates/General Tech" WHERE contains(category, "General Tech") AND example = false SORT date DESC LIMIT 10
```


## 💸 Cambios de precio

```dataview
TABLE WITHOUT ID file.link AS "Nota", date AS "Fecha", product AS "Producto", pricing AS "Precio" FROM "02 - Updates" WHERE pricing != "unknown" AND pricing != "open-source" AND example = false SORT date DESC LIMIT 15
```


## 🧠 Nuevos modelos

- Release: v1.0.0 — deepseek-ai/DeepSeek-V3 _(fuente: DeepSeek-V3 (GitHub))_

## 🔁 Alternativas gratuitas / open source

- Release: 1.127.0 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.128.1 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.129.1 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.130.0 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.131.0 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: 1.132.1 — microsoft/vscode _(fuente: VS Code (GitHub))_
- Release: v1.0.0 — deepseek-ai/DeepSeek-V3 _(fuente: DeepSeek-V3 (GitHub))_

## 🐙 GitHub

_Sin actividad de GitHub aún._

## 🔬 Tendencias / Investigación

_Sin investigaciones detectadas aún._

## 🛰️ Tech Radar

```dataview
TABLE ring AS "Anillo", category AS "Categoría", file.link AS "Nota" FROM "10 - Radar" WHERE type = "trend" SORT ring ASC, date DESC
```

Anillos: 🟢 **ADOPT** · 🔵 **TRIAL** · 🟡 **ASSESS** · 🔴 **HOLD**  
_El Radar se actualiza manualmente en `10 - Radar/`._

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
