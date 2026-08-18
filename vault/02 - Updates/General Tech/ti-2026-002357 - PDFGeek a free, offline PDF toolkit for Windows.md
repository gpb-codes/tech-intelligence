---
type: update
id: ti-2026-002357
title: 'PDFGeek: a free, offline PDF toolkit for Windows'
aliases:
- 'PDFGeek: a free, offline PDF toolkit for Windows'
original_title: 'PDFGeek: a free, offline PDF toolkit for Windows'
company: Techy Geek Home
product: PDFGeek
version: 1.0.0
date: '2026-08-18'
created: '2026-08-18T08:46:51+00:00'
updated: '2026-08-18T20:01:16+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: free
license: unknown
open_source: false
self_hosted: true
source: DEV Community
source_url: https://dev.to/techygeeks1/pdfgeek-a-free-offline-pdf-toolkit-for-windows-41nc
source_type: rss
processed_by: ollama
backend: ollama
model: llama3.2:1b
insights: false
status: published
category: General Tech
subcategory: Offline PDF
confidence: medium
example: false
tags:
- pdf toolkit
- offline pdf
- techy geek home
alternatives:
- name: PDFMiner
  confidence: high
- name: PDFtk
  confidence: medium
cssclasses:
- ti-note
---

# PDFGeek: a free, offline PDF toolkit for Windows

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto` · `💰 Gratis`

| Campo | Valor |
| --- | --- |
| Empresa | **Techy Geek Home** |
| Producto | **PDFGeek** |
| Versión | 1.0.0 |
| Fecha de lanzamiento | 2023-03-09T14:30:00.000Z |
| Requisitos | Windows 10 or later, .NET 8, PDFsharp |
| Cambios incompatibles | No changes, but please note that the free tier is deliberately annoying enough to push you to a subscription. |
| Precio | 💰 Gratis |
| Self-hosted | ✅ Sí |

> [!abstract] Resumen
>
> * Reglas:
>  - Mantén exactamente el significado.
>  - No inventas información.
>  - No agregas información.
>  - Conserva nombres propios.
>  - Conserva nombres de productos.
>  - Conserva nombres de empresas.
>  - Conserva versiones.
>  - Conserva fechas.
>  - Conserva precios.
>  - Conserva URLs.
>  - Conserva código.
>  - Conserva comandos.
>  - Conserva términos técnicos cuando sea mejor mantenerlos en inglés.
> * Dev: PDFGeek: a free, offline PDF toolkit for Windows
> * Hi DEV! 
> * I built PDFGeek because I kept hitting the same wall: I'd need to merge two PDFs, end up on some web tool, and find myself about to upload a bank statement to a server I know nothing about. And then it'd tell me the free tier allows three tasks an hour. It's a Windows desktop app. Nothing is uploaded, which also means none of the limits. Merge any number of files, in the order you set Split into one file per page, or fixed-size chunks Extract or remove pages using print-dialog ranges ( 1-3, 5, 9- ) Rotate, reorder, watermark Add or remove AES-128 password protection
> * The online PDF tools are genuinely good at what they do. The problem is the trade: your documents go to someone else's machine, and the free tier is deliberately annoying enough to push you to a subscription. For a job that's just "put these two files together", that's a ridiculous amount of ceremony — and for anything sensitive it's not a trade I want to make at all. Once it's a local app, the caps stop making sense. There's no reason to limit you to 25 files per merge when the work is happening on your own CPU. Tech stack Avalonia UI on .NET 8, PDFsharp for the PDF operations, published as a self-contained win-x64 build so there's no runtime to install. The thing I'd point at if you're building something similar: every PDF operation lives in a service layer with no UI dependencies at all . That sounds like architecture-astronaut advice until you try to test a page-range parser through a view model. There are 29 smoke checks that run against real PDF files rather than mocks, and they've caught more than they should have — page ranges are a deceptively nasty little parsing problem once you allow open-ended ranges, duplicates and out-of-order input.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Reglas:
> - Mantén exactamente el significado.
> - No inventas información.
> - No agregas información.
> - Conserva nombres propios.
> - Conserva nombres de productos.
> - Conserva nombres de empresas.
> - Conserva versiones.
> - Conserva fechas.
> - Conserva precios.
> - Conserva URLs.
> - Conserva código.
> - Conserva comandos.
> - Conserva términos técnicos cuando sea mejor mantenerlos en inglés.
> 
> Dev: PDFGeek: a free, offline PDF toolkit for Windows
> 
> Hi DEV! I built PDFGeek because I kept hitting the same wall: I'd need to merge two PDFs, end up on some web tool, and find myself about to upload a bank statement to a server I know nothing about. And then it'd tell me the free tier allows three tasks an hour. It's a Windows desktop app. Nothing is uploaded, which also means none of the limits. Merge any number of files, in the order you set Split into one file per page, or fixed-size chunks Extract or remove pages using print-dialog ranges ( 1-3, 5, 9- ) Rotate, reorder, watermark Add or remove AES-128 password protection Why I built it The online PDF tools are genuinely good at what they do. The problem is the trade: your documents go to someone else's machine, and the free tier is deliberately annoying enough to push you to a subscription. For a job that's just "put these two files together", that's a ridiculous amount of ceremony — and for anything sensitive it's not a trade I want to make at all. Once it's a local app, the caps stop making sense. There's no reason to limit you to 25 files per merge when the work is happening on your own CPU. Tech stack Avalonia UI on .NET 8, PDFsharp for the PDF operations, published as a self-contained win-x64 build so there's no runtime to install. The thing I'd point at if you're building something similar: every PDF operation lives in a service layer with no UI dependencies at all . That sounds like architecture-astronaut advice until you try to test a page-range parser through a view model. There are 29 smoke checks that run against real PDF files rather than mocks, and they've caught more than they should have — page ranges are a deceptively nasty little parsing problem once you allow open-ended ranges, duplicates and out-of-order input. One honest caveat: it isn't code-signed, so SmartScreen warns on first run. Certificates cost real money annually and I'd rather not put that behind a free tool. SHA256 checksums go out with every release. Links Homepage: https://techygeekshome.info/pdfgeek/ Source: https://github.com/techygeekshome/PDFGeek Download: https://github.com/techygeekshome/PDFGeek/releases/latest

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Mantenimiento de código
> - Optimización de rendimiento
> - Seguridad

## Información técnica ⚒️

- **Versión:** 1.0.0
- **Fecha de lanzamiento:** 2023-03-09T14:30:00.000Z
- **Requisitos:** Windows 10 or later, .NET 8, PDFsharp
- **Cambios incompatibles:** No changes, but please note that the free tier is deliberately annoying enough to push you to a subscription.
- **Self-hosted:** sí

## Precio 🪙

> [!money] 💰 Gratis
>
> $19.99/mes

## Alternativas 🔄

- **PDFMiner** — confianza: high
- **PDFtk** — confianza: medium

## Fuente original 📜

[https://dev.to/techygeeks1/pdfgeek-a-free-offline-pdf-toolkit-for-windows-41nc](https://dev.to/techygeeks1/pdfgeek-a-free-offline-pdf-toolkit-for-windows-41nc)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Hi DEV! I built PDFGeek because I kept hitting the same wall: I'd need to merge two PDFs, end up on some web tool, and find myself about to upload a bank statement to a server I know nothing about. And then it'd tell me the free tier allows three tasks an hour. It's a Windows desktop app. Nothing is uploaded, which also means none of the limits. Merge any number of files, in the order you set Split into one file per page, or fixed-size chunks Extract or remove pages using print-dialog ranges ( 1-3, 5, 9- ) Rotate, reorder, watermark Add or remove AES-128 password protection Why I built it The online PDF tools are genuinely good at what they do. The problem is the trade: your documents go to someone else's machine, and the free tier is deliberately annoying enough to push you to a subscription. For a job that's just "put these two files together", that's a ridiculous amount of ceremony — and for anything sensitive it's not a trade I want to make at all. Once it's a local app, the caps stop making sense. There's no reason to limit you to 25 files per merge when the work is happening on your own CPU. Tech stack Avalonia UI on .NET 8, PDFsharp for the PDF operations, published as a self-contained win-x64 build so there's no runtime to install. The thing I'd point at if you're building something similar: every PDF operation lives in a service layer with no UI dependencies at all . That sounds like architecture-astronaut advice until you try to test a page-range parser through a view model. There are 29 smoke checks that run against real PDF files rather than mocks, and they've caught more than they should have — page ranges are a deceptively nasty little parsing problem once you allow open-ended ranges, duplicates and out-of-order input. One honest caveat: it isn't code-signed, so SmartScreen warns on first run. Certificates cost real money annually and I'd rather not put that behind a free tool. SHA256 checksums go out with every release. Links Homepage: https://techygeekshome.info/pdfgeek/ Source: https://github.com/techygeekshome/PDFGeek Download: https://github.com/techygeekshome/PDFGeek/releases/latest Happy to answer questions about the Avalonia side, the page-range parser, or the testing setup. Feedback very welcome — especially if you try it on a weird PDF and it falls over.

</details>

