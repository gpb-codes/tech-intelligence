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
company: ''
product: ''
version: ''
date: '2026-07-20'
created: '2026-07-20T16:37:34+00:00'
updated: '2026-08-18T21:49:14+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-one-click-lambda-setup-prompt-openai-gpt-5-6-models-on-bedrock-and-more-july-20-2026/
source_type: rss
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
- name: Google Cloud Functions
  confidence: high
- name: Microsoft Azure Functions
  confidence: high
- name: AWS Lambda
  confidence: medium
cssclasses:
- ti-note
---

# AWS Weekly Roundup: One-click Lambda setup prompt, OpenAI GPT-5.6 models on Bedrock, and more (July 20, 2026)

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Fecha de lanzamiento | 2026-07-20 |

> [!abstract] Resumen
>
> - AWS Weekly Roundup: 
>   - Un enlace a un prompt de configuración One-click para la función Lambda.
>   - Los modelos GPT-5.6 de OpenAI están disponibles en Bedrock.
> - Información relevante: 
>   - La función Lambda.
>   - Bedrock.
> - No inventa información: 
>   - No se proporcionan detalles adicionales sobre la función Lambda.
>   - No se mencionan los modelos GPT-5.6 de OpenAI.
>   - No se mencionan los nombres de empresas.
> - No especula: 
>   - No se proporcionan opiniones o análisis sobre la información.
> - No introduces información externa: 
>   - No se mencionan fuentes o recursos externos.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> AWS Weekly Roundup: One-click Lambda setup prompt, OpenAI GPT-5.6 models on Bedrock, and more (July 20, 2026)
> 
> - Mantenga exactamente el significado.
> - No inventes información.
> - No agregues información.
> - Conserva nombres propios.
> - Conserva nombres de productos.
> - Conserva nombres de empresas.
> - Conserva versiones.
> - Conserva fechas.
> - Conserva precios.
> - Conserva URLs.
> - Conserva código.
> - No traduzcas nombres de productos o tecnologías.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Nuevos modelos importantes
> - Gran releases
> - Cambios significativos de producto

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> AWS (Amazon Web Services) es una plataforma de servicios en la nube que proporciona una amplia gama de servicios de infraestructura, aplicaciones y servicios de la nube, diseñados para satisfacer las necesidades de los usuarios finales.

> [!tip] ¿En qué ayuda al desarrollo?
>
> AWS ofrece una amplia gama de servicios que facilitan el desarrollo y la implementación de aplicaciones en la nube, lo que reduce los costos y la complejidad del desarrollo, y permite a los usuarios aprovechar las últimas tecnologías y tendencias en la industria.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | AWS CloudFormation · AWS Lambda · AWS S3 |
| Junior | Baja | AWS Cognito · AWS DynamoDB · AWS RDS |
| Semi-Senior | Baja | AWS Glue · AWS Step Functions · AWS CloudWatch |
| Senior | Alta | AWS API Gateway · AWS IAM · AWS CloudTrail |
| Ingeniero de Software | Alta | AWS CodePipeline · AWS CodeBuild · AWS CodeCommit |
| Ingeniero en Redes | Alta | AWS VPC · AWS Subnet · AWS Route 53 |
| DevOps / SRE | Alta | AWS CloudWatch · AWS CloudTrail · AWS CloudFormation |
| Ciberseguridad | Alta | AWS IAM · AWS Cognito · AWS CloudWatch |


## Información técnica ⚒️

- **Fecha de lanzamiento:** 2026-07-20

## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Alternativas 🔄

- **Google Cloud Functions** — confianza: high
- **Microsoft Azure Functions** — confianza: high
- **AWS Lambda** — confianza: medium

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/aws-weekly-roundup-one-click-lambda-setup-prompt-openai-gpt-5-6-models-on-bedrock-and-more-july-20-2026/](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-one-click-lambda-setup-prompt-openai-gpt-5-6-models-on-bedrock-and-more-july-20-2026/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Last week, my team visited Seoul to meet AWS Korea User Group (AWSKRUG) leaders. AWSKRUG is the largest cloud developer community in Korea, with 20 meetup groups organized by topic and area that collectively host over 100 events each year, primarily in Seoul. My team regularly visits countries across the Asia-Pacific region, listens to feedback from user group leaders, and works to support their communities. At this meeting, leaders honestly shared what they did well in the first half of the year, what needs improvement, and what they asked of AWS Developer Experience team. We also enjoyed a pleasant conversation during our Chimaek time together. Now, let’s take a closer look at key launches of last week. A one-click Lambda setup prompt for coding agents caught my eye most last week. This prompt configures your agent with AWS Serverless skills and the Serverless Model Context Protocol (MCP) server, embedding serverless best practices from the start. This prompt references the Lambda agent setup guide, which includes installation commands for Claude Code, Kiro, Cursor, GitHub Copilot, Codex, Devin Desktop, and OpenCode. To get started, choose the Copy agent prompt button on the Lambda console screen or copy fetch https://docs.aws.amazon.com/lambda/latest/dg/samples/aws-lambda-agent-setup.md directly, and paste this URL in your preferred AI agent. You can also use Agent Toolkit for AWS to give your coding agent current AWS knowledge and safe resource access. Use fetch https://raw.githubusercontent.com/aws/agent-toolkit-for-aws/refs/heads/main/setup-instructions/setup.md for installing AWS MCP Server. Last week’s launches Here are last week’s launches that caught my attention: OpenAI GPT-5.6 Sol, Terra, and Luna on Amazon Bedrock : You can use the smartest family of models from OpenAI yet on Bedrock’s next-generation inference engine built for high performance, security, and reliability. The three models span capability tiers from flagship reasoning (Sol) to balanced performance (Terra) to fast, cost-efficient inference (Luna), all accessible through the Responses API on Amazon Bedrock. Same-day transitions to Amazon S3 Standard-IA and S3 One Zone-IA : You can now transition objects to S3 Standard-Infrequent Access (S3 Standard-IA) and S3 One Zone-Infrequent Access (S3 One Zone-IA) as soon as the day they are created, without the previous 30-day minimum retention period in S3 Standard. These storage classes offer up to 40% lower storage costs than S3 Standard while still providing millisecond access when needed, making them ideal for backups, log analytics, and compliance workloads where data becomes cold within hours or days. Self-managed code storage on AWS Lambda : With self-managed Amazon S3 buckets for code storage, you can reference source code directly from your own S3 buckets without Lambda creating intermediate copies. This eliminates code storage limits and reduces function activation time after function creates and updates by removing the copy step. Importing users with password hashes on Amazon Cognito : You can now import users with password hashes in CSV user imports. Previously, imported users had to reset their passwords on first sign-in. Now, you can include password hashes in the CSV import, enabling users to sign in immediately with their existing credentials. When creating a CSV import, you specify the password hashing algorithm used by your source system. For a full list of AWS announcements, be sure to keep an eye on the What’s New with AWS page. Additional updates Here are some additional news items that you might find interesting: Amazon SQS turns 20: Two decades of reliable messaging at scale : When Amazon SQS launched publicly in July 2006, it made this pattern available to every AWS customer. Twenty years later, that core function, decoupling producers from consumers, remains the reason customers use SQS. Let’s look back important milestones after Jeff’s 15th anniversary post . Open Protocols with the Strands Agents SDK : Learn how open AI protocols such as MCP, A2A, UTCP, AG-UI, and x402 work together using Strands Agents SDK for building AI agents as an example implementation, though the patterns apply to any agent framework. Open source Bulk Executor for Amazon DynamoDB : Performing bulk operations against all items in a DynamoDB table has historically required custom coding. The Bulk Executor for DynamoDB simplifies bulk tasks like these. You can use this feature to invoke commands like count , find , delete , or update . No coding is required, even when running at large scale. Transform AWS Support Case Workflows with Kiro CLI : Explore how Kiro CLI’s MCP integration accelerates support case workflows by combining investigation, documentation lookup, and case creation into a single conversational interface across three real-world scenarios: AWS Glue job failures, AWS Lambda cold start investigation, and AWS WAF false positive analysis. For a full list of AWS blog posts, be sure to keep an eye on the AWS Blogs page. Learn more about AWS, browse and join upcoming AWS-led in-person and virtual events , startup events , and developer-focused events including AWS Summits . Join the AWS Builder Center to connect with builders, share solutions, and access content that supports your development. Finally, some customers experienced an issue with Cost Explorer displaying inaccurate estimated billing data in last weekend. They may have received erroneous budget and cost anomaly detection alerts, and observed inflated estimated cost and usage data. The issue has been resolved, and all AWS services are operating normally. We apologize for the concern this incident caused our customers and are conducting a thorough retrospective to prevent events like this from reoccurring, as well as improving our response when billing incidents occur. For more information, visit the AWS Health Dashboard . That’s all for this week. Check back next Monday for another Weekly Roundup ! — Channy

</details>

