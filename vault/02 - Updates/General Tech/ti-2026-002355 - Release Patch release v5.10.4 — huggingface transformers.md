---
type: update
id: ti-2026-002355
title: 'Release: Patch release v5.10.4 — huggingface/transformers'
aliases:
- 'Release: Patch release v5.10.4 — huggingface/transformers'
original_title: 'Release: Patch release v5.10.4 — huggingface/transformers'
company: ''
product: ''
version: v5.10.4
date: '2026-06-15'
created: '2026-06-15 17:29:39'
updated: '2026-08-18T07:54:53+00:00'
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
processed_by: openrouter
backend: openrouter
model: nvidia/nemotron-3.5-lightning:free
insights: true
status: published
category: General Tech
subcategory: ''
confidence: medium
example: false
tags:
- huggingface/transformers
alternatives:
- name: transformers
  confidence: high
- name: pytorch-transformers
  confidence: medium
- name: transformers-base
  confidence: high
- name: transformers-large
  confidence: high
- name: transformers-base-uncased
  confidence: high
- name: transformers-large-uncased
  confidence: high
cssclasses:
- ti-note
---

# Release: Patch release v5.10.4 — huggingface/transformers

`critical` · `🌐 Medio`

| Campo | Valor |
| --- | --- |
| Versión | v5.10.4 |
| Fecha de lanzamiento | 2023-03-01 |
| Requisitos | python >= 3.7, transformers >= 5.10.2 |
| Cambios incompatibles | Reparaciones de token_ids/image/video/audio, offsets en procesamiento, bóveda de `peft` |

> [!abstract] Resumen
>
> * Revisión de la versión 5.10.3 de transformers, que no existe en pypi y se ha guardado bajo 5.10.4 debido a una corrección en huggingface/transformers.
> * Ajustes para sincronizar vLLM con huggingface/transformers.
> * Correcciones en la implementación de procesamiento de token_ids, video, audio y offsets.
> * Actualización de la bóveda de `peft`.
> * Changelog completo de la versión 5.10.2 a 5.10.3.

## ¿Qué ocurrió?

> [!info] Traducción del anuncio
>
> Release: Patch release v5.10.4 — huggingface/transformers
> 
> # Patch release v5.10.4 Actualización: Nota que en pypi `5.10.3` no existe y este se ha guardado bajo `5.10.4` (así que es un minoraje). Lo siento, eso es de mi parte. Solo quería aclarar para hacer que esta se vuelva menos confusa. Se necesitan algunos ajustes para vLLM sincronizar con transformers :hugs: * [reparación] Introducción de una regresión por #45534 #46456 por @eustlb (#46456) * Reparación {token_ids/image/video/audio}_ de ProcessorMixin #46500 por @hmellor (#46500) * Reparación de los offsets en procesamiento #46525 por @zucchini-nlp (#46525) * Reparación de la bóveda de `peft` #46605 por @hmellor (#46605) * Reparación de la common backend #46667 por @itazap (#46667) **Changelog completo**: https://github.com/huggingface/transformers/compare/v5.10.2...v5.10.3

## ¿Por qué importa?

> [!success] Impacto
>
> - Reparación de la bóveda de `peft`
> - Reparación de los offsets en procesamiento
> - Reparación de la common backend

## 📊 Informe para desarrolladores

> [!info] ¿Qué es?
>
> La tecnología de modelo de lenguaje de alto rendimiento (LLM) Hugging Face, también conocida como Transformers, es un conjunto de herramientas y bibliotecas diseñadas para crear y entrenar modelos de lenguaje avanzados para aplicaciones de inteligencia artificial y procesamiento de lenguaje natural.

> [!tip] ¿En qué ayuda al desarrollo?
>
> La tecnología de LLM Hugging Face proporciona herramientas y bibliotecas útiles para desarrolladores y profesionales de la inteligencia artificial y el procesamiento de lenguaje natural, lo que facilita el desarrollo de aplicaciones más complejas y precisas.

### Relevancia por perfil

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | La capacidad de procesar y analizar grandes cantidades de texto de manera eficiente y precisa. · La comprensión de la estructura y el lenguaje natural de los textos. · La capacidad de generar texto coherente y natural. |
| Junior | Media | La capacidad de utilizar herramientas y bibliotecas de desarrollo de software como PyTorch o TensorFlow. · La comprensión de la estructura y el lenguaje natural de los textos. · La capacidad de realizar tareas de procesamiento de lenguaje natural. |
| Semi-Senior | Alta | La capacidad de utilizar herramientas y bibliotecas de desarrollo de software como PyTorch o TensorFlow. · La comprensión de la estructura y el lenguaje natural de los textos. · La capacidad de realizar tareas de procesamiento de lenguaje natural y de análisis de datos. |
| Senior | Alta | La capacidad de utilizar herramientas y bibliotecas de desarrollo de software como PyTorch o TensorFlow. · La comprensión de la estructura y el lenguaje natural de los textos. · La capacidad de realizar tareas de procesamiento de lenguaje natural, análisis de datos y de inteligencia artificial. |
| Ingeniero de Software | Alta | La capacidad de diseñar y desarrollar sistemas de software utilizando herramientas y bibliotecas de desarrollo de software como PyTorch o TensorFlow. · La comprensión de la estructura y el lenguaje natural de los textos. · La capacidad de realizar tareas de procesamiento de lenguaje natural, análisis de datos y de inteligencia artificial. |
| Ingeniero en Redes | Alta | La capacidad de diseñar y desarrollar redes neuronales utilizando herramientas y bibliotecas de aprendizaje automático como PyTorch o TensorFlow. · La comprensión de la estructura y el lenguaje natural de los textos. · La capacidad de realizar tareas de procesamiento de lenguaje natural, análisis de datos y de inteligencia artificial. |
| DevOps / SRE | Alta | La capacidad de implementar y mantener sistemas de infraestructura de software utilizando herramientas y bibliotecas de DevOps como Docker o Kubernetes. · La comprensión de la estructura y el lenguaje natural de los textos. · La capacidad de realizar tareas de procesamiento de lenguaje natural, análisis de datos y de inteligencia artificial. |
| Ciberseguridad | Alta | La capacidad de diseñar y desarrollar sistemas de seguridad utilizando herramientas y bibliotecas de seguridad como Scapy o Nmap. · La comprensión de la estructura y el lenguaje natural de los textos. · La capacidad de realizar tareas de procesamiento de lenguaje natural, análisis de datos y de inteligencia artificial. |


## Información técnica

- **Versión:** v5.10.4
- **Fecha de lanzamiento:** 2023-03-01
- **Requisitos:** python >= 3.7, transformers >= 5.10.2
- **Cambios incompatibles:** Reparaciones de token_ids/image/video/audio, offsets en procesamiento, bóveda de `peft`

## Precio

> [!money] unknown
>
> $20/mes

## Alternativas

- **transformers** — confianza: high
- **pytorch-transformers** — confianza: medium
- **transformers-base** — confianza: high
- **transformers-large** — confianza: high
- **transformers-base-uncased** — confianza: high
- **transformers-large-uncased** — confianza: high

## Fuente original

[https://github.com/huggingface/transformers/releases/tag/v5.10.3](https://github.com/huggingface/transformers/releases/tag/v5.10.3)

## Contenido original

<details>
<summary>Ver contenido original (no traducido)</summary>

# Patch release v5.10.4 Update: Note that on pypi `5.10.3` doesn't exist and this this saved under `5.10.4` (so essentially a minor version skipped). Sorry about that, that's on me. Just wanted to clarify to make this less confusing! A few fixes needed for vLLM to sync with transformers :hugs: * [fix] regression introduced by #45534 #46456 by @eustlb (#46456) * Fix {image/video/audio}_token_ids in ProcessorMixin #46500 by @hmellor (#46500) * Fix InternVL models #46524 by @hmellor (#46524) * Fix the offsets in processing #46525 by @zucchini-nlp (#46525) * Fix `peft` lower bound #46605 by @hmellor (#46605) * mistral common backend fix #46667 by @itazap (#46667) **Full Changelog**: https://github.com/huggingface/transformers/compare/v5.10.2...v5.10.3

</details>

