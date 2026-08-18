---
type: update
id: ti-2026-002258
title: 'AWS Weekly Roundup: Local Zone in Athens, Claude Opus 5 on AWS, Lambda durable
  execution for .NET, and more (July 27, 2026)'
aliases:
- 'AWS Weekly Roundup: Local Zone in Athens, Claude Opus 5 on AWS, Lambda durable
  execution for .NET, and more (July 27, 2026)'
original_title: 'AWS Weekly Roundup: Local Zone in Athens, Claude Opus 5 on AWS, Lambda
  durable execution for .NET, and more (July 27, 2026)'
company: Amazon Web Services
product: AWS
version: ''
date: '2026-07-27'
created: '2026-07-27T14:54:41+00:00'
updated: '2026-08-18T21:12:11+00:00'
original_language: en
translated: true
importance: high
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-july-27-2026/
source_type: rss
processed_by: openrouter
backend: opencodezen
model: nvidia/nemotron-3.5-lightning:free
insights: true
status: published
category: Cloud
subcategory: Weekly Roundup
confidence: medium
example: false
tags:
- aws
- cloud
- weekly-roundup
- announcements
- infrastructure
- ai
alternatives: []
cssclasses:
- ti-note
---

# AWS Weekly Roundup: Local Zone in Athens, Claude Opus 5 on AWS, Lambda durable execution for .NET, and more (July 27, 2026)

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Empresa | **Amazon Web Services** |
| Producto | **AWS** |

> [!abstract] Resumen
>
> - Lanzamiento de Local Zone de AWS en Atenas, Grecia, con soporte para Amazon S3 y Amazon EBS Local Snapshots, que permite almacenar y procesar datos localmente para cumplir con requisitos de residencia de datos y ofrecer latencia de milisegundos a usuarios finales.
> - Disponibilidad de Claude Opus 5 de Anthropic en Amazon Bedrock con retención de datos cero (ZDR) habilitada por defecto, que iguala la inteligencia de primer nivel de modelos superiores con precios de nivel Opus y cumple con requisitos de gobernanza de datos.
> - Lanzamiento general del SDK de ejecución duradera de AWS Lambda para .NET, que permite crear flujos de trabajo resilientes y de larga duración en C# con guardado automático de progreso y capacidad de pausar la ejecución por hasta un año, sin necesidad de orquestación externa.
> - Amazon Bedrock AgentCore ahora ofrece observabilidad unificada con trazas y prompts en un solo grupo de registros de Amazon CloudWatch, simplificando la depuración de invocaciones de agentes y permitiendo controles de acceso y cifrado detallados por agente.
> - Amazon Connect ahora soporta experiencias de voz agentivas más naturales en más de 50 idiomas, con más de 100 nuevas opciones de voz y mejoras conversacionales, facilitando interacciones de IA más fluidas en centros de contacto multilingües.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> AWS Weekly Roundup: Local Zone en Atenas, Claude Opus 5 en AWS, ejecución duradera de Lambda para .NET y más (27 de julio de 2026)
> 
> La semana pasada tuve el privilegio de pasar tres días en São Paulo con constructores técnicos de toda América Latina, reunidos para un evento tecnológico regional lleno de sesiones detalladas, talleres prácticos y conversaciones con clientes y socios. Lo que más me llamó la atención no fue ninguna sesión en particular, sino la energía de una comunidad técnica que tan rara vez tiene la oportunidad de estar en la misma habitación. La gente intercambió ideas de arquitectura durante el café, dibujó soluciones en pizarras y se fueron con una lista más larga de cosas por probar de las que llegaron. Es un buen recordatorio de que, por todas las herramientas que construimos, la comunidad alrededor de ellas es lo que hace que la tecnología se mantenga. Ese espíritu comunitario conecta muy bien con las noticias más importantes de la semana sobre infraestructura, que se tratan todas de acercar AWS a donde están realmente los constructores. Ahora, entremos en las noticias de AWS de esta semana...
> 
> Titulares
> 
> Local Zone de AWS en Atenas, Grecia: AWS ha abierto una nueva Local Zone en Atenas, Grecia, la segunda Local Zone en EMEA con soporte para Amazon S3 y Amazon EBS Local Snapshots, para que puedas almacenar y procesar datos dentro de Grecia para ayudar a cumplir con los requisitos locales de residencia de datos. La Local Zone de Atenas soporta Amazon EC2 (instancias C7i, M7i y R7i), Amazon S3 con la clase de almacenamiento One Zone-Infrequent Access, Amazon EBS, Amazon ECS y más. Con este lanzamiento, puedes procesar y almacenar datos en el país mientras ofreces latencia de milisegundos a tus usuarios finales. Las Local Zones de AWS colocan la infraestructura de AWS mucho más cerca de grandes centros de población e industria para soportar cargas de trabajo como servicios financieros, atención médica, producción de medios y juegos en tiempo real. Para los constructores en Grecia, esto significa ejecutar cargas de trabajo sensibles a la latencia localmente y cumplir con los requisitos de residencia de datos en el país, sin necesidad de gestionar tu propia infraestructura de centro de datos. Para aprender más, visita el blog de AWS Global Infrastructure and Sustainability.
> 
> Lanzamientos de la semana pasada
> 
> Aquí hay algunos lanzamientos y actualizaciones de esta semana pasada que llamaron mi atención:
> 
> Claude Opus 5 en AWS: Puedes usar Claude Opus 5 de Anthropic, el modelo Opus más avanzado hasta ahora, que iguala la inteligencia de primer nivel de Claude Fable 5 en muchos dominios con precios de nivel Opus. Amazon Bedrock ofrece Claude Opus 5 con retención de datos cero (ZDR) habilitada por defecto, dándote la inteligencia de primer nivel de Opus mientras cumples con tus requisitos de gobernanza de datos, a diferencia de Claude Fable 5. Tienes dos formas de acceder a Claude Opus 5: Amazon Bedrock y Claude Platform en AWS. Para aprender más, visita el artículo de análisis detallado.
> 
> El SDK de ejecución duradera de AWS Lambda para .NET ahora está disponible generalmente: Ahora puedes construir flujos de trabajo resilientes y de larga duración en C# usando funciones duraderas de Lambda, sin necesidad de implementar seguimiento de progreso personalizado o integrar un servicio de orquestación externo. El SDK es una excelente opción para aplicaciones multietapa como pipelines de procesamiento de pagos, orquestación de agentes de IA y aprobaciones con participación humana, guarda automáticamente el progreso y puede pausar la ejecución por hasta un año. Si eres un desarrollador .NET construyendo flujos de trabajo sin servidor, esto elimina mucha de la infraestructura que solías escribir a mano.
> 
> Amazon Bedrock AgentCore ahora ofrece observabilidad unificada con trazas y registros en un solo grupo de registros: Amazon Bedrock AgentCore ahora entrega trazas de agentes y prompts al mismo grupo de registros de Amazon CloudWatch que los registros de tu agente. Anteriormente, la telemetría estaba dividida entre destinos, las trazas iban a un grupo de registros compartido mientras que los prompts, entradas y salidas iban a otro separado, por lo que depurar una sola invocación de agente significaba buscar en múltiples lugares. Ahora puedes depurar una invocación en un solo lugar, y aplicar controles de acceso detallados y cifrado con claves administradas por el cliente (CMK) al nivel individual de cada agente.
> 
> Amazon Connect ofrece experiencias de voz agentivas más naturales: Amazon Connect ahora soporta experiencias de voz agentivas más naturales y humanas en más de 50 idiomas, incluyendo portugués, español, francés, italiano, japonés, coreano y tailandés, con más de 100 nuevas opciones de voz y mejoras conversacionales que hacen que las interacciones de IA suenen más fluidas. El autoservicio agentivo de Connect permite que los agentes de IA entiendan, razonen y actúen a través de canales de voz y digitales, adaptándose al tono y sentimiento del cliente. Ahora puedes construir experiencias de centro de contacto que se sientan naturales para los llamantes en muchos más idiomas de los que tus clientes realmente hablan.
> 
> Amazon SageMaker Unified Studio ahora soporta Amazon OpenSearch: Ahora puedes consultar y analizar tus datos de búsqueda y análisis de registros de Amazon OpenSearch directamente junto con otros activos de datos en Amazon SageMaker Unified Studio. Con esta conexión, puedes combinar datos de búsqueda operativa en OpenSearch con datos de fuentes como Amazon Redshift, Amazon S3 y bases de datos relacionales, todo dentro de un entorno gobernado único. Es especialmente útil cuando necesitas correlacionar cargas de trabajo analíticas y operativas, como unir registros de aplicaciones con datos transaccionales para descubrir perspectivas.
> 
> Amazon CloudWatch anuncia perspectivas de agentes de codificación: Amazon CloudWatch ahora brinda a los líderes de ingiería visibilidad sobre cómo las herramientas de codificación de IA están generando valor en toda su organización. Las perspectivas de agentes de codificación se integran con la puerta de enlace de aplicaciones Claude para AWS para recopir telemetría de Claude Code sin instrumentación adicional, y también soporta agentes como Codex y GitHub Copilot. A medida que los equipos escalan la adopción de codificación de IA, ahora puedes medir el retorno de esa inversión con métricas basadas en OpenTelemetry, sin necesidad de instrumentación personalizada.
> 
> Para obtener una lista completa de anuncios de AWS, asegúrate de seguir observando la página What's New with AWS.
> 
> Otras noticias de AWS
> 
> Aquí hay algunas publicaciones y recursos adicionales que podrías encontrar interesantes:
> 
> Evaluando agentes de IA: Un plan maestro de producción con Strands y AgentCore: Una guía práctica para evaluar agentes de IA antes y después de que lleguen a producción, usando Strands Agents y Amazon Bedrock AgentCore. Si estás moviendo agentes de prototipo a producción, esta publicación es un excelente complemento a la actualización de observabilidad de AgentCore mencionada arriba, te guía sobre cómo medir la calidad del agente sistemáticamente en lugar de por intuición.
> 
> Construyendo resiliencia multi-región para el despliegue de recursos personalizados de AWS CloudFormation: Aprende cómo arquitectar recursos personalizados de CloudFormation para resiliencia multi-región, para que tus despliegues de infraestructura como código permanezcan confiables incluso cuando una sola región tenga problemas.
> 
> Presentamos planes de precios de Amazon Simple Email Service (SES): Amazon SES ahora ofrece planes de precios que te dan costos más predecibles a medida que crece tu volumen de correo electrónico. Si envías a gran escala, esto podría simplificar significativamente tu facturación.
> 
> Próximos eventos de AWS
> 
> Revisa tu calendario e inscríbete para los próximos eventos de AWS:
> 
> AWS Summits: AWS Summits son eventos gratuitos que reúnen a la comunidad de nube e IA para conectarse, aprender y explorar las últimas tecnologías. Navega por el calendario completo para encontrar un Summit cerca de ti en la segunda mitad de 2026.
> 
> AWS Community Days: Conferencias lideradas por la comunidad donde el contenido es planeado, obtenido y entregado por líderes comunitarios. Si estás en América Latina, no te pierdas AWS Community Day Belo Horizonte el 22 de agosto, las inscripciones están abiertas en awscommunityday.com.br.
> 
> Únete al AWS Builder Center para conectarte con constructores, compartir soluciones y acceder a contenido que apoya tu desarrollo. Navega aquí para encontrar eventos presenciales y virtuales liderados por AWS y eventos centrados en desarrolladores.
> 
> Eso es todo por esta semana. ¡Vuelve el próximo lunes para otra Weekly Roundup!
> 
> Esta publicación es parte de nuestra serie Weekly Roundup. ¡Vuelve cada semana para obtener un resumen rápido de noticias interesantes y anuncios de AWS!

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Lanzamiento de una nueva Local Zone de AWS en Atenas, Grecia, ampliando la infraestructura de baja latencia y cumplimiento de residencia de datos en EMEA.
> - Disponibilidad general del SDK de ejecución duradera de AWS Lambda para .NET, facilitando flujos de trabajo sin servidor de larga duración en C#.
> - Integración de Claude Opus 5 en Amazon Bedrock, ofreciendo un modelo de lenguaje avanzado con retención de datos cero para gobernanza reforzada.

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> El AWS Weekly Roundup del 27 de julio de 2026 anuncia múltiples lanzamientos: nueva Local Zone en Atenas con residencia de datos, Claude Opus 5 en Amazon Bedrock con retención cero, SDK de ejecución duradera de Lambda para .NET, observabilidad unificada en Bedrock AgentCore, voces agentivas naturales en Amazon Connect en 50+ idiomas, integración de OpenSearch en SageMaker Unified Studio, y métricas de agentes de codificación en CloudWatch.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Estos lanzamientos aceleran el desarrollo al acercar infraestructura de baja latencia a usuarios finales, proveer modelos de IA avanzados con gobernanza de datos, simplificar flujos de trabajo duraderos sin orquestadores externos, unificar depuración de agentes, habilitar centros de contacto multilingües naturales, correlacionar datos operativos y analíticos, y medir ROI de herramientas de codificación con IA sin instrumentación extra.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Ingeniero de Software | Alta | SDK Lambda duradero para flujos .NET resilientes · Claude Opus 5 en Bedrock con ZDR por defecto · Integración OpenSearch en SageMaker Unified Studio |
| DevOps / SRE | Alta | Local Zone Atenas: EC2, S3, EBS, ECS locales · Observabilidad unificada AgentCore en CloudWatch · Resiliencia multi-región CloudFormation personalizada |
| Senior | Alta | Arquitectura con Local Zones para residencia datos · Patrones de ejecución duradera sin orquestador externo · Métricas OpenTelemetry para agentes de codificación |
| Semi-Senior | Media | Uso de Claude Opus 5 vs Fable 5 en Bedrock · Construcción de flujos duraderos en C# con Lambda · Depuración de agentes en grupo de logs único |
| Junior | Media | Conceptos básicos de Local Zones y casos de uso · Fundamentos de Amazon Bedrock AgentCore · Nuevas voces y idiomas en Amazon Connect |
| Ciberseguridad | Media | Retención de datos cero (ZDR) en Claude Opus 5 · Cifrado CMK a nivel de agente en AgentCore · Residencia de datos en Local Zone Atenas |
| Ingeniero en Redes | Baja | Latencia de milisegundos en Local Zone Atenas · Conectividad a servicios locales EC2, S3, EBS |
| Trainee | Baja | Qué son las Local Zones de AWS · Concepto de ejecución duradera en Lambda · Amazon Connect para centros de contacto |


## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/aws-weekly-roundup-july-27-2026/](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-july-27-2026/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Last week I had the privilege of spending three days in São Paulo with technical builders from across Latin America, brought together for a regional tech event full of deep-dive sessions, hands-on workshops, and conversations with customers and partners. What struck me most wasn’t any single session, it was the energy of a technical community that so rarely gets to be in the same room. People traded architecture ideas over coffee, sketched out solutions on whiteboards, and left with a longer list of things to try than they arrived with. It’s a good reminder that, for all the tooling we build, the community around it is what makes the technology stick. That community spirit connects nicely to the week’s biggest infrastructure news, which is all about bringing AWS closer to where builders actually are. Now, let’s get into this week’s AWS news… Headlines AWS Local Zone in Athens, Greece : AWS has opened a new Local Zone in Athens, Greece, the second Local Zone in EMEA with support for Amazon S3 and Amazon EBS Local Snapshots, so you can store and process data within Greece to help meet local data residency requirements. The Athens Local Zone supports Amazon EC2 (C7i, M7i, and R7i instances), Amazon S3 with the One Zone-Infrequent Access storage class, Amazon EBS, Amazon ECS, and more. With this launch, you can process and store data in-country while delivering single-digit millisecond latency to your end users. AWS Local Zones place AWS infrastructure much closer to large population and industry hubs to support workloads such as financial services, healthcare, media production, and real-time gaming. For builders in Greece, this means running latency-sensitive workloads locally and meeting in-country data residency requirements, without managing your own data center infrastructure. To learn more, visit AWS Global Infrastructure and Sustainability Blog post . Last week’s launches Here are some launches and updates from this past week that caught my attention: Claude Opus 5 on AWS : You can use Anthropic’s Claude Opus 5, the most advanced Opus model yet, matching Claude Fable 5’s top-tier intelligence in many domains at Opus-tier pricing. Amazon Bedrock offers Claude Opus 5 with zero data retention (ZDR) enabled by default, giving you Opus’ top-tier intelligence while meeting your data governance requirements unlike Claude Fable 5. You have two ways to access Claude Opus 5: Amazon Bedrock and Claude Platform on AWS. To learn more, visit the deep dive blog post . AWS Lambda durable execution SDK for .NET is now generally available : You can now build resilient, long-running workflows in C# using Lambda durable functions, without implementing custom progress tracking or integrating an external orchestration service. The SDK is a natural fit for multi-step applications like payment processing pipelines, AI agent orchestration, and human-in-the-loop approvals, it checkpoints progress automatically and can pause execution for up to a year. If you’re a .NET developer building serverless workflows, this removes a lot of the plumbing you used to write by hand. Amazon Bedrock AgentCore now delivers unified observability with traces and logs in a single log group : Amazon Bedrock AgentCore now delivers agent traces and prompts to the same Amazon CloudWatch log group as your agent’s logs. Previously, telemetry was split across destinations, trace spans went to a shared log group while prompts, inputs, and outputs went to a separate one, so debugging a single agent invocation meant searching in multiple places. You can now debug an invocation in one place, and apply fine-grained access control and customer-managed key (CMK) encryption at the individual agent level. Amazon Connect delivers more natural agentic voice experiences : Amazon Connect now supports more natural, human-sounding agentic voice experiences across 50+ languages, including Portuguese, Spanish, French, Italian, Japanese, Korean, and Thai, with over 100 new voice options and conversational improvements that make AI interactions sound more fluid. Connect’s agentic self-service lets AI agents understand, reason, and take action across voice and digital channels, adapting to a customer’s tone and sentiment. You can now build contact center experiences that feel natural to callers in far more of the languages your customers actually speak. Amazon SageMaker Unified Studio now supports Amazon OpenSearch : You can now query and analyze your search and log analytics data from Amazon OpenSearch directly alongside other data assets in Amazon SageMaker Unified Studio. With this connection, you can combine operational search data in OpenSearch with data from sources like Amazon Redshift, Amazon S3, and relational databases, all within a single, governed environment. It’s especially useful when you need to correlate analytical and operational workloads, such as joining application logs with transactional data to uncover insights. Amazon CloudWatch announces coding agent insights : Amazon CloudWatch now gives engineering leaders visibility into how AI coding tools are driving value across their organization. Coding agent insights integrates with the Claude apps gateway for AWS to collect telemetry from Claude Code without additional instrumentation, and also supports agents like Codex and GitHub Copilot. As teams scale AI coding adoption, you can now measure the return on that investment with metrics built on OpenTelemetry, no custom instrumentation required. For a full list of AWS announcements, be sure to keep an eye on the What’s New with AWS page. Other AWS news Here are some additional posts and resources that you might find interesting: Evaluating AI Agents: A production blueprint with Strands and AgentCore : A practical guide to evaluating AI agents before and after they reach production, using Strands Agents and Amazon Bedrock AgentCore. If you’re moving agents from prototype to production, this post is a great companion to the AgentCore observability update above, it walks through how to measure agent quality systematically rather than by gut feel. Building multi-region resiliency for AWS CloudFormation custom resource deployment : Learn how to architect CloudFormation custom resources for multi-region resiliency, so your infrastructure-as-code deployments stay reliable even when a single Region has issues. Introducing Amazon Simple Email Service (SES) pricing plans : Amazon SES now offers pricing plans that give you more predictable costs as your email volume grows. If you send at scale, this could simplify your billing significantly. Upcoming AWS events Check your calendar and sign up for upcoming AWS events: AWS Summits : AWS Summits are free events that bring the cloud and AI community together to connect, learn, and explore the latest technologies. Browse the full calendar to find a Summit near you in the second half of 2026. AWS Community Days : Community-led conferences where content is planned, sourced, and delivered by community leaders. If you’re in Latin America, don’t miss AWS Community Day Belo Horizonte on August 22, registration is open at awscommunityday.com.br . Join the AWS Builder Center to connect with builders, share solutions, and access content that supports your development. Browse here for upcoming AWS-led in-person and virtual events and developer-focused events. That’s all for this week. Check back next Monday for another Weekly Roundup! This post is part of our Weekly Roundup series. Check back each week for a quick roundup of interesting news and announcements from AWS!

</details>

