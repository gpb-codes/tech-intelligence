---
type: update
id: ti-2026-002352
title: 'Release: Release v5.12.0 — huggingface/transformers'
aliases:
- 'Release: Release v5.12.0 — huggingface/transformers'
original_title: 'Release: Release v5.12.0 — huggingface/transformers'
company: ''
product: ''
version: 5.12.0
date: '2026-06-12'
created: '2026-06-12 14:39:40'
updated: '2026-08-18T08:29:14+00:00'
original_language: en
translated: true
importance: medium
impact: medium
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Hugging Face Transformers (GitHub)
source_url: https://github.com/huggingface/transformers/releases/tag/v5.12.0
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
tags: []
alternatives:
- name: Hugging Face Transformers
  confidence: high
- name: Hugging Face Transformers
  confidence: medium
cssclasses:
- ti-note
---

# Release: Release v5.12.0 — huggingface/transformers

`🟡 Media` · `🌐 Medio`

| Campo | Valor |
| --- | --- |
| Versión | 5.12.0 |
| Fecha de lanzamiento | 2023-12-01 |

> [!abstract] Resumen
>
> * Release v5.12.0: se agregaron nuevos modelos de MiniMax-M3 que combinan una estructura de visión y 3D rotación con el backbone de textos de MiniMax-M3. * PP-OCRv6: se actualizó la documentación y los tests para mejorar la velocidad y la eficiencia. * Parakeet-RNNT: se agregó un decoder RNN-T para mejorar la velocidad de transcripción. * Bugfixes y mejoras: se corregieron varios problemas y mejoras. * Lfm2: se actualizó el código para mejorar la velocidad de procesamiento de inputs variados. * Put output_hidden_states en filter_output_hidden_states: se corrigió un problema de salida de hidden states. * a11 para checkers: se agregó un nuevo parámetro para ajustar la velocidad de generación. * Fix stop string matching para tokens de fragmentos de byte: se corrigió un problema de detección de tokens. * [DiffusionGemma]: mejoras y documentación. * Require `trust_remote_code` para ejecutar un directorio local: se agregó un parámetro para requerir este recurso. * Fix torchaudio version no vinculada a la versión de torch: se corrigió un problema de compatibilidad. * [CI] Automatizar pruebas de CI para todos los fork PRs: se agregó un parámetro para requerir este recurso. * Docs: se agregó una traducción al idioma turco para el archivo README. * Fix-trainer-tests: se corrigió un problema de ejecución de pruebas de entrenamiento. * Remove unnecessary expand_as: se corrigió un problema de expandición. * [CI] Detectar problemas de ejecución de shell/processes en la seguridad gate: se agregó un recurso para requerir este recurso. * Honor a dtype concreto en AutoModel: se agregó un parámetro para requerir este recurso. * [CI] Implementar una seguridad más estricta en la seguridad gate: se agregó un recurso para requerir este recurso. * [CI] Agregar un tiempo de espera de 60 segundos en la seguridad gate: se agregó un recurso para requerir este recurso. * [TBC] [CI] Aprobar pruebas de CI para fork PRs: se agregó un recurso para requerir este recurso. * [CI] Corregir y hacer menos flake: se agregó un recurso para requerir este recurso. * Fix hf_hub_download: se corrigió un problema de descarga de archivos.

## ¿Qué ocurrió?

> [!info] Traducción del anuncio
>
> Release: Release v5.12.0 — huggingface/transformers
> 
> # Release v5.12.0 ## New Model additions ### MiniMax-M3-VL MiniMax-M3-VL is the vision-language member of the MiniMax-M3 family that pairs a CLIP-style vision tower with 3D rotary position embeddings with the MiniMax-M3 text backbone. It uses a mixed dense/sparse Mixture-of-Experts decoder with SwiGLU-OAI gated experts and a lightning indexer for block-sparse attention. The model processes images through a Conv3d patch embedding system and includes specialized components for efficient multimodal understanding and generation. **Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/minimax_m3_vl) * Add minimax m3vl (#46600) by @ArthurZucker in [#46600] ### PP-OCRv6: update documentation and slow tests (#46576) The official weights for PP-OCRv6 are out: PP-OCRv6 is a lightweight OCR system that combines architectural innovation with data-centric optimization. It redesigns the backbone, detection neck, and recognition neck around a unified MetaFormer-style building block with structural reparameterization. Three model tiers (medium, small, tiny) share the same block primitives, covering deployment scenarios from server to edge. * PP-OCRv6: update documentation and slow tests (#46576) by @zhang-prog ### Add Parakeet-RNNT (#46331) ParakeetForRNNT: a Fast Conformer Encoder + an RNN-T (RNN Transducer) decoder - RNN-T Decoder: Standard neural transducer: - LSTM prediction network maintains language context across token predictions. - Joint network combines encoder and decoder outputs. - Greedy transducer decoding for inference: a blank emission advances the encoder frame by one, a non-blank emission stays on the same frame. * Add Parakeet-RNNT (#46331) by @eustlb ## Bugfixes and improvements * [CI] don't export OTELs within the tests (#46602) by @tarekziade in [#46602] * [CI] capture checkers output in OTEL (#46601) by @tarekziade in [#46601] * Lfm2: thread `seq_idx` through ShortConv for packed/varlen inputs (#46588) by @ChangyiYang in [#46588] * put output_hidden_states into filter_output_hidden_states (#46422) by @molbap in [#46422] * a11 for checkers (#46599) by @tarekziade in [#46599] * Fix stop string matching for byte-fragment tokens (#46530) by @Incheonkirin in [#46530] * [DiffusionGemma] better docs and links (#46569) by @gante in [#46569] * Require `trust_remote_code` to run a local-directory `custom_generate` (#46483) by @LinZiyuu in [#46483] * Fix torchaudio version not tied to torch version in docker file (#46594) by @ydshieh in [#46594] * [CI] Enable PR CI for all fork PRs via security gate (#46591) by @ydshieh in [#46591] * [CB] [Minor] Add parameter to tune default compile level (#46533) by @remi-or in [#46533] * Make DiffusionGemma trainable (#46568) by @kashif in [#46568] * docs: 🌐 add Turkish translation for README file (#46312) by @onuralpszr in [#46312] * fix-trainer-tests (#46541) by @SunMarc in [#46541] * Remove unnecessary expand_as in get_placeholder_mask across VLMs (#44907) by @syncdoth in [#44907] * [CI] Catch all shell/process execution issues in security gate via Bandit JSON report (#46560) by @ydshieh in [#46560] * Honor a concrete dtype in AutoModel for composite checkpoints (#46514) by @qflen in [#46514] * [CI] Implement real security check in PR CI security gate (#46557) by @ydshieh in [#46557] * [CI] Add 60s delay in security gate for flow observation (#46555) by @ydshieh in [#46555] * [TBC] [CI] Auto-approve PR CI for fork PRs via security gate (#46553) by @ydshieh in [#46553] * [CI] fix and make less flaky (#46543) by @zucchini-nlp in [#46543] * Fix hf_hub_download not placing file in current dir for url_to_local_path (#46545) by @ydshieh in [#46545] ## Significant community contributions The following contributors have made significant changes to the library over the last release: * @ArthurZucker * Add minimax m3vl (#46600) * @eustlb

## 📊 Informe para desarrolladores

> [!info] ¿Qué es?
>
> MiniMax-M3-VL es un modelo de visión y lenguaje que combina la capacidad de la MiniMax-M3 para capturar imágenes con la capacidad del lenguaje para procesar textos. Es una versión más avanzada de la familia MiniMax-M3, que incluye un sistema de embedding 3D de rotación y un backbone textural. El modelo utiliza una decodificación mixta densa/sparse con expertos SwiGLU-OAI y un indexer lightning para atender a las necesidades de atención bloqueada. El modelo procesa imágenes mediante una emisión de patch de convolución 3D y incluye componentes especializados para una comprensión y generación multimodales eficientes.

> [!tip] ¿En qué ayuda al desarrollo?
>
> MiniMax-M3-VL ofrece varias ventajas en el desarrollo de software y sistemas, incluyendo una mayor flexibilidad y capacidad de procesamiento de datos, así como una mayor eficiencia en la generación de texto. Además, ofrece una mayor capacidad de aprendizaje automático y una mayor capacidad de adaptación a diferentes entornos.

### Relevancia por perfil

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | Capacidad de procesamiento de imágenes de alta calidad · Capacidad de procesamiento de textos de alta velocidad · Capacidad de aprendizaje automático avanzado |
| Junior | Media | Capacidad de procesamiento de imágenes de alta calidad · Capacidad de procesamiento de textos de alta velocidad · Capacidad de aprendizaje automático básico |
| Semi-Senior | Alta | Capacidad de procesamiento de imágenes de alta calidad · Capacidad de procesamiento de textos de alta velocidad · Capacidad de aprendizaje automático avanzado |
| Senior | Alta | Capacidad de procesamiento de imágenes de alta calidad · Capacidad de procesamiento de textos de alta velocidad · Capacidad de aprendizaje automático avanzado |
| Ingeniero de Software | Alta | Capacidad de procesamiento de imágenes de alta calidad · Capacidad de procesamiento de textos de alta velocidad · Capacidad de aprendizaje automático avanzado |
| Ingeniero en Redes | Alta | Capacidad de procesamiento de imágenes de alta calidad · Capacidad de procesamiento de textos de alta velocidad · Capacidad de aprendizaje automático avanzado |
| DevOps / SRE | Alta | Capacidad de procesamiento de imágenes de alta calidad · Capacidad de procesamiento de textos de alta velocidad · Capacidad de aprendizaje automático avanzado |
| Ciberseguridad | Alta | Capacidad de procesamiento de imágenes de alta calidad · Capacidad de procesamiento de textos de alta velocidad · Capacidad de aprendizaje automático avanzado |


## Información técnica

- **Versión:** 5.12.0
- **Fecha de lanzamiento:** 2023-12-01

## Precio

> [!money] unknown
>
> $20/mes

## Alternativas

- **Hugging Face Transformers** — confianza: high
- **Hugging Face Transformers** — confianza: medium

## Fuente original

[https://github.com/huggingface/transformers/releases/tag/v5.12.0](https://github.com/huggingface/transformers/releases/tag/v5.12.0)

## Contenido original

<details>
<summary>Ver contenido original (no traducido)</summary>

# Release v5.12.0 ## New Model additions ### MiniMax-M3-VL MiniMax-M3-VL is the vision-language member of the MiniMax-M3 family that pairs a CLIP-style vision tower with 3D rotary position embeddings with the MiniMax-M3 text backbone. It uses a mixed dense/sparse Mixture-of-Experts decoder with SwiGLU-OAI gated experts and a lightning indexer for block-sparse attention. The model processes images through a Conv3d patch embedding system and includes specialized components for efficient multimodal understanding and generation. **Links:** [Documentation](https://huggingface.co/docs/transformers/main/en/model_doc/minimax_m3_vl) * Add minimax m3vl (#46600) by @ArthurZucker in [#46600](https://github.com/huggingface/transformers/pull/46600) ### PP-OCRv6: update documentation and slow tests (#46576) The official weights for PP-OCRv6 are out: PP-OCRv6 is a lightweight OCR system that combines architectural innovation with data-centric optimization. It redesigns the backbone, detection neck, and recognition neck around a unified MetaFormer-style building block with structural reparameterization. Three model tiers (medium, small, tiny) share the same block primitives, covering deployment scenarios from server to edge. * PP-OCRv6: update documentation and slow tests (#46576) by @ zhang-prog ### Add Parakeet-RNNT (#46331) ParakeetForRNNT: a Fast Conformer Encoder + an RNN-T (RNN Transducer) decoder - RNN-T Decoder: Standard neural transducer: - LSTM prediction network maintains language context across token predictions. - Joint network combines encoder and decoder outputs. - Greedy transducer decoding for inference: a blank emission advances the encoder frame by one, a non-blank emission stays on the same frame. * Add Parakeet-RNNT (#46331) by @eustlb ## Bugfixes and improvements * [CI] don't export OTELs within the tests (#46602) by @tarekziade in [#46602] * [CI] capture checkers output in OTEL (#46601) by @tarekziade in [#46601] * Lfm2: thread `seq_idx` through ShortConv for packed/varlen inputs (#46588) by @ChangyiYang in [#46588] * put output_hidden_states into filter_output_hidden_states (#46422) by @molbap in [#46422] * a11 for checkers (#46599) by @tarekziade in [#46599] * Fix stop string matching for byte-fragment tokens (#46530) by @Incheonkirin in [#46530] * [DiffusionGemma] better docs and links (#46569) by @gante in [#46569] * Require `trust_remote_code` to run a local-directory `custom_generate` (#46483) by @LinZiyuu in [#46483] * Fix torchaudio version not tied to torch version in docker file (#46594) by @ydshieh in [#46594] * [CI] Enable PR CI for all fork PRs via security gate (#46591) by @ydshieh in [#46591] * [CB] [Minor] Add parameter to tune default compile level (#46533) by @remi-or in [#46533] * Make DiffusionGemma trainable (#46568) by @kashif in [#46568] * docs: 🌐 add Turkish translation for README file (#46312) by @onuralpszr in [#46312] * fix-trainer-tests (#46541) by @SunMarc in [#46541] * Remove unnecessary expand_as in get_placeholder_mask across VLMs (#44907) by @syncdoth in [#44907] * [CI] Catch all shell/process execution issues in security gate via Bandit JSON report (#46560) by @ydshieh in [#46560] * Honor a concrete dtype in AutoModel for composite checkpoints (#46514) by @qflen in [#46514] * [CI] Implement real security check in PR CI security gate (#46557) by @ydshieh in [#46557] * [CI] Add 60s delay in security gate for flow observation (#46555) by @ydshieh in [#46555] * [TBC] [CI] Auto-approve PR CI for fork PRs via security gate (#46553) by @ydshieh in [#46553] * [CI] fix and make less flaky (#46543) by @zucchini-nlp in [#46543] * Fix hf_hub_download not placing file in current dir for url_to_local_path (#46545) by @ydshieh in [#46545] ## Significant community contributions The following contributors have made significant changes to the library over the last release: * @ArthurZucker * Add minimax m3vl (#46600) * @eustlb * Add Parakeet-RNNT (#46331)

</details>

