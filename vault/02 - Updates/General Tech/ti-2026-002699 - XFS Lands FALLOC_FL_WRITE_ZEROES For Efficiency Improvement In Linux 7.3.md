---
type: update
id: ti-2026-002699
title: XFS Lands FALLOC_FL_WRITE_ZEROES For Efficiency Improvement In Linux 7.3
aliases:
- XFS Lands FALLOC_FL_WRITE_ZEROES For Efficiency Improvement In Linux 7.3
original_title: XFS Lands FALLOC_FL_WRITE_ZEROES For Efficiency Improvement In Linux
  7.3
company: ''
product: XFS
version: '7.3'
date: '2026-08-18'
created: '2026-08-18T09:35:33+00:00'
updated: '2026-08-18T21:24:39+00:00'
original_language: en
translated: true
importance: medium
impact: medium
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Phoronix
source_url: https://www.phoronix.com/news/XFS-FALLOC-FL-WRITE-ZEROES
source_type: rss
processed_by: openrouter
backend: opencodezen
model: nvidia/nemotron-3.5-lightning:free
insights: true
status: published
category: General Tech
subcategory: File System
confidence: medium
example: false
tags:
- xfs
- linux
- file-system
- kernel
- efficiency
alternatives:
- name: ext4
  confidence: high
- name: Btrfs
  confidence: medium
cssclasses:
- ti-note
---

# XFS Lands FALLOC_FL_WRITE_ZEROES For Efficiency Improvement In Linux 7.3

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟡 Media` · `🌐 Medio`

| Campo | Valor |
| --- | --- |
| Producto | **XFS** |
| Versión | 7.3 |

> [!abstract] Resumen
>
> - Se fusionaron mejoras del sistema de archivos **XFS** para el kernel **Linux 7.3**.
> - El cambio principal para usuarios finales es la adición de soporte para **FALLOC_FL_WRITE_ZEROES**.
> - Esta operación permite escribir ceros en un rango de archivo de forma eficiente sin asignar bloques físicos innecesarios.
> - Mejora el rendimiento y la eficiencia de espacio en cargas de trabajo que requieren inicializar regiones de archivos con ceros.
> - La funcionalidad fue integrada en la ventana de fusión (merge window) de Linux 7.3.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> XFS Llega FALLOC_FL_WRITE_ZEROES Para Mejora de Eficiencia En Linux 7.3
> 
> Las mejoras del sistema de archivos XFS han sido fusionadas para Linux 7.3. Para usuarios finales el único cambio notable para este sistema de archivos en el nuevo kernel es agregar soporte para FALLOC_FL_WRITE_ZEROES...

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Agrega soporte para FALLOC_FL_WRITE_ZEROES en sistema de archivos XFS
> - Mejora la eficiencia en el kernel Linux 7.3
> - Único cambio notable para usuarios finales en XFS para esta versión

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> XFS es un sistema de archivos de alto rendimiento diseñado para entornos Linux empresariales. Con la versión 7.3 del kernel, se incorpora soporte nativo para FALLOC_FL_WRITE_ZEROES, una bandera que permite escribir bloques ceros en archivos de manera eficiente. Esta mejora optimiza el manejo de espacio y rendimiento en operaciones de escritura masiva.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Esta funcionalidad permite a desarrolladores y sistemas gestionar eficientemente archivos esparsos y operaciones de truncado o expansión de archivos sin escribir datos reales. Facilita la creación de archivos de gran tamaño con bajo consumo de espacio físico, mejora pruebas de rendimiento y optimiza almacenamiento en aplicaciones que manejan grandes volúmenes de datos. Además, brinda nuevas herramientas de bajo nivel para ingeniería de sistemas y optimización de almacenamiento.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Baja | Concepto de banderas de archivo · Uso básico de fallocate · Impacto en espacio en disco |
| Junior | Media | Manejo de archivos esparsos en aplicaciones · Comandos fallocate --zero-range · Diferencia entre escritura y cero |
| Semi-Senior | Alta | Optimización de almacenamiento XFS · Implementación de caché de páginas cero · Ajuste de parámetros de asignación |
| Senior | Alta | Diseño de sistemas que aprovechen archivos esparsos · Perfilado de rendimiento de E/S · Configuración avanzada de kernel XFS |
| Ingeniero de Software | Alta | Gestión de E/S de bajo nivel en código · Control de archivos esparsos en almacenamiento · Compatibilidad con flags de kernel |
| DevOps / SRE | Alta | Optimización de uso de disco en producción · Monitoreo de eficiencia del sistema de archivos · Parámetros de kernel para escritura optimizada |


## Información técnica ⚒️

- **Versión:** 7.3

## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Alternativas 🔄

- **ext4** — confianza: high
- **Btrfs** — confianza: medium

## Fuente original 📜

[https://www.phoronix.com/news/XFS-FALLOC-FL-WRITE-ZEROES](https://www.phoronix.com/news/XFS-FALLOC-FL-WRITE-ZEROES)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

The XFS file-system improvements have been merged for Linux 7.3. For end-users the only notable change for this file-system on the new kernel is adding support for FALLOC_FL_WRITE_ZEROES...

</details>

