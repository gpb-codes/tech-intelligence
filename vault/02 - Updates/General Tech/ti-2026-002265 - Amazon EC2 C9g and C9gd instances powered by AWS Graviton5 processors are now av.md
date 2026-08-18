---
type: update
id: ti-2026-002265
title: Amazon EC2 C9g and C9gd instances powered by AWS Graviton5 processors are now
  available
aliases:
- Amazon EC2 C9g and C9gd instances powered by AWS Graviton5 processors are now available
original_title: Amazon EC2 C9g and C9gd instances powered by AWS Graviton5 processors
  are now available
company: ''
product: Amazon EC2 C9g y C9gd instancias
version: ''
date: '2026-06-30'
created: '2026-06-30T20:56:44+00:00'
updated: '2026-08-18T22:02:25+00:00'
original_language: en
translated: true
importance: high
impact: medium
pricing: free
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/amazon-ec2-c9g-and-c9gd-instances-powered-by-aws-graviton5-processors-are-now-available/
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
- ec2
- amazon
- cloud
- general tech
alternatives:
- name: Amazon EC2 C5g
  confidence: high
- name: Amazon EC2 C5gd
  confidence: medium
cssclasses:
- ti-note
---

# Amazon EC2 C9g and C9gd instances powered by AWS Graviton5 processors are now available

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🌐 Medio` · `💰 Gratis`

| Campo | Valor |
| --- | --- |
| Producto | **Amazon EC2 C9g y C9gd instancias** |
| Precio | 💰 Gratis |

> [!abstract] Resumen
>
> * Amazon EC2 C9g y C9gd instancias están disponibles para el uso general.
> * Estas instancias están diseñadas para ofrecer un rendimiento superior en comparación con las instancias C8g anteriores.
> * Un aumento del 25% en la velocidad de procesamiento por vCPU.
> * Un mayor acceso a memoria.
> * Una mayor velocidad de transferencia de datos.
> * Estas instancias están equipadas con el procesador Graviton5.
> * Ofrece una velocidad de memoria la más rápida de cualquier procesador instanciado en el cloud.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Amazon EC2 C9g y C9gd instancias están disponibles para el uso general. Estas instancias están diseñadas para ofrecer un rendimiento superior en comparación con las instancias C8g anteriores, con un aumento del 25% en la velocidad de procesamiento por vCPU y un mayor acceso a memoria, así como una mayor velocidad de transferencia de datos. Estas instancias están equipadas con el procesador Graviton5, que ofrece una velocidad de memoria la más rápida de cualquier procesador instanciado en el cloud, con DIMMs DDR5 8800MT/s, 5 veces más caché L3 y hasta 3 veces más rendimiento de procesamiento de packets.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Nuevos modelos importantes
> - Granos releases
> - Cambios significativos de producto

## Precio 🪙

> [!money] 💰 Gratis

## Alternativas 🔄

- **Amazon EC2 C5g** — confianza: high
- **Amazon EC2 C5gd** — confianza: medium

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/amazon-ec2-c9g-and-c9gd-instances-powered-by-aws-graviton5-processors-are-now-available/](https://aws.amazon.com/blogs/aws/amazon-ec2-c9g-and-c9gd-instances-powered-by-aws-graviton5-processors-are-now-available/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

When you run compute-intensive workloads like real-time analytics, batch processing, video encoding, scientific modeling, or CPU-based machine learning inference, every percentage point of performance matters. You need instances that deliver higher throughput per vCPU, faster memory access, and more network bandwidth, all while keeping your costs in check. Today I am happy to announce the general availability of Amazon Elastic Compute Cloud (Amazon EC2) C9g and C9gd instances, powered by AWS Graviton5 processors. C9g instances are compute-optimized and deliver up to 25% higher performance per vCPU compared to previous-generation C8g instances. They feature the fastest memory of any processor instance in the cloud, with DDR5 8800MT/s DIMMs, 5x more L3 cache, and up to 3x higher packet-processing performance compared to Graviton4-based instances. The faster memory and larger caches mean your workloads spend less time waiting on data, translating into higher throughput for in-memory analytics, faster agentic loops, and more responsive real-time applications. C9g instances are ideal for batch jobs, video encoding pipelines, or distributed analytics that can utilize Amazon Elastic Block Store (Amazon EBS) for storage. It is also a natural fit for agentic AI workloads, where concurrent environments and CPU-bound reasoning steps benefit from Graviton5’s higher core count and larger caches. As AI shifts from answering questions to taking actions, running code, and orchestrating multi-step tasks, the demand for CPU compute is growing, and C9g instances are built for this shift. Some workloads also need fast local storage alongside that compute power. Choose C9gd when your application benefits from high-speed, low-latency local NVMe SSD storage, for example scratch space during HPC simulations, temporary caches for ML inference, or local buffers for ad-serving engines. Graviton5-based instances with NVMe instance store volumes also support detailed performance statistics, providing high-resolution I/O metrics, including latency histograms broken down by I/O size, up to 1-second granularity and accessible via Amazon CloudWatch or nvme-cli at no additional cost. C9g and C9gd instances at a glance C9g and C9gd instances are available in 11 sizes ranging from medium to 48xlarge, plus a bare metal option. They offer up to 15% higher network bandwidth and 20% higher EBS bandwidth on average across sizes compared to the previous generation, with the largest 48xlarge size delivering up to 100 Gbps of network bandwidth and up to 72 Gbps of EBS bandwidth, a 2x increase. C9g vCPUs Memory (GiB) Network Bandwidth (Gbps) EBS Bandwidth (Gbps) medium 1 2 Up to 15 Up to 12 large 2 4 Up to 15 Up to 12 xlarge 4 8 Up to 15 Up to 12 2xlarge 8 16 Up to 17 Up to 12 4xlarge 16 32 Up to 17 Up to 12 8xlarge 32 64 17 12 12xlarge 48 96 25 18 16xlarge 64 128 34 24 24xlarge 96 192 50 36 48xlarge 192 384 100 72 metal-48xl 192 384 100 72 C9gd instances add local NVMe SSD storage with up to 30% higher storage performance compared to previous-generation local storage instances. C9gd vCPUs Memory (GiB) Instance Storage (GB) Network Bandwidth (Gbps) EBS Bandwidth (Gbps) medium 1 2 1 x 59 Up to 15 Up to 12 large 2 4 1 x 118 Up to 15 Up to 12 xlarge 4 8 1 x 237 Up to 15 Up to 12 2xlarge 8 16 1 x 474 Up to 17 Up to 12 4xlarge 16 32 1 x 950 Up to 17 Up to 12 8xlarge 32 64 1 x 1900 17 12 12xlarge 48 96 3 x 950 25 18 16xlarge 64 128 1 x 3800 34 24 24xlarge 96 192 3 x 1900 50 36 48xlarge 192 384 3 x 3800 100 72 metal-48xl 192 384 3 x 3800 100 72 Both families are well-suited for high-performance computing (HPC), batch processing, gaming, video encoding, scientific modeling, distributed analytics, CPU-based machine learning inference, and ad serving. Here are some additional capabilities: Instance Bandwidth Configuration (IBC) lets you adjust the allocation of bandwidth between Amazon EBS and Amazon VPC networking by up to 25%, helping you optimize performance for workloads with specific bandwidth requirements such as databases and caching. ENA Express support for enhanced networking. Up to 128 EBS volumes can be attached to virtual instances. Support for Savings Plans, On-Demand, Spot Instances, Dedicated Instances, and Dedicated Hosts. Nitro Isolation Engine Security and isolation are foundational requirements for running workloads in the cloud. Within the Nitro System , the AWS Nitro Hypervisor is designed to isolate instances from each other as well as AWS operators. With C9g and C9gd instances we are raising the bar even further with the Nitro Isolation Engine , an enhancement to the Nitro System, which enforces isolation of instances and harnesses formal verification to provide assurances of isolation with mathematical precision. C9g and C9gd instances are the first set of compute-optimized instance types to feature Nitro Isolation Engine, a purpose built component that is responsible for enforcing isolation between virtual machines, including mediation of all access to virtual machine memory, CPU register state, and I/O devices through a minimal set of APIs. To learn more about the Nitro Isolation Engine, visit the blog post . For details on the formal verification results, including scope and assumptions, see our technical white paper . Now available Amazon EC2 C9g and C9gd instances are now available in US East (Ohio, N. Virginia), US West (Oregon), and Europe (Frankfurt). Additional regions will follow. You can launch C9g and C9gd instances today using the AWS Management Console , AWS Command Line Interface (AWS CLI) , or AWS SDKs . For pricing information, visit the Amazon EC2 Pricing page . To learn more, visit the Amazon EC2 C9g and C9gd instances page and send feedback to AWS re:Post for EC2 or through your usual AWS Support contacts. — seb Editor’s Note: Updated 7/1/2026- Paragraph about Nitro Isolation Engine rewritten for clarity.

</details>

