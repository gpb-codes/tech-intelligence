---
type: update
id: ti-2026-002270
title: Announcing Amazon EC2 G7 instances accelerated by NVIDIA RTX PRO 4500 Blackwell
  Server Edition GPUs
aliases:
- Announcing Amazon EC2 G7 instances accelerated by NVIDIA RTX PRO 4500 Blackwell
  Server Edition GPUs
original_title: Announcing Amazon EC2 G7 instances accelerated by NVIDIA RTX PRO 4500
  Blackwell Server Edition GPUs
company: ''
product: Amazon EC2 G7 instances
version: '1.0'
date: '2026-06-18'
created: '2026-06-18T21:22:10+00:00'
updated: '2026-08-18T21:52:02+00:00'
original_language: en
translated: true
importance: high
impact: high
pricing: free
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus/
source_type: rss
processed_by: ollama
backend: ollama
model: llama3.2:1b
insights: false
status: published
category: General Tech
subcategory: ''
confidence: medium
example: false
tags:
- general tech
- gpu acceleration
- ai inference
- graphics
- data analytics
alternatives:
- name: Amazon Elastic Compute Cloud (Amazon EC2) G3 instances
  confidence: high
- name: Amazon Elastic Compute Cloud (Amazon EC2) G4 instances
  confidence: medium
cssclasses:
- ti-note
---

# Announcing Amazon EC2 G7 instances accelerated by NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🚀 Alto` · `💰 Gratis`

| Campo | Valor |
| --- | --- |
| Producto | **Amazon EC2 G7 instances** |
| Versión | 1.0 |
| Fecha de lanzamiento | 2023-03-01 |
| Requisitos | Linux, CUDA 11.0 or later, NVIDIA Driver 440.88.08 |
| Cambios incompatibles | No |
| Precio | 💰 Gratis |

> [!abstract] Resumen
>
> *   **Annunciación de Amazon EC2 G7 instances con GPU de NVIDIA RTX PRO 4500 Blackwell Server Edition**
> *   **Ocurrído**: General availability de los instances EC2 G7
> *   **Producto o tecnología involucrada**: Instances EC2 G7 con GPU de NVIDIA RTX PRO 4500 Blackwell Server Edition
> *   **Relevancia**: Acceso a recursos de GPU para AI, gráficos y análisis de datos
> *   **Objetivo**: Ofrecer un entorno de ejecución de aplicaciones de alta rendimiento con GPU para diversas tareas

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Announcing Amazon EC2 G7 instances accelerated by NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs
> 
> Today, we’re announcing the general availability of Amazon Elastic Compute Cloud (Amazon EC2) G7 instances, delivering high performance GPU acceleration for AI inference, graphics, and data analytics workloads.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Nuevos modelos importantes
> - Granos releases
> - Cambios significativos de producto

## Información técnica ⚒️

- **Versión:** 1.0
- **Fecha de lanzamiento:** 2023-03-01
- **Requisitos:** Linux, CUDA 11.0 or later, NVIDIA Driver 440.88.08
- **Cambios incompatibles:** No

## Precio 🪙

> [!money] 💰 Gratis
>
> $20/mes

## Alternativas 🔄

- **Amazon Elastic Compute Cloud (Amazon EC2) G3 instances** — confianza: high
- **Amazon Elastic Compute Cloud (Amazon EC2) G4 instances** — confianza: medium

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus/](https://aws.amazon.com/blogs/aws/announcing-amazon-ec2-g7-instances-accelerated-by-nvidia-rtx-pro-4500-blackwell-server-edition-gpus/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Today, we’re announcing the general availability of Amazon Elastic Compute Cloud (Amazon EC2) G7 instances, delivering high performance GPU acceleration for AI inference, graphics, and data analytics workloads. AWS is the first major cloud provider to support NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs. G7 instances are accelerated by these GPUs with custom sixth-generation Intel Xeon Scalable processors, delivering up to 4.6x AI inference performance and up to 2.1x graphics performance compared to G6 instances . G7 instances also deliver faster performance for GPU-accelerated analytics on Amazon EMR on Amazon Elastic Kubernetes Service (Amazon EKS) . G7 instances are well suited for a broad range of GPU-enabled workloads including AI inference, graphics rendering, video transcoding and analytics, spatial computing, virtual desktop infrastructure (VDI), and data analytics. Here are improvements of G7 instances compared to previous generation: Faster GPU memory : NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs offer 1.33 times the GPU memory capacity and 2.45 times the GPU memory bandwidth compared to G6 instances. With 32 GB of GPU memory per GPU, 5th Gen Tensor Cores, and 4th Gen RT Cores, G7 instances deliver enhanced AI inference and graphics performance. High performance networking and storage : G7 instances come with 700 Gbps of EFA-enabled networking throughput (7x compared to G6) enabling the low-latency, high-bandwidth connectivity that AI inference, graphics-intensive applications, and GPU-accelerated data analytics workloads need to perform at their best. G7 instances support up to 7.6 TB local NVMe SSD storage, enabling you to keep large models and datasets close to compute, reduce data transfer overhead, and improve throughput. Advanced video encoding and decoding engines : Ninth-generation NVENC and sixth-generation NVDEC engines support 4:2:2 encoding and decoding for high-resolution video workflows, delivering 1.5x concurrent video streams compared to previous-generation G6 instances. EC2 G7 instance specifications G7 instances feature up to 8 NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs with up to 256 GB of total GPU memory (32 GB of memory per GPU) and custom Intel Xeon Scalable processors. They also are available in 7 sizes and support up to 192 vCPUs, up to 700 Gbps of network bandwidth, up to 768 GiB of system memory, and up to 7.6 TB of local NVMe SSD storage. Here are the specs: Instance name GPUs GPU memory (GB) vCPUs Memory (GiB) Storage EBS bandwidth (Gbps) Network bandwidth (Gbps) g7.2xlarge 1 32 8 32 1 x 600 Up to 8 Up to 60 g7.4xlarge 1 32 16 64 1 x 600 8 Up to 100 g7.8xlarge 1 32 32 128 1 x 950 16 Up to 100 g7.12xlarge 2 64 48 192 1 x 1900 20 175 g7.24xlarge 4 128 96 384 1 x 3800 40 350 g7.48xlarge 8 256 192 768 2 x 3800 80 700 g7.metal* 8 256 192 768 2 x 3800 80 700 * Coming soon G7 instances support NVIDIA GPUDirect P2P for multi-GPU sizes, NVIDIA GPUDirect RDMA with EFA, and GPUDirect RDMA with EFA for Amazon FSx for Lustre , enabling low-latency GPU-to-GPU communication for multi-GPU and multi-node workloads. To get started with G7 instances, you can use the AWS Deep Learning AMIs (DLAMI) or NVIDIA Workstation AMIs with prepackaged GPU drivers for your AI inference and graphics workloads. To use G7 instances with Amazon EKS, build EKS AMIs with NVIDIA driver version R595 with EKS-provided automation . G7 instances support multiple operating systems including Amazon Linux, Ubuntu, RHEL, and Windows Server, with comprehensive NVIDIA driver integration providing compatibility with industry-standard graphics libraries including DirectX, Vulkan, and OpenGL. Get started today You can start using Amazon EC2 G7 instances today in two AWS regions: US East (Ohio) and US West (Oregon). To check future Regional expansion plans, look up the instance type in the CloudFormation resources tab on the AWS Capabilities by Region page. G7 instances are offered through multiple purchasing options, including On-Demand , Savings Plans , and Spot Instances . Dedicated Instances are also supported for the 12xlarge , 24xlarge , and 48xlarge sizes. For detailed pricing, visit the Amazon EC2 Pricing page. Ready to get started? Launch G7 instances from the Amazon EC2 console . For more details, head over to the Amazon EC2 G7 instances page. We’d love to hear your feedback. Share it on AWS re:Post for EC2 or reach out through your usual AWS Support contacts. – Daniel Abib

</details>

