---
type: update
id: ti-2026-002257
title: 'AWS Weekly Roundup: Price reduction of GPT models in Bedrock, CloudWatch managed
  collectors for Prometheus metrics, and more (August 3, 2026)'
aliases:
- 'AWS Weekly Roundup: Price reduction of GPT models in Bedrock, CloudWatch managed
  collectors for Prometheus metrics, and more (August 3, 2026)'
original_title: 'AWS Weekly Roundup: Price reduction of GPT models in Bedrock, CloudWatch
  managed collectors for Prometheus metrics, and more (August 3, 2026)'
company: Amazon Web Services
product: AWS
version: ''
date: '2026-08-03'
created: '2026-08-03T16:12:30+00:00'
updated: '2026-08-18T21:10:56+00:00'
original_language: en
translated: true
importance: high
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-price-reduction-of-gpt-models-in-bedrock-cloudwatch-managed-collectors-for-prometheus-metrics-and-more-august-3-2026/
source_type: rss
processed_by: openrouter
backend: opencodezen
model: nvidia/nemotron-3.5-lightning:free
insights: true
status: published
category: Cloud
subcategory: AWS announcements
confidence: medium
example: false
tags:
- aws
- bedrock
- cloudwatch
- interconnect
- iam
- s3-tables
alternatives: []
cssclasses:
- ti-note
---

# AWS Weekly Roundup: Price reduction of GPT models in Bedrock, CloudWatch managed collectors for Prometheus metrics, and more (August 3, 2026)

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Empresa | **Amazon Web Services** |
| Producto | **AWS** |

> [!abstract] Resumen
>
> - Amazon Bedrock reduce precios hasta un 80% para modelos OpenAI GPT-5.6 (Luna y Terra), aplicado automáticamente desde el 30 de julio sin requerir acción del usuario.
> - Amazon CloudWatch introduce coleccionadores gestionados de Prometheus para recolectar métricas en servicios AWS (EKS, EC2, ECS, MSK, OpenSearch) sin necesidad de implementar ni gestionar agentes propios.
> - AWS Interconnect está disponible generalmente para Oracle Cloud Infrastructure, habilitando conexiones privadas y escalables entre AWS y OCI sin atravesar Internet pública para arquitecturas multicloud seguras.
> - AWS IAM Identity Center amplía soporte multi-región para directorios de identidades, replicando la configuración a regiones adicionales para mantener el acceso de usuarios ante interrupciones en la región principal.
> - Amazon S3 Tables incorpora soporte para el tipo de datos Variant (especificación Apache Iceberg V3), permitiendo gestionar datos semiestructurados (IoT, logs) de forma nativa y de alto rendimiento en lagos de datos.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> AWS Weekly Roundup: Reducción de precios de modelos GPT en Bedrock, coleccionadores gestionados de CloudWatch para métricas de Prometheus y más (3 de agosto de 2026)
> 
> La semana pasada tuve la alegría de participar en el "Día de Trae a Tus Hijos al Trabajo" de Amazon con mi hijo de 7 años. Viajamos juntos a la oficina de Nueva York, su primer viaje en tren durante la hora pico, y pasamos el día explorando cómo Amazon utiliza IA, aprendizaje automático y robótica para entregar paquetes a clientes en todo el mundo. Ver cómo sus ojos se iluminaban al ver robots navegando por un centro de cumplimiento me recordó por qué tantos de nosotros nos metimos en la tecnología. No hay nada como ver ese sentido de asombro cuando algo complejo hace clic. Esa misma energía se trasladó a los lanzamientos de la semana. Tenemos actualizaciones en precios de IA, observabilidad, redes multicloud y gestión de datos. Vamos a sumergirnos.
> 
> Titulares: Amazon Bedrock anuncia precios reducidos hasta en un 80% para modelos OpenAI GPT‑5.6 – Si estás utilizando la familia GPT‑5.6 de OpenAI a través de Amazon Bedrock, tus costos acaban de caer significativamente. Con efecto desde el 30 de julio, los precios de inferencia bajo demanda para GPT‑5.6 Luna se reducen en un 80%, mientras que los precios de GPT‑5.6 Terra se reducen en un 20%. Luna ahora cuesta $0.20 por millón de tokens de entrada y $1.20 por millón de tokens de salida, convirtiéndola en uno de los modelos de vanguardia más asequibles disponibles. Estas reducciones de precios se aplican automáticamente, sin necesidad de que tomes ninguna acción. Lee más
> 
> Lanzamientos de la semana pasada: Aquí hay algunos lanzamientos y actualizaciones de esta semana que llamaron mi atención:
> 
> Amazon CloudWatch anuncia coleccionadores gestionados de Prometheus – Amazon CloudWatch ahora admite la recopilación de métricas de Prometheus desde tu infraestructura de AWS mediante coleccionadores completamente gestionados, lo que te permite monitorear cargas de trabajo de Amazon EKS, Amazon EC2, Amazon ECS, Amazon MSK y Amazon OpenSearch Service sin necesidad de implementar o gestionar agentes. Si has estado manteniendo tu propia infraestructura de raspado de Prometheus, esto elimina una carga operativa significativa. Lee más
> 
> AWS Interconnect: conectividad multicloud con Oracle Cloud Infrastructure ahora está disponible generalmente – AWS Interconnect es el primer producto de conectividad multicloud de su tipo diseñado específicamente para este propósito, permitiéndote aprovisionar rápidamente conexiones privadas resistentes y escalables entre AWS y otros proveedores de nube. Con este lanzamiento GA para Oracle Cloud Infrastructure (OCI), puedes establecer redes privadas entre nubes sin atravesar Internet pública, facilitando la ejecución de arquitecturas multicloud con la seguridad y rendimiento que tus cargas de trabajo demandan. Lee más
> 
> AWS IAM Identity Center amplía el soporte multi-región para el directorio de Identity Center – Ahora puedes replicar IAM Identity Center desde tu región principal de AWS a regiones adicionales cuando uses el directorio de Identity Center como tu fuente de identidad. Si IAM Identity Center se ve afectado por una interrupción en la región principal, tus usuarios continúan teniendo acceso a sus cuentas de AWS utilizando derechos provisionados en regiones adicionales. Esta función anteriormente solo estaba disponible para instancias conectadas a proveedores de identidad externos. Lee más
> 
> Amazon S3 Tables ahora admite el tipo de datos Variant para Apache Iceberg V3 – Amazon S3 Tables agrega soporte para el tipo de datos Variant, introducido en la especificación del formato de tabla Apache Iceberg V3. Variant proporciona una solución nativa de alto rendimiento para gestionar datos semiestructurados dentro de tu lago de datos, como datos de sensores IoT, registros de aplicaciones y otras cargas útiles flexibles en esquema, sin recurrir a blobs de JSON. Lee más
> 
> Otras noticias de AWS: Aquí hay algunas publicaciones y recursos adicionales que podrían interesarte:
> 
> Instalación y actualización del AWS CLI con comandos de una sola línea – Una nueva publicación en el blog del equipo de Herramientas para Desarrolladores que simplifica la instalación y actualización del AWS CLI en todas las plataformas con comandos de una sola línea. Si gestionas versiones de CLI entre equipos o en pipelines de CI, esta es una agradable mejora en calidad de vida.
> 
> Implementación de Kimi K3 en Amazon SageMaker HyperPod y Amazon EKS – Una guía paso a paso para implementar el modelo Kimi K3 de Moonshot AI en la infraestructura de AWS utilizando SageMaker HyperPod y Amazon EKS. Si estás evaluando opciones de implementación de modelos a gran escala, esta recorre el flujo de trabajo completo.
> 
> Entrega de datos de Apache Kafka a tablas de transmisión para Apache Iceberg con brokers de Amazon MSK Express – Aprende cómo transmitir datos desde Apache Kafka a tablas de Apache Iceberg utilizando brokers de Amazon MSK Express, con soporte de rendimiento de hasta 10 GB/s para la entrega a Apache Iceberg en Amazon S3 Tables.
> 
> Próximos eventos de AWS: Revisa tu calendario y regístrate para los próximos eventos de AWS:
> 
> AWS Summits: Los AWS Summits son eventos gratuitos que reúnen a la comunidad de nube e IA para conectarse, aprender y explorar las últimas tecnologías. Explora el calendario completo para encontrar un Summit cerca de ti en la segunda mitad de 2026.
> 
> AWS Community Days: Conferencias lideradas por la comunidad donde el contenido es planeado, obtenido y entregado por líderes comunitarios. Únete al AWS Builder Center para conectarte con constructores, compartir soluciones y acceder a contenido que apoya tu desarrollo. Explora aquí para encontrar eventos presenciales y virtuales organizados por AWS y eventos centrados en desarrolladores.
> 
> Eso es todo por esta semana. ¡Vuelve el lunes que viene para otro Weekly Roundup!

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Reducción de precios de hasta un 80% para modelos GPT-5.6 en Amazon Bedrock, afectando directamente el costo de uso de IA generativa.
> - Lanzamiento de coleccionistas gestionados de Prometheus en CloudWatch, eliminando la necesidad de gestionar infraestructura de monitoreo.
> - Disponibilidad general de AWS Interconnect para conectividad multicloud con Oracle Cloud Infrastructure, facilitando arquitecturas híbridas seguras.

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> El AWS Weekly Roundup del 3 de agosto de 2026 anuncia reducciones de precio de hasta 80% en modelos GPT-5.6 de OpenAI en Amazon Bedrock, coleccionadores gestionados de Prometheus en CloudWatch, conectividad multicloud AWS Interconnect con Oracle Cloud Infrastructure, expansión multi-región de IAM Identity Center, soporte de tipo Variant en S3 Tables para Apache Iceberg V3, y mejoras en AWS CLI y despliegue de modelos.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Facilita la adopción de IA generativa más económica, simplifica la observabilidad sin gestionar agentes, habilita arquitecturas multicloud seguras y de alto rendimiento, mejora la resiliencia de identidad y la gestión de datos semiestructurados en lagos de datos, y agiliza operaciones de CLI y despliegue de modelos a gran escala.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Media | Conocer nuevos precios Bedrock GPT-5.6 · Entender coleccionadores Prometheus gestionados · Aprender AWS CLI instalación simplificada |
| Junior | Alta | Implementar modelos GPT-5.6 Luna/Terra en Bedrock · Configurar CloudWatch coleccionadores Prometheus · Usar S3 Tables tipo Variant Iceberg V3 |
| Semi-Senior | Alta | Optimizar costos inferencia Bedrock con nuevos precios · Migrar a coleccionadores gestionados Prometheus · Diseñar multicloud con AWS Interconnect OCI |
| Senior | Alta | Arquitectar soluciones IA rentables con Bedrock · Evaluar observabilidad unificada CloudWatch Prometheus · Planificar resiliencia multi-región IAM Identity Center |
| Ingeniero de Software | Alta | Integrar GPT-5.6 Luna/Terra en aplicaciones · Consumir métricas Prometheus vía CloudWatch · Escribir datos Variant en S3 Tables Iceberg |
| DevOps / SRE | Alta | Automatizar despliegue coleccionadores CloudWatch Prometheus · Gestionar conectividad AWS Interconnect OCI · Actualizar AWS CLI en pipelines CI/CD |
| Ingeniero en Redes | Media | Configurar AWS Interconnect para OCI · Validar latencia y seguridad conexiones privadas · Monitorear red multicloud con CloudWatch |
| Ciberseguridad | Media | Auditar acceso multi-región IAM Identity Center · Verificar cifrado en tránsito AWS Interconnect · Revisar políticas de datos Variant en S3 |


## Precio 🪙

> [!money] unknown
>
> $0.20 por millón de tokens de entrada y $1.20 por millón de tokens de salida

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/aws-weekly-roundup-price-reduction-of-gpt-models-in-bedrock-cloudwatch-managed-collectors-for-prometheus-metrics-and-more-august-3-2026/](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-price-reduction-of-gpt-models-in-bedrock-cloudwatch-managed-collectors-for-prometheus-metrics-and-more-august-3-2026/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Last week I had the joy of participating in Amazon’s “Bring Your Kids to Work Day” with my 7 year old son. We commuted together into the New York City office, his first real rush hour train ride, and spent the day exploring how Amazon uses AI, machine learning, and robotics to deliver packages to customers all over the world. Watching his eyes light up as he saw robots navigating a fulfillment center reminded me why so many of us got into technology in the first place. There’s nothing quite like seeing that sense of wonder when something complex clicks. That same energy carried into the week’s launches. We’ve got updates across AI pricing, observability, multicloud networking, and data management. Let’s dive in. Headlines Amazon Bedrock announces up to 80% lower prices for OpenAI GPT‑5.6 models – If you’re using OpenAI’s GPT‑5.6 family through Amazon Bedrock, your costs just dropped significantly. Effective July 30, on-demand inference prices for GPT‑5.6 Luna are reduced by 80%, while GPT‑5.6 Terra prices are reduced by 20%. Luna now costs $0.20 per million input tokens and $1.20 per million output tokens, making it one of the most affordable frontier-class models available. These price reductions apply automatically — no action required on your part. Read more Last week’s launches Here are some launches and updates from this past week that caught my attention: Amazon CloudWatch announces managed Prometheus collectors – Amazon CloudWatch now supports collecting Prometheus metrics from your AWS infrastructure using fully managed collectors, enabling you to monitor Amazon EKS, Amazon EC2, Amazon ECS, Amazon MSK, and Amazon OpenSearch Service workloads without deploying or managing any agents. If you’ve been maintaining your own Prometheus scraping infrastructure, this removes a significant operational burden. Read more AWS Interconnect — multicloud connectivity with Oracle Cloud Infrastructure is now generally available – AWS Interconnect is the first purpose-built multicloud connectivity product of its kind, allowing you to quickly provision resilient, scalable private connections between AWS and other cloud providers. With this GA launch for Oracle Cloud Infrastructure (OCI), you can establish private cross-cloud networking without traversing the public internet, making it easier to run multicloud architectures with the security and performance your workloads demand. Read more AWS IAM Identity Center extends multi-Region support to Identity Center directory – You can now replicate IAM Identity Center from your primary AWS Region to additional Regions when using the Identity Center directory as your identity source. If IAM Identity Center is affected by a disruption in the primary Region, your users continue to have access to their AWS accounts using provisioned entitlements in additional Regions. This feature was previously available only for instances connected to external identity providers. Read more Amazon S3 Tables now supports the Variant data type for Apache Iceberg V3 – Amazon S3 Tables adds support for the Variant data type, introduced in the Apache Iceberg V3 table format specification. Variant provides a high-performance, native solution for managing semi-structured data within your data lake — think IoT sensor data, application logs, and other schema-flexible payloads — without resorting to JSON blobs. Read more Other AWS news Here are some additional posts and resources that you might find interesting: Installing and updating the AWS CLI with single-line commands – A new blog post from the Developer Tools team that simplifies AWS CLI installation and updates across platforms with single-line commands. If you manage CLI versions across teams or in CI pipelines, this is a nice quality-of-life improvement. Deploying Kimi K3 on Amazon SageMaker HyperPod and Amazon EKS – A step-by-step guide for deploying Moonshot AI’s Kimi K3 model on AWS infrastructure using SageMaker HyperPod and Amazon EKS. If you’re evaluating large-scale model deployment options, this walks through the full workflow. Deliver Apache Kafka data to streaming tables for Apache Iceberg with Amazon MSK Express brokers – Learn how to stream data from Apache Kafka into Apache Iceberg tables using Amazon MSK Express brokers, with throughput support of up to 10 GB/s for delivery to Apache Iceberg on Amazon S3 Tables. Upcoming AWS events Check your calendar and sign up for upcoming AWS events: AWS Summits – AWS Summits are free events that bring the cloud and AI community together to connect, learn, and explore the latest technologies. Browse the full calendar to find a Summit near you in the second half of 2026. AWS Community Days – Community-led conferences where content is planned, sourced, and delivered by community leaders. Join the AWS Builder Center to connect with builders, share solutions, and access content that supports your development. Browse here for upcoming AWS-led in-person and virtual events and developer-focused events. That’s all for this week. Check back next Monday for another Weekly Roundup!

</details>

