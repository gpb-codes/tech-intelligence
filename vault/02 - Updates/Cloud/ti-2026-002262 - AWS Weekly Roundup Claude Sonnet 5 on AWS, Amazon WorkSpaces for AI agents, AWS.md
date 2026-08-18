---
type: update
id: ti-2026-002262
title: 'AWS Weekly Roundup: Claude Sonnet 5 on AWS, Amazon WorkSpaces for AI agents,
  AWS service availability updates, and more (July 6, 2026)'
aliases:
- 'AWS Weekly Roundup: Claude Sonnet 5 on AWS, Amazon WorkSpaces for AI agents, AWS
  service availability updates, and more (July 6, 2026)'
original_title: 'AWS Weekly Roundup: Claude Sonnet 5 on AWS, Amazon WorkSpaces for
  AI agents, AWS service availability updates, and more (July 6, 2026)'
company: AWS
product: ''
version: ''
date: '2026-07-06'
created: '2026-07-06T15:46:43+00:00'
updated: '2026-08-18T21:07:47+00:00'
original_language: en
translated: true
importance: high
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-sonnet-5-on-aws-amazon-workspaces-for-ai-agents-aws-service-availability-updates-and-more-july-6-2026/
source_type: rss
processed_by: openrouter
backend: opencodezen
model: nvidia/nemotron-3.5-lightning:free
insights: true
status: published
category: Cloud
subcategory: AWS service updates
confidence: medium
example: false
tags:
- aws
- cloud
- ai
- infrastructure
- services
- updates
alternatives: []
cssclasses:
- ti-note
---

# AWS Weekly Roundup: Claude Sonnet 5 on AWS, Amazon WorkSpaces for AI agents, AWS service availability updates, and more (July 6, 2026)

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Empresa | **AWS** |
| Fecha de lanzamiento | July 6, 2026 |

> [!abstract] Resumen
>
> - **Lanzamiento de Claude Sonnet 5 en AWS**: El modelo más avanzado de Anthropic ya está disponible en Amazon Bedrock, ofreciendo inteligencia de primer nivel para coding, agentes y tareas profesionales a escala con mejor manejo de contexto y uso de herramientas.
> - **Disponibilidad general de Amazon WorkSpaces for AI agents**: Permite a agentes de IA acceder y operar aplicaciones de escritorio de forma segura en entornos gestionados sin necesidad de modernizar las aplicaciones ni crear integraciones personalizadas.
> - **Nuevas instancias Amazon EC2 C9g/C9gd con AWS Graviton5**: Ofrecen hasta 25% más rendimiento de cómputo que Graviton4, 5x más caché y la memoria más rápida en la nube, optimizando cargas de trabajo intensivas en cómputo.
> - **Optimización de Amazon OpenSearch Service para análisis de logs**: Nuevo motor dedicado que entrega hasta 4x mejor relación precio-rendimiento en benchmarks internos, unificando agregaciones y búsqueda full-text en una sola solución.
> - **Actualizaciones de ciclo de vida de servicios AWS (30 junio 2026)**: Múltiples servicios y características (incluyendo Amazon Kendra, Amazon Q Business, AWS IoT Device Defender Detect y funciones de SageMaker AI) pasan a Mantenimiento, Sunset o Fin de Soporte, requiriendo planificación de migración para clientes afectados.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> AWS Weekly Roundup: Claude Sonnet 5 on AWS, Amazon WorkSpaces for AI agents, AWS service availability updates, and more (July 6, 2026)
> 
> Hace unas ediciones que escribí sobre lo que encuentro tan enérgico trabajando con startups. La semana pasada recibí una dosis fresca de ello: pasé unos días con el equipo AWS Startups, escuchando historias de fundadores hablando sobre los problemas que están resolviendo realmente. Una historia que me quedó con Marco Negreiros, fundador de EyeCare Health, una healthtech brasileña que amplía el acceso a la atención ocular. Compartió un hecho impactante: más del 70% de los municipios brasileños no tienen ni un solo oftalmólogo. Su respuesta fue poner una prueba de visión en el dispositivo que casi todos ya llevan, el smartphone, de modo que un screening básico de ojos ya no depende de vivir cerca de una clínica. Ver a un fundador convertir una brecha tan grande en algo tan concreto es exactamente por lo que amo este espacio. Esta semana, tomaré un vistazo más de cerca a algunos lanzamientos clave, y luego cubriré las actualizaciones trimestrales de disponibilidad de servicios AWS. Los lanzamientos de la semana pasada Aquí están algunos de los lanzamientos cubiertos en el AWS News Blog de esta pasada semana: Instancias Amazon EC2 C9g y C9gd alimentadas por procesadores AWS Graviton5: Entreggan hasta un 25% mejor rendimiento de cómputo que las instancias basadas en Graviton4, caché 5x mayor, la memoria más rápida de cualquier procesador en la nube, y opciones de almacenamiento local NVMe (C9gd). Un nuevo modo AWS CloudFormation Express: Puedes acelerar la implementación de infraestructura con el modo AWS CloudFormation Express, permitiendo a agentes de IA y desarrolladores recibir confirmación de implementación en segundos y iterar más rápido. Disponible en todas las Regiones comerciales sin costo adicional. Actualizar clusters Amazon EKS con confianza usando rollbacks de versión de Kubernetes: Aprende cómo los rollbacks de versión de Kubernetes para Amazon EKS te permiten revertir actualizaciones de cluster dentro de siete días. Esta nueva característica brinda una red de seguridad para fallos de actualización, sin necesidad de reconstruir clusters, convirtiendo las actualizaciones de versión de Kubernetes en una operación reversible de bajo riesgo. Automatizar la emisión pública de certificados TLS con soporte ACME en AWS Certificate Manager: AWS Certificate Manager ahora soporta el protocolo ACME, por lo que puedes automatizar la emisión y renovación de certificados TLS públicos usando herramientas estándar y ampliamente adoptadas. Aquí hay algunos lanzamientos y actualizaciones que llamaron mi atención: Claude Sonnet 5 ya está disponible en AWS – El modelo Sonnet más capaz de Anthropic aporta inteligencia de primer nivel al precio de Sonnet para coding, agentes y trabajo profesional a escala. Navega por grandes bases de código, llama herramientas con precisión, y mantiene estado en tareas agénticas de larga duración. Para más información, visita el post del AI Blog. Amazon WorkSpaces for AI agents ya está disponible generalmente: Los agentes de IA ahora pueden acceder de forma segura y operar aplicaciones de escritorio a través de entornos de WorkSpaces gestionados, sin requerir modernización de aplicaciones o integraciones personalizadas. Para más información. visita el post del Desktop and Application Streaming Blog post. Amazon OpenSearch Service ahora está optimizado para análisis de logs: Esta introducción incluye un motor creado específicamente para cargas de trabajo de análisis de logs que ofrece hasta 4x mejor relación precio-rendimiento en benchmarks internos, manteniendo las capacidades de búsqueda full-text que OpenSearch es conocido. Los equipos ahora pueden obtener agregaciones y búsqueda de texto preciso en un solo lugar. Para más información, visita el post del Big Data Blog post. Amazon SageMaker AI reduce a la mitad el tiempo de escala-out de IA generativa: SageMaker Inference ahora soporta caché de imágenes de contenedor, habilitando hasta 2x más rápido escala end-to-end para modelos de IA generativa durante eventos de escala-out. Para más información, visita el post del AI Blog post. Amazon CloudWatch ahora admite crear alarmas desde consultas de logs: Ahora puedes crear alarmas directamente en resultados de consulta de logs y establecer umbrales en un solo flujo de trabajo, eliminando la necesidad de crear primero filtros de métricas o métricas personalizadas como pasos intermedios. Para una lista completa de anuncios AWS, asegúrate de mantener la vista en la página What’s New with AWS. Actualizaciones de disponibilidad de servicios AWS Cuando la disponibilidad de un servicio o característica de AWS cambia, ofrecemos orientación a los clientes en AWS Product Lifecycle Changes sobre alternativas disponibles y soporte para migración para que las interrupciones a tus operaciones se minimicen. Los siguientes cambios de ciclo de vida se actualizaron el June 30, 2026. Servicios que se mueven a Mantenimiento (ya no accesibles para nuevos clientes a partir del July 30, 2026): Amazon Bedrock Agents (lanzado noviembre 2023) ahora es Amazon Bedrock Agents Classic Amazon Cognito Sync Amazon Kendra Amazon Q Business AWS Directory Service – Simple AD AWS IoT Device Defender – Detect (la característica ya no será accesible para nuevos clientes a partir de August 31, 2026) AWS Mainframe Modernization – Self-Managed Experience AWS Management Console – myApplications AWS Resource Groups – Group Lifecycle Events AWS Service Catalog – Application Registry AWS Systems Manager – Application Manager Amazon SageMaker AI features: A2I , Clarify , Debugger , GeoSpatial , Ground Truth , Mechanical Turk , Model Monitor , Role Manager , and Studio Lab Servicios en Sunset: Amazon WorkSpaces – PCoIP Amazon WorkSpaces – Pool AWS Managed Services (AMS) Advanced AWS re:Post Private Amazon Sagemaker AI- Profiler Servicios que llegan al fin del Soporte (as of June 30, 2026): Amazon Chime SDK – Carrier Voice Focus Amazon SageMaker AI – Ground Truth Plus Entendemos que los cambios en disponibilidad pueden impactar tus operaciones. Para orientación específica, consulta la documentación del servicio relevante o contacta al soporte de AWS. Próximos eventos AWS Revisa tu calendario y regístrate para próximos eventos AWS: AWS Summits – AWS Summits son eventos gratuitos que reúnen a la comunidad cloud y AI para conectar, aprender y explorar las últimas tecnologías. Navega por el calendario completo para encontrar un Summit cerca de ti en la second half of 2026. AWS Community Days – Conferencias lideradas por la comunidad donde el contenido se planifica, sourcing y entrega por líderes comunitarios. Si estás en Latinoamérica, no te pierdas AWS Community Day Belo Horizonte el August 22. El registro está abierto en awscommunityday.com.br. Únete al AWS Builder Center para conectar con creadores, compartir soluciones y acceder a contenido que apoya tu desarrollo. Navega aquí para próximos eventos AWS presenciales y virtuales liderados y eventos enfocados en desarrolladores. Eso es todo por esta semana. ¡Mañana vuelve la próxima semana para otro Weekly Roundup! – Daniel Abib Esta publicación es parte de nuestra serie Weekly Roundup. ¡Mantente atento cada semana para un rápido resumen de noticias y anuncios de AWS!

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Instancias EC2 C9g y C9gd con procesadores AWS Graviton5 que ofrecen hasta un 25% mejor rendimiento de cómputo, caché 5x mayor y memoria más rápida en la nube.
> - Disponibilidad de Claude Sonnet 5 en AWS, modelo de Anthropic con inteligencia de primer nivel para coding, agentes y trabajo profesional al precio de Sonnet.
> - Optimización de Amazon OpenSearch Service para análisis de logs con hasta 4x mejor relación precio-rendimiento, manteniendo capacidades de búsqueda full-text.

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> Es un resumen semanal de AWS (julio de 2026) que agrupa lanzamientos tecnológicos como instancias EC2 Graviton5, CloudFormation Express y Claude Sonnet 5. También detalla actualizaciones de disponibilidad de servicios en la nube y nuevas capacidades de IA y observabilidad.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Estas actualizaciones ayudan al desarrollo de software al acelerar el despliegue de infraestructura y permitir iteraciones más rápidas mediante agentes de IA y CloudFormation Express. Además, mejoran la resiliencia con rollbacks en EKS y automatizan la emisión de certificados TLS, reduciendo la carga operativa.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Media | Instancias EC2 C9g con Graviton5 · Modo CloudFormation Express gratuito · Claude Sonnet 5 en AWS |
| Junior | Alta | Rollback de versiones en EKS · Soporte ACME en Certificate Manager · Alarmas CloudWatch desde logs |
| Semi-Senior | Alta | Optimización de OpenSearch para logs · Caché de imágenes en SageMaker · Actualizaciones de disponibilidad AWS |
| Senior | Alta | Rendimiento EC2 C9g con Graviton5 · Cambios de ciclo de vida AWS · WorkSpaces para agentes de IA |
| Ingeniero de Software | Alta | Claude Sonnet 5 para código · CloudFormation Express para iterar · Agentes IA en WorkSpaces |
| Ingeniero en Redes | Media | Automatización TLS con ACME · Instancias C9gd con NVMe · Almacenamiento local rápido |
| DevOps / SRE | Alta | Rollbacks Kubernetes en EKS · Alarmas CloudWatch en logs · Escala-out SageMaker 2x más rápido |
| Ciberseguridad | Media | Certificados TLS automatizados ACME · Acceso seguro agentes WorkSpaces · Fin de soporte servicios AWS |


## Información técnica ⚒️

- **Fecha de lanzamiento:** July 6, 2026

## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-sonnet-5-on-aws-amazon-workspaces-for-ai-agents-aws-service-availability-updates-and-more-july-6-2026/](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-sonnet-5-on-aws-amazon-workspaces-for-ai-agents-aws-service-availability-updates-and-more-july-6-2026/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

A couple of editions ago I wrote about what I find so energizing about working with startups. Last week I got a fresh dose of it: I spent a few days with the AWS Startups team, listening to stories of founders talking about the problems they’re actually solving. One story that stayed with me came from Marco Negreiros, founder of EyeCare Health , a Brazilian healthtech expanding access to eye care. He shared a striking fact: more than 70% of Brazilian municipalities don’t have a single ophthalmologist. His answer was to put a vision test on the one device almost everyone already carries, the smartphone, so a basic eye screening no longer depends on living near a clinic. Watching a founder turn a gap that big into something that concrete is exactly why I love this space. This week, I’ll take a closer look at some key launches, and then cover the quarterly AWS Service Availability updates. Last week’s launches Here are some of the launches covered from this past week in the AWS News Blog: Amazon EC2 C9g and C9gd instances powered by AWS Graviton5 processors : They deliver up to 25% better compute performance than Graviton4-based instances, 5x larger cache, fastest memory of any processor instances in the cloud, and local NVMe storage options (C9gd). A new AWS CloudFormation Express mode : You can speed up infrastructure deployment with AWS CloudFormation Express mode, enabling AI agents and developers to receive deployment confirmation in seconds and iterate faster. Available in all commercial Regions at no additional cost. Upgrade Amazon EKS clusters with confidence using Kubernetes version rollbacks : Learn how Kubernetes version rollbacks for Amazon EKS let you reverse cluster upgrades within seven days. This new feature provides a safety net for upgrade failures, no cluster rebuilds required, turning Kubernetes version upgrades into a reversible, low-risk operation. Automate public TLS certificate issuance with ACME support in AWS Certificate Manager : AWS Certificate Manager now supports the ACME protocol, so you can automate the issuance and renewal of public TLS certificates using standard, widely adopted tooling. Here are some launches and updates that caught my attention: Claude Sonnet 5 is now available on AWS – Anthropic’s most capable Sonnet model brings top-tier intelligence at Sonnet pricing for coding, agents, and everyday professional work at scale. It navigates large codebases, calls tools precisely, and holds state across long agentic tasks. To learn more, visit the AI Blog post . Amazon WorkSpaces for AI agents is now generally available : AI agents can now securely access and operate desktop applications through managed WorkSpaces environments, without requiring application modernization or custom integrations. To learn more. visit the Desktop and Application Streaming Blog post . Amazon OpenSearch Service is now optimized for log analytics : This release introduces a new engine purpose-built for log analytics workloads that delivers up to 4x better price-performance on internal benchmarks, while keeping the full-text search capabilities OpenSearch is known for. Teams can now get aggregations and precise text search in one place. To learn more, visit the Big Data Blog post . Amazon SageMaker AI cuts generative AI inference scale-out time by up to half : SageMaker Inference now supports container image caching, enabling up to 2x faster end-to-end scaling for generative AI models during scale-out events. To learn more, visit the AI Blog post . Amazon CloudWatch supports creating alarms from log queries : You can now create alarms directly on log query results and set thresholds in a single workflow, eliminating the need to first create metric filters or custom metrics as intermediate steps. For a full list of AWS announcements, be sure to keep an eye on the What’s New with AWS page. AWS Service Availability Updates When the availability of an AWS service or feature changes, we provide customers guidance in AWS Product Lifecycle Changes on available alternatives and support for migration so that disruptions to your operations are minimized. The following lifecycle changes were updated on June 30, 2026. Services moving to Maintenance (no longer accessible to new customers starting July 30, 2026): Amazon Bedrock Agents (launched November 2023) is now Amazon Bedrock Agents Classic Amazon Cognito Sync Amazon Kendra Amazon Q Business AWS Directory Service – Simple AD AWS IoT Device Defender – Detect (feature will no longer be accessible to new customers starting August 31, 2026) AWS Mainframe Modernization – Self-Managed Experience AWS Management Console – myApplications AWS Resource Groups – Group Lifecycle Events AWS Service Catalog – Application Registry AWS Systems Manager – Application Manager Amazon SageMaker AI features: A2I , Clarify , Debugger , GeoSpatial , Ground Truth , Mechanical Turk , Model Monitor , Role Manager , and Studio Lab Services entering Sunset: Amazon WorkSpaces – PCoIP Amazon WorkSpaces – Pool AWS Managed Services (AMS) Advanced AWS re:Post Private Amazon Sagemaker AI- Profiler Services reaching End of Support (as of June 30, 2026): Amazon Chime SDK – Carrier Voice Focus Amazon SageMaker AI – Ground Truth Plus We understand that changes in availability can impact your operations. For specific guidance, consult the relevant service documentation or contact AWS Support. Upcoming AWS events Check your calendar and sign up for upcoming AWS events: AWS Summits – AWS Summits are free events that bring the cloud and AI community together to connect, learn, and explore the latest technologies. Browse the full calendar to find a Summit near you in the second half of 2026. AWS Community Days – Community-led conferences where content is planned, sourced, and delivered by community leaders. If you’re in Latin America, don’t miss AWS Community Day Belo Horizonte on August 22. Registration is open at awscommunityday.com.br . Join the AWS Builder Center to connect with builders, share solutions, and access content that supports your development. Browse here for upcoming AWS-led in-person and virtual events and developer-focused events. That’s all for this week. Check back next Monday for another Weekly Roundup! – Daniel Abib This post is part of our Weekly Roundup series. Check back each week for a quick roundup of interesting news and announcements from AWS!

</details>

