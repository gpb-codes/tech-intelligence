---
type: update
id: ti-2319
title: "Release: v0.32.10 — ollama/ollama"
aliases: ["Release: v0.32.10 — ollama/ollama"]
original_title: "Release: v0.32.10 — ollama/ollama"
company: "Ollama"
product: "Ollama"
version: "v0.32.10"
date: "2026-08-12"
created: "2026-08-12 22:36:49"
updated: "2026-08-18"
original_language: en
translated: true
importance: low
impact: low
pricing: unknown
license: unknown
open_source: true
self_hosted: true
source: "Ollama (GitHub)"
source_url: "https://github.com/ollama/ollama/releases/tag/v0.32.10"
source_type: rss
processed_by: manual
model: opencode
status: published
category: "AI"
subcategory: ""
confidence: medium
tags: [ai, llm, open-source, ollama]
alternatives: []
insights: true
cssclasses: [ti-note]
---

# Release: v0.32.10 — ollama/ollama

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`⚪ Baja` · `🌱 Bajo` · `confianza: medium`

| Campo | Valor |
| --- | --- |
| Fuente | **Ollama (GitHub)** |

> [!abstract] Resumen 🛡️
> Ollama publica la versión v0.32.10: los modelos sin `repeat_penalty` pasan a usar 1.0 (off) por defecto, prefill más rápido en modelos MLX NVFP4 y corrección en la verificación de blobs de manifiestos OCI.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
> La release v0.32.10 de Ollama cambia el `repeat_penalty` por defecto a 1.0 (desactivado) para modelos que no lo definen, acelerando la decodificación especulativa y alineándose con otros motores. También mejora el prefill en modelos NVFP4 MLX (7-8 % más rápido en Qwen3.6 y Muse Glimmer) y arregla la verificación de blobs cuando el config y la capa de un manifiesto OCI comparten digest.

## ¿Por qué importa? 🛡️

> [!success] Impacto
> - El cambio de `repeat_penalty` afecta a la generación de modelos propensos a repeticiones.
> - La optimización de prefill acelera la carga de modelos MLX en hardware Apple.

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
> Una release de mantenimiento de Ollama, el motor de inferencia local de LLMs, con cambios en parámetros por defecto, prefill y verificación OCI.

> [!tip] ¿En qué ayuda al desarrollo?
> Mejora el rendimiento de la decodificación especulativa y del prefill en modelos NVFP4 MLX; revisa los modelos antiguos que repitan texto.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Baja | Ollama sigue siendo la puerta de entrada a LLMs locales. |
| Junior | Baja | Actualiza tu instalación local sin cambios de configuración. |
| Semi-Senior | Media | Revisa el `repeat_penalty` por defecto en tus modelos. |
| Senior | Media | Planifica la actualización en despliegues de inferencia local. |
| Ingeniero de Software | Media | Integra la nueva release en tus pipelines de LLM local. |
| Ingeniero en Redes | Baja | Sin impacto relevante. |
| DevOps / SRE | Media | Actualiza imágenes y revisa el registro de cambios. |
| Ciberseguridad | Baja | Sin impacto relevante. |

## Información técnica ⚒️

- **Licencia:** unknown

## Precio 🪙

> [!money] 🧡 Open source
> No se ha detectado información de precios en la fuente.

## Fuente original 📜

[https://github.com/ollama/ollama/releases/tag/v0.32.10](https://github.com/ollama/ollama/releases/tag/v0.32.10)
