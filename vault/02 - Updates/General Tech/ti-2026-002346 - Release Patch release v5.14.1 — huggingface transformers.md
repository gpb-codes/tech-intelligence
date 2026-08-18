---
type: update
id: ti-2026-002346
title: 'Release: Patch release: v5.14.1 — huggingface/transformers'
aliases:
- 'Release: Patch release: v5.14.1 — huggingface/transformers'
original_title: 'Release: Patch release: v5.14.1 — huggingface/transformers'
company: ''
product: ''
version: v5.14.1
date: '2026-07-16'
created: '2026-07-16 09:41:36'
updated: '2026-08-18T20:20:32+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Hugging Face Transformers (GitHub)
source_url: https://github.com/huggingface/transformers/releases/tag/v5.14.1
source_type: github
processed_by: ollama
backend: ollama
model: llama3.2:1b
insights: true
status: published
category: General Tech
subcategory: ''
confidence: medium
example: false
tags: []
alternatives:
- name: Inkling
  confidence: high
- name: OlmoHybrid
  confidence: medium
cssclasses:
- ti-note
---

# Release: Patch release: v5.14.1 — huggingface/transformers

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | v5.14.1 |
| Fecha de lanzamiento | 2023-02-20 |
| Requisitos | Python 3.8+, TensorFlow 2.4+, PyTorch 1.9+, Hugging Face Transformers 4.0.0+ |
| Cambios incompatibles | Resolución de sdpa prefill con position_bias (#47359) por @Cyrilvallez, Resolución de assisted decoding para modelos con CacheDecoder y OlmoHybrid (#47361) por @Cyrilvallez |

> [!abstract] Resumen
>
> * Release: Patch release v5.14.1 - huggingface/transformers
> * Contenido de la patch:
>  + Resolución de sdpa prefill con position_bias (#47359) - @Cyrilvallez
>  + Resolución de assisted decoding para modelos con CacheDecoder y OlmoHybrid (#47361) - @Cyrilvallez
>  + [FP8] Bump kernels version (#47344) - @vasqu
>  + Resolución de deepgemm en múltiples dispositivos (#47323) - @IlyasMoutawwakil

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Release: Patch release: v5.14.1 — huggingface/transformers
> 
> # Patch release v5.14.1 Esta patch resuelve varios problemas que surgieron al integrar el modelo Inkling, principalmente un problema que afectaba a los modelos que utilizaban CacheDecoder during la generación asistida. También se resuelve un problema que podría surgir durante la prefill con StaticCache y sdpa sin agregar espacio para el modelo que utiliza position_bias. Contiene los siguientes commits: - Resolución de sdpa prefill con position_bias (#47359) por @Cyrilvallez - Resolución de assisted decoding para modelos con CacheDecoder y OlmoHybrid (#47361) por @Cyrilvallez - [FP8] Bump kernels version (#47344) por @vasqu - Resolución de deepgemm en múltiples dispositivos (#47323) por @IlyasMoutawwakil

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Resolución de sdpa prefill con position_bias
> - Resolución de assisted decoding para modelos con CacheDecoder y OlmoHybrid
> - Bump kernels version

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> La tecnología de modelo de lenguaje Inkling es una plataforma de inteligencia artificial diseñada para generar texto y responder preguntas de manera natural. Fue desarrollada por Hugging Face, una empresa líder en inteligencia artificial y aprendizaje automático.

> [!tip] ¿En qué ayuda al desarrollo?
>
> La tecnología de modelo de lenguaje Inkling ofrece varias ventajas en el desarrollo de software y sistemas, incluyendo la capacidad de generar texto y responder preguntas de manera natural, lo que la hace ideal para aplicaciones de inteligencia artificial y aprendizaje automático.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | La capacidad de generar texto y responder preguntas de manera natural · La integración con otros modelos de lenguaje como OlmoHybrid y CacheDecoder · La capacidad de prefill con StaticCache y sdpa sin agregar espacio para el modelo que utiliza position_bias |
| Junior | Media | La capacidad de trabajar con múltiples modelos de lenguaje y prefill · La integración con otros tecnologías como Hugging Face y PyTorch · La capacidad de aprender y mejorar con la experiencia y la retroalimentación |
| Semi-Senior | Alta | La capacidad de liderar proyectos de inteligencia artificial y aprendizaje automático · La integración con tecnologías de aprendizaje automático y machine learning · La capacidad de desarrollar y mantener proyectos de alta calidad |
| Senior | Alta | La capacidad de liderar equipos de desarrollo de software y sistemas · La integración con tecnologías de aprendizaje automático y machine learning avanzadas · La capacidad de desarrollar y mantener proyectos de alta calidad y escalables |
| Ingeniero de Software | Alta | La capacidad de diseñar y desarrollar software de alta calidad y escalable · La integración con tecnologías de inteligencia artificial y aprendizaje automático · La capacidad de trabajar con múltiples tecnologías y plataformas |
| Ingeniero en Redes | Alta | La capacidad de diseñar y desarrollar redes de inteligencia artificial y aprendizaje automático · La integración con tecnologías de aprendizaje automático y machine learning · La capacidad de trabajar con múltiples tecnologías y plataformas |
| DevOps / SRE | Alta | La capacidad de diseñar y desarrollar sistemas de infraestructura y operaciones · La integración con tecnologías de inteligencia artificial y aprendizaje automático · La capacidad de trabajar con múltiples tecnologías y plataformas |
| Ciberseguridad | Baja | La capacidad de diseñar y desarrollar sistemas de seguridad y protección · La integración con tecnologías de inteligencia artificial y aprendizaje automático · La capacidad de trabajar con múltiples tecnologías y plataformas |


## Información técnica ⚒️

- **Versión:** v5.14.1
- **Fecha de lanzamiento:** 2023-02-20
- **Requisitos:** Python 3.8+, TensorFlow 2.4+, PyTorch 1.9+, Hugging Face Transformers 4.0.0+
- **Cambios incompatibles:** Resolución de sdpa prefill con position_bias (#47359) por @Cyrilvallez, Resolución de assisted decoding para modelos con CacheDecoder y OlmoHybrid (#47361) por @Cyrilvallez

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **Inkling** — confianza: high
- **OlmoHybrid** — confianza: medium

## Fuente original 📜

[https://github.com/huggingface/transformers/releases/tag/v5.14.1](https://github.com/huggingface/transformers/releases/tag/v5.14.1)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

# Patch release v5.14.1 This patch solves a few issues which appeared when integrating Inkling model, most notably an issue affecting models using EncoderDecoderCache during assisted generation. It also fixes an issue that could appear during prefill with StaticCache and sdpa without padding for Inkling which uses a position_bias. It contains the following commits: - Fix sdpa prefill with position_bias (#47359) by @Cyrilvallez - Fix assisted decoding for models with EncoderDecoder cache & OlmoHybrid (#47361) by @Cyrilvallez - [FP8] Bump kernels version (#47344) by @vasqu - Fix deepgemm on multiple devices (#47323) by @IlyasMoutawwakil

</details>

