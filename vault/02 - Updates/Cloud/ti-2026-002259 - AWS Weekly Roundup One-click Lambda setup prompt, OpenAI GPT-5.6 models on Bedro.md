---
type: update
id: ti-2026-002259
title: 'AWS Weekly Roundup: One-click Lambda setup prompt, OpenAI GPT-5.6 models on
  Bedrock, and more (July 20, 2026)'
aliases:
- 'AWS Weekly Roundup: One-click Lambda setup prompt, OpenAI GPT-5.6 models on Bedrock,
  and more (July 20, 2026)'
original_title: 'AWS Weekly Roundup: One-click Lambda setup prompt, OpenAI GPT-5.6
  models on Bedrock, and more (July 20, 2026)'
company: AWS
product: AWS Cloud Services
version: ''
date: '2026-07-20'
created: '2026-07-20T16:37:34+00:00'
updated: '2026-08-18T21:08:40+00:00'
original_language: en
translated: true
importance: high
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-one-click-lambda-setup-prompt-openai-gpt-5-6-models-on-bedrock-and-more-july-20-2026/
source_type: rss
processed_by: openrouter
backend: opencodezen
model: nvidia/nemotron-3.5-lightning:free
insights: true
status: published
category: Cloud
subcategory: Serverless, AI, Storage, Identity, Messaging, Database
confidence: medium
example: false
tags:
- aws
- cloud
- serverless
- lambda
- bedrock
- s3
alternatives:
- name: Google Cloud Functions
  confidence: high
- name: Cloudflare Workers
  confidence: medium
cssclasses:
- ti-note
---

# AWS Weekly Roundup: One-click Lambda setup prompt, OpenAI GPT-5.6 models on Bedrock, and more (July 20, 2026)

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Empresa | **AWS** |
| Producto | **AWS Cloud Services** |
| Fecha de lanzamiento | 20 de julio de 2026 |

> [!abstract] Resumen
>
> - Lanzamiento de un prompt de configuración un solo clic para Lambda, que integra el Protocolo de Contexto de Modelo Sin Servidor (MCP) y brinda compatibilidad con agentes de codificación (Claude Code, Kiro, Cursor, GitHub Copilot, Codex, Devin Desktop y OpenCode) para facilitar la configuración serverless desde el inicio.  
> - Disponibilidad en Amazon Bedrock de la familia de modelos OpenAI GPT-5.6 (Sol, Terra y Luna), accesibles mediante la API de Respuestas, que cubren desde razonamiento principal hasta inferencia rápida y eficiente en costos.  
> - Nueva funcionalidad de transición automática al mismo día a S3 Standard-IA y S3 One Zone-IA, eliminando el requisito mínimo de 30 días de retención y ofreciendo hasta un 40% menos de costo de almacenamiento con acceso en milisegundos, ideal para copias de seguridad y cargas de trabajo de cumplimiento.  
> - Almacenamiento de código autogestionado en AWS Lambda mediante cubos S3, que permite referenciar el código fuente directamente sin crear copias intermedias, eliminando límites de almacenamiento y reduciendo el tiempo de activación de funciones tras su creación o actualización.  
> - Amazon Cognito ahora soporta la importación de usuarios con hashes de contraseña mediante CSV, habilitando el inicio de sesión inmediato con credenciales existentes y eliminando la necesidad de restablecer la contraseña en el primer acceso.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> AWS Weekly Roundup: Configuración de Lambda con un clic, modelos OpenAI GPT-5.6 en Bedrock y más (20 de julio de 2026)
> 
> La semana pasada, mi equipo visitó Seúl para reunirse con los líderes del Grupo de Usuarios de AWS Corea (AWSKRUG). AWSKRUG es la mayor comunidad de desarrolladores en la nube en Corea, con 20 grupos de encuentros organizados por tema y área que colectivamente organizan más de 100 eventos cada año, principalmente en Seúl. Mi equipo visita regularmente países en toda la región Asia-Pacífico, escucha comentarios de líderes de grupos de usuarios y trabaja para apoyar sus comunidades. En esta reunión, los líderes compartieron honestamente lo que hicieron bien en la primera mitad del año, qué necesita mejora y lo que solicitaron al equipo de Experiencia de Desarrollador de AWS. También disfrutamos de una agradable conversación durante nuestro tiempo de Chimaek juntos. Ahora, echemos un vistazo más de cerca a los lanzamientos clave de la semana pasada. Un prompt de configuración de Lambda con un clic para agentes de codificación llamó mi atención la semana pasada. Este prompt configura su agente con habilidades de AWS Serverless y el servidor del Protocolo de Contexto de Modelo Sin Servidor (MCP), integrando las mejores prácticas de serverless desde el principio. Este prompt hace referencia a la guía de configuración del agente Lambda, que incluye comandos de instalación para Claude Code, Kiro, Cursor, GitHub Copilot, Codex, Devin Desktop y OpenCode. Para comenzar, elija el botón "Copiar prompt de agente" en la pantalla de la consola Lambda o copie fetch https://docs.aws.amazon.com/lambda/latest/dg/samples/aws-lambda-agent-setup.md directamente y pegue esta URL en su agente de IA preferido. También puede usar Agent Toolkit for AWS para dar a su agente de codificación conocimientos actualizados de AWS y acceso seguro a recursos. Use fetch https://raw.githubusercontent.com/aws/agent-toolkit-for-aws/refs/heads/main/setup-instructions/setup.md para instalar el servidor MCP de AWS. Lanzamientos de la semana pasada Aquí están los lanzamientos de la semana pasada que llamaron mi atención: Modelos OpenAI GPT-5.6 Sol, Terra y Luna en Amazon Bedrock: Puede usar la familia más inteligente de modelos de OpenAI aún en el motor de inferencia de próxima generación de Bedrock, construido para alto rendimiento, seguridad y confiabilidad. Los tres modelos abarcan niveles de capacidad desde razonamiento principal (Sol) hasta rendimiento equilibrado (Terra) hasta inferencia rápida y eficiente en costos (Luna), todos accesibles a través de la API de Respuestas en Amazon Bedrock. Transiciones del mismo día a Amazon S3 Standard-IA y S3 One Zone-IA: Ahora puede transicionar objetos a S3 Standard-Infrequent Access (S3 Standard-IA) y S3 One Zone-Infrequent Access (S3 One Zone-IA) tan pronto como se crean, sin el período mínimo de retención de 30 días en S3 Standard anterior. Estas clases de almacenamiento ofrecen hasta un 40% menos de costos de almacenamiento que S3 Standard, manteniendo el acceso en milisegundos cuando se necesita, lo que los hace ideales para copias de seguridad, análisis de registros y cargas de trabajo de cumplimiento donde los datos se enfrían en horas o días. Almacenamiento de código autogestionado en AWS Lambda: Con cubos de Amazon S3 para almacenamiento de código autogestionado, puede hacer referencia al código fuente directamente desde sus propios cubos S3 sin que Lambda cree copias intermedias. Esto elimina los límites de almacenamiento de código y reduce el tiempo de activación de funciones después de la creación y actualización de funciones, eliminando el paso de copia. Importación de usuarios con hashes de contraseñas en Amazon Cognito: Ahora puede importar usuarios con hashes de contraseñas en importaciones de usuarios CSV. Anteriormente, los usuarios importados tenían que restablecer sus contraseñas al iniciar sesión por primera vez. Ahora, puede incluir hashes de contraseñas en la importación CSV, permitiendo a los usuarios iniciar sesión inmediatamente con sus credenciales existentes. Al crear una importación CSV, especifica el algoritmo de hash de contraseñas utilizado por tu sistema de origen. Para obtener una lista completa de anuncios de AWS, asegúrese de seguir observando la página "¿Qué hay de nuevo en AWS". Actualizaciones adicionales Aquí hay algunos elementos de noticias adicionales que podría interesarle: Amazon SQS cumple 20 años: Dos décadas de mensajería confiable a escala: Cuando Amazon SQS se lanzó públicamente en julio de 2006, puso este patrón a disposición de todos los clientes de AWS. Veinte años después, esa función central, desacoplar productores de consumidores, sigue siendo la razón por la que los clientes usan SQS. Echemos un vistazo a los hitos importantes después del post de aniversario de 15 años de Jeff. Protocolos abiertos con el SDK de Agentes Strands: Aprenda cómo protocolos de IA abiertos como MCP, A2A, UTCP, AG-UI y x402 trabajan juntos usando el SDK de Agentes Strands como ejemplo de implementación, aunque los patrones se aplican a cualquier marco de agentes. Ejecutor masivo de código abierto para Amazon DynamoDB: Realizar operaciones masivas contra todos los elementos en una tabla de DynamoDB históricamente ha requerido codificación personalizada. El Ejecutor Masivo para DynamoDB simplifica tareas masivas como estas. Puede usar esta función para invocar comandos como contar, encontrar, eliminar o actualizar. No se requiere codificación, incluso al ejecutar a gran escala. Transforme flujos de trabajo de casos de soporte de AWS con Kiro CLI: Explore cómo la integración MCP de Kiro CLI acelera los flujos de trabajo de casos de soporte combinando investigación, búsqueda de documentación y creación de casos en una única interfaz conversacional a través de tres escenarios del mundo real: fallos en trabajos de AWS Glue, investigación de inicio en frío de AWS Lambda y análisis de falsos positivos de AWS WAF. Para obtener una lista completa de publicaciones de blogs de AWS, asegúrese de seguir observando la página de Blogs de AWS. Aprenda más sobre AWS, explore y únete a eventos presenciales y virtuales liderados por AWS, eventos para startups y eventos centrados en desarrolladores, incluyendo AWS Summits. Únete al AWS Builder Center para conectarte con constructores, compartir soluciones y acceder a contenido que apoya tu desarrollo. Finalmente, algunos clientes experimentaron un problema con Cost Explorer mostrando datos de facturación estimados inexactos el fin de semana pasado. Pueden haber recibido alertas erróneas de presupuestos y detección de anomalías de costos, y observado datos de costos y uso estimados inflados. El problema ha sido resuelto y todos los servicios de AWS están operando normalmente. Pedimos disculpas por la preocupación que este incidente causó a nuestros clientes y estamos realizando una retrospectiva exhaustiva para prevenir que eventos como este se repitan, así como mejorar nuestra respuesta cuando ocurren incidentes de facturación. Para más información, visite el AWS Health Dashboard. Eso es todo por esta semana. ¡Vuelva el próximo lunes para otra Weekly Roundup! — Channy

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Lanzamiento de modelos OpenAI GPT-5.6 en Amazon Bedrock, ampliando las capacidades de IA disponibles para clientes empresariales.
> - Nueva funcionalidad de configuración de Lambda con un clic para agentes de codificación, mejorando la productividad de desarrolladores.
> - Transiciones inmediatas a clases de almacenamiento S3 Standard-IA y S3 One Zone-IA sin período mínimo de retención, reduciendo costos operativos.

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> El AWS Weekly Roundup del 20 de julio de 2026 anuncia actualizaciones clave: configuración de Lambda con un clic mediante prompt para agentes de codificación (integrando MCP), disponibilidad de modelos OpenAI GPT-5.6 (Sol, Terra, Luna) en Amazon Bedrock, transiciones inmediatas a S3 Standard-IA y S3 One Zone-IA sin retención mínima, almacenamiento de código autogestionado en Lambda usando buckets S3, importación de usuarios con hashes de contraseña en Cognito, y nuevas herramientas open source como Strands Agents SDK, Bulk Executor para DynamoDB e integración MCP en Kiro CLI.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Estas novedades aceleran el desarrollo serverless al eliminar fricción en configuración de agentes IA y despliegues Lambda, democratizan acceso a modelos de razonamiento avanzado vía API gestionada, reducen costos de almacenamiento con tiering inmediato, simplifican migraciones de identidad preservando credenciales, y proveen marcos estandarizados para agentes IA y operaciones masivas en DynamoDB, mejorando productividad y eficiencia operativa.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Media | Entender prompt Lambda one-click con MCP · Conocer modelos GPT-5.6 en Bedrock · Aprender transiciones S3 IA mismo día |
| Junior | Alta | Configurar agente IA con prompt Lambda · Usar API Respuestas Bedrock para GPT-5.6 · Implementar importación Cognito con hashes |
| Semi-Senior | Alta | Diseñar serverless con almacenamiento código S3 · Optimizar costos con S3 IA inmediato · Integrar Strands SDK para agentes IA |
| Senior | Alta | Arquitectar migración a Lambda self-managed · Evaluar Bedrock vs otros proveedores IA · Planificar adopción Bulk Executor DynamoDB |
| Ingeniero de Software | Alta | Desarrollar con Agent Toolkit for AWS · Usar Kiro CLI para casos soporte AWS · Aprovechar protocolos abiertos MCP/A2A |
| Ingeniero en Redes | Baja | Monitorear transferencias datos S3 IA · Entender impacto red en Lambda S3 |
| DevOps / SRE | Alta | Automatizar despliegues Lambda sin copia · Configurar alertas Cost Explorer precisas · Operar Bulk Executor DynamoDB a escala |
| Ciberseguridad | Media | Validar algoritmos hash Cognito importación · Auditar acceso modelos Bedrock OpenAI · Revisar permisos MCP Agent Toolkit |


## Información técnica ⚒️

- **Fecha de lanzamiento:** 20 de julio de 2026

## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Alternativas 🔄

- **Google Cloud Functions** — confianza: high
- **Cloudflare Workers** — confianza: medium

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/aws-weekly-roundup-one-click-lambda-setup-prompt-openai-gpt-5-6-models-on-bedrock-and-more-july-20-2026/](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-one-click-lambda-setup-prompt-openai-gpt-5-6-models-on-bedrock-and-more-july-20-2026/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Last week, my team visited Seoul to meet AWS Korea User Group (AWSKRUG) leaders. AWSKRUG is the largest cloud developer community in Korea, with 20 meetup groups organized by topic and area that collectively host over 100 events each year, primarily in Seoul. My team regularly visits countries across the Asia-Pacific region, listens to feedback from user group leaders, and works to support their communities. At this meeting, leaders honestly shared what they did well in the first half of the year, what needs improvement, and what they asked of AWS Developer Experience team. We also enjoyed a pleasant conversation during our Chimaek time together. Now, let’s take a closer look at key launches of last week. A one-click Lambda setup prompt for coding agents caught my eye most last week. This prompt configures your agent with AWS Serverless skills and the Serverless Model Context Protocol (MCP) server, embedding serverless best practices from the start. This prompt references the Lambda agent setup guide, which includes installation commands for Claude Code, Kiro, Cursor, GitHub Copilot, Codex, Devin Desktop, and OpenCode. To get started, choose the Copy agent prompt button on the Lambda console screen or copy fetch https://docs.aws.amazon.com/lambda/latest/dg/samples/aws-lambda-agent-setup.md directly, and paste this URL in your preferred AI agent. You can also use Agent Toolkit for AWS to give your coding agent current AWS knowledge and safe resource access. Use fetch https://raw.githubusercontent.com/aws/agent-toolkit-for-aws/refs/heads/main/setup-instructions/setup.md for installing AWS MCP Server. Last week’s launches Here are last week’s launches that caught my attention: OpenAI GPT-5.6 Sol, Terra, and Luna on Amazon Bedrock : You can use the smartest family of models from OpenAI yet on Bedrock’s next-generation inference engine built for high performance, security, and reliability. The three models span capability tiers from flagship reasoning (Sol) to balanced performance (Terra) to fast, cost-efficient inference (Luna), all accessible through the Responses API on Amazon Bedrock. Same-day transitions to Amazon S3 Standard-IA and S3 One Zone-IA : You can now transition objects to S3 Standard-Infrequent Access (S3 Standard-IA) and S3 One Zone-Infrequent Access (S3 One Zone-IA) as soon as the day they are created, without the previous 30-day minimum retention period in S3 Standard. These storage classes offer up to 40% lower storage costs than S3 Standard while still providing millisecond access when needed, making them ideal for backups, log analytics, and compliance workloads where data becomes cold within hours or days. Self-managed code storage on AWS Lambda : With self-managed Amazon S3 buckets for code storage, you can reference source code directly from your own S3 buckets without Lambda creating intermediate copies. This eliminates code storage limits and reduces function activation time after function creates and updates by removing the copy step. Importing users with password hashes on Amazon Cognito : You can now import users with password hashes in CSV user imports. Previously, imported users had to reset their passwords on first sign-in. Now, you can include password hashes in the CSV import, enabling users to sign in immediately with their existing credentials. When creating a CSV import, you specify the password hashing algorithm used by your source system. For a full list of AWS announcements, be sure to keep an eye on the What’s New with AWS page. Additional updates Here are some additional news items that you might find interesting: Amazon SQS turns 20: Two decades of reliable messaging at scale : When Amazon SQS launched publicly in July 2006, it made this pattern available to every AWS customer. Twenty years later, that core function, decoupling producers from consumers, remains the reason customers use SQS. Let’s look back important milestones after Jeff’s 15th anniversary post . Open Protocols with the Strands Agents SDK : Learn how open AI protocols such as MCP, A2A, UTCP, AG-UI, and x402 work together using Strands Agents SDK for building AI agents as an example implementation, though the patterns apply to any agent framework. Open source Bulk Executor for Amazon DynamoDB : Performing bulk operations against all items in a DynamoDB table has historically required custom coding. The Bulk Executor for DynamoDB simplifies bulk tasks like these. You can use this feature to invoke commands like count , find , delete , or update . No coding is required, even when running at large scale. Transform AWS Support Case Workflows with Kiro CLI : Explore how Kiro CLI’s MCP integration accelerates support case workflows by combining investigation, documentation lookup, and case creation into a single conversational interface across three real-world scenarios: AWS Glue job failures, AWS Lambda cold start investigation, and AWS WAF false positive analysis. For a full list of AWS blog posts, be sure to keep an eye on the AWS Blogs page. Learn more about AWS, browse and join upcoming AWS-led in-person and virtual events , startup events , and developer-focused events including AWS Summits . Join the AWS Builder Center to connect with builders, share solutions, and access content that supports your development. Finally, some customers experienced an issue with Cost Explorer displaying inaccurate estimated billing data in last weekend. They may have received erroneous budget and cost anomaly detection alerts, and observed inflated estimated cost and usage data. The issue has been resolved, and all AWS services are operating normally. We apologize for the concern this incident caused our customers and are conducting a thorough retrospective to prevent events like this from reoccurring, as well as improving our response when billing incidents occur. For more information, visit the AWS Health Dashboard . That’s all for this week. Check back next Monday for another Weekly Roundup ! — Channy

</details>

