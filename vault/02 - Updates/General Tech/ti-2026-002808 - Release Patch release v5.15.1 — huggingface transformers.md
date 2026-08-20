---
type: update
id: ti-2026-002808
title: 'Release: Patch release: v5.15.1 — huggingface/transformers'
aliases:
- 'Release: Patch release: v5.15.1 — huggingface/transformers'
original_title: 'Release: Patch release: v5.15.1 — huggingface/transformers'
company: ''
product: ''
version: v5.15.1
date: '2026-08-19'
created: '2026-08-19 10:50:47'
updated: '2026-08-20T01:55:55+00:00'
original_language: en
translated: true
importance: critical
impact: medium
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Hugging Face Transformers (GitHub)
source_url: https://github.com/huggingface/transformers/releases/tag/v5.15.1
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
- name: DFlash
  confidence: high
- name: Generadores candidatos
  confidence: medium
- name: Filtro Lanczos
  confidence: medium
- name: Configuración de MTP
  confidence: medium
- name: Distribuciones logit
  confidence: medium
- name: Video a dispositivo
  confidence: medium
cssclasses:
- ti-note
---

# Release: Patch release: v5.15.1 — huggingface/transformers

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🌐 Medio`

| Campo | Valor |
| --- | --- |
| Versión | v5.15.1 |
| Fecha de lanzamiento | 2023-02-20 |
| Requisitos | Python 3.8+, TensorFlow 2.4+, PyTorch 1.9+, CUDA 11.0+ |
| Cambios incompatibles | Resolución del desequilibrio de token de candidato con la configuración de dispositivo "auto" |

> [!abstract] Resumen
>
> * Release: Patch release v5.15.1 — huggingface/transformers
> * Contenido: Resolución de problemas con DFlash y generadores candidatos, así como un problema con imágenes en el acelerador.
> * Ocurrió: Desequilibrio de token de candidato con configuración de dispositivo "auto", alineación de distribuciones logit para generadores candidatos, resolución de config de MTP, fallo de fallback de 'lanczos' a 'bicubic'.
> * Producto o tecnología involucrada: Patch release v5.15.1 de huggingface/transformers.
> * Es relevante: Porque se trata de una actualización importante para mejorar la estabilidad y la funcionalidad de los modelos de procesamiento de lenguaje natural.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Release: Patch release: v5.15.1 — huggingface/transformers
> 
> # Patch release v5.15.1 Esta patch resuelve principalmente varios problemas con DFlash y generadores candidatos, así como un problema donde las imágenes podrían no ser procesadas en el acelerador si se utilizaba el filtro Lanczos. Contiene los siguientes commits: - Resolución del desequilibrio de token de candidato con la configuración de dispositivo "auto" (¡@sywangyi y @Cyrilvallez) - Alineación de distribuciones logit para los generadores candidatos utilizando sampling (¡@Cyrilvallez) - Resolución del config de MTP cuando los tipos de MLP están ausentes (¡@Cyrilvallez) - Fallo de fallback de 'lanczos' a 'bicubic' cuando se está en CUDA (¡@zucchini-nlp) - Resolución del gemma4 video a dispositivo (¡@guarin)

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Resolución de problemas con DFlash y generadores candidatos
> - Resolución de problemas con el filtro Lanczos en el acelerador
> - Alineación de distribuciones logit para los generadores candidatos utilizando sampling

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> Hugging Face Transformers es una plataforma de inteligencia artificial desarrollada por Hugging Face, una empresa líder en el campo de la inteligencia artificial y el aprendizaje automático. Es una herramienta de código abierto que permite a los desarrolladores crear modelos de inteligencia artificial de alta precisión para una amplia variedad de tareas, desde la traducción automática hasta la generación de contenido.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Hugging Face Transformers ofrece varias ventajas en el desarrollo de software y sistemas, incluyendo la capacidad de crear modelos de inteligencia artificial de alta precisión, la facilitación de la colaboración entre desarrolladores y expertos en inteligencia artificial, y la posibilidad de automatizar tareas repetitivas.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | Crear modelos de inteligencia artificial de alta precisión utilizando Hugging Face Transformers · Utilizar las herramientas de código abierto de Hugging Face para automatizar tareas repetitivas · Comprender el concepto de distribuciones logit y sampling para optimizar las generaciones de modelos |
| Junior | Media | Utilizar las herramientas de código abierto de Hugging Face para automatizar tareas repetitivas · Crear y mantener modelos de inteligencia artificial de alta precisión utilizando Hugging Face Transformers · Comprender el concepto de MTP y cómo resolver problemas de configuración |
| Semi-Senior | Alta | Crear y mantener modelos de inteligencia artificial de alta precisión utilizando Hugging Face Transformers · Utilizar las herramientas de código abierto de Hugging Face para automatizar tareas repetitivas · Comprender el concepto de gemma4 y cómo utilizarlo para mejorar la calidad de los resultados |
| Senior | Alta | Crear y mantener modelos de inteligencia artificial de alta precisión utilizando Hugging Face Transformers · Utilizar las herramientas de código abierto de Hugging Face para automatizar tareas repetitivas · Comprender el concepto de MTP y cómo resolver problemas de configuración |
| Ingeniero de Software | Alta | Crear y mantener modelos de inteligencia artificial de alta precisión utilizando Hugging Face Transformers · Utilizar las herramientas de código abierto de Hugging Face para automatizar tareas repetitivas · Comprender el concepto de MTP y cómo resolver problemas de configuración |
| Ingeniero en Redes | Alta | Crear y mantener modelos de inteligencia artificial de alta precisión utilizando Hugging Face Transformers · Utilizar las herramientas de código abierto de Hugging Face para automatizar tareas repetitivas · Comprender el concepto de MTP y cómo resolver problemas de configuración |
| DevOps / SRE | Alta | Crear y mantener modelos de inteligencia artificial de alta precisión utilizando Hugging Face Transformers · Utilizar las herramientas de código abierto de Hugging Face para automatizar tareas repetitivas · Comprender el concepto de MTP y cómo resolver problemas de configuración |
| Ciberseguridad | Alta | Crear y mantener modelos de inteligencia artificial de alta precisión utilizando Hugging Face Transformers · Utilizar las herramientas de código abierto de Hugging Face para automatizar tareas repetitivas · Comprender el concepto de MTP y cómo resolver problemas de configuración |


## Información técnica ⚒️

- **Versión:** v5.15.1
- **Fecha de lanzamiento:** 2023-02-20
- **Requisitos:** Python 3.8+, TensorFlow 2.4+, PyTorch 1.9+, CUDA 11.0+
- **Cambios incompatibles:** Resolución del desequilibrio de token de candidato con la configuración de dispositivo "auto"

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **DFlash** — confianza: high
- **Generadores candidatos** — confianza: medium
- **Filtro Lanczos** — confianza: medium
- **Configuración de MTP** — confianza: medium
- **Distribuciones logit** — confianza: medium
- **Video a dispositivo** — confianza: medium

## Fuente original 📜

[https://github.com/huggingface/transformers/releases/tag/v5.15.1](https://github.com/huggingface/transformers/releases/tag/v5.15.1)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

# Patch release v5.15.1 This patch most notably solves a few issues with DFlash and MTP candidate generators, as well as an issue where images could sometimes not be processed on accelerator if using Lanczos filter. It contains the following commits: - Fix DFlash candidate token device mismatch with device_map="auto" (#47877) by @sywangyi and @Cyrilvallez - Align logit distributions for CandidateGenerators using sampling (#48007) by @Cyrilvallez - Fix MTP config when mlp_layer_types is absent (#48015) by @Cyrilvallez - Fallback from 'lanczos' to 'bicubic' when on cuda (#48026) by @zucchini-nlp - Fix gemma4 video to device (#47896) by @guarin

</details>

