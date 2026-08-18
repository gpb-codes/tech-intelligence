---
type: update
id: ti-2026-002351
title: 'Release: Patch release v5.10.4 — huggingface/transformers'
aliases:
- 'Release: Patch release v5.10.4 — huggingface/transformers'
original_title: 'Release: Patch release v5.10.4 — huggingface/transformers'
company: ''
product: ''
version: v5.10.4
date: '2026-06-15'
created: '2026-06-15 17:29:39'
updated: '2026-08-18T20:12:21+00:00'
original_language: en
translated: true
importance: critical
impact: medium
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Hugging Face Transformers (GitHub)
source_url: https://github.com/huggingface/transformers/releases/tag/v5.10.3
source_type: github
processed_by: ollama
backend: ollama
model: llama3.2:1b
insights: false
status: published
category: General Tech
subcategory: ''
confidence: medium
example: false
tags: []
alternatives:
- name: transformers
  confidence: high
- name: transformers
  confidence: medium
cssclasses:
- ti-note
---

# Release: Patch release v5.10.4 — huggingface/transformers

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🌐 Medio`

| Campo | Valor |
| --- | --- |
| Versión | v5.10.4 |
| Fecha de lanzamiento | 2023-03-01 |
| Requisitos | pytorch-lightning>=1.0.0,<2.0.0 |
| Cambios incompatibles | Corrección de los offsets en la procesamiento |

> [!abstract] Resumen
>
> * Revisión de la versión 5.10.3 de `transformers` para eliminar minorías y mejorar la compatibilidad con `transformers` v5.10.4
> * Corrección de la compatibilidad con `transformers` v5.10.3 mediante ajustes en la LLM
> * Corrección de los offsets en el procesamiento de datos de imagen, video y audio
> * Introducción de una regresión por #45534 y #46456 para mejorar la sincronización con `transformers`
> * Solución común para el backend `mistral` para mejorar la compatibilidad con `transformers` v5.10.4

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Release: Patch release v5.10.4 — huggingface/transformers
> 
> # Patch release v5.10.4 Actualización: Nota que en pypi `5.10.3` no existe y este se ha guardado bajo `5.10.4` (de manera que se ha "saltado" un minorismo). Lo siento, eso es de mí. Solo quería aclarar para hacer que esta se convirtiera en menos confuso. Se necesitan algunos ajustes para la LLM para sincronizar con transformers: * [reparación] Introducción de una regresión por #45534 #46456 por @eustlb (#46456) * Corrección {token_ids de imagen/video/a}_id en ProcessorMixin #46500 por @hmellor (#46500) * Corrección de los offsets en la procesamiento #46525 por @zucchini-nlp (#46525) * Corrección `peft` lower bound #46605 por @hmellor (#46605) * solución común para el backend mistral #46667 por @itazap (#46667) **Changelog completo**: https://github.com/huggingface/transformers/compare/v5.10.2...v5.10.3

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Lanzamiento disruptivo
> - Cambio significativo de producto
> - Cambio importante de precio

## Información técnica ⚒️

- **Versión:** v5.10.4
- **Fecha de lanzamiento:** 2023-03-01
- **Requisitos:** pytorch-lightning>=1.0.0,<2.0.0
- **Cambios incompatibles:** Corrección de los offsets en la procesamiento

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **transformers** — confianza: high
- **transformers** — confianza: medium

## Fuente original 📜

[https://github.com/huggingface/transformers/releases/tag/v5.10.3](https://github.com/huggingface/transformers/releases/tag/v5.10.3)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

# Patch release v5.10.4 Update: Note that on pypi `5.10.3` doesn't exist and this this saved under `5.10.4` (so essentially a minor version skipped). Sorry about that, that's on me. Just wanted to clarify to make this less confusing! A few fixes needed for vLLM to sync with transformers :hugs: * [fix] regression introduced by #45534 #46456 by @eustlb (#46456) * Fix {image/video/audio}_token_ids in ProcessorMixin #46500 by @hmellor (#46500) * Fix InternVL models #46524 by @hmellor (#46524) * Fix the offsets in processing #46525 by @zucchini-nlp (#46525) * Fix `peft` lower bound #46605 by @hmellor (#46605) * mistral common backend fix #46667 by @itazap (#46667) **Full Changelog**: https://github.com/huggingface/transformers/compare/v5.10.2...v5.10.3

</details>

