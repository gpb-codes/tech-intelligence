---
type: update
id: ti-2026-002261
title: 'AWS Weekly Roundup: AWS Builder Center at 1 year, Network Scanning in Security
  Hub, Loom for AWS, and more (July 13, 2026)'
aliases:
- 'AWS Weekly Roundup: AWS Builder Center at 1 year, Network Scanning in Security
  Hub, Loom for AWS, and more (July 13, 2026)'
original_title: 'AWS Weekly Roundup: AWS Builder Center at 1 year, Network Scanning
  in Security Hub, Loom for AWS, and more (July 13, 2026)'
company: Amazon Web Services
product: ''
version: ''
date: '2026-07-13'
created: '2026-07-13T16:18:20+00:00'
updated: '2026-08-18T21:05:37+00:00'
original_language: en
translated: true
importance: high
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-builder-center-at-one-year-network-scanning-in-security-hub-loom-for-aws-and-more-july-13-2026/
source_type: rss
processed_by: openrouter
backend: opencodezen
model: nvidia/nemotron-3.5-lightning:free
insights: true
status: published
category: Cloud
subcategory: weekly aws summary
confidence: medium
example: false
tags:
- aws
- cloud
- security
- ai
- developer tools
alternatives: []
cssclasses:
- ti-note
---

# AWS Weekly Roundup: AWS Builder Center at 1 year, Network Scanning in Security Hub, Loom for AWS, and more (July 13, 2026)

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Empresa | **Amazon Web Services** |
| Fecha de lanzamiento | 2026-07-13 |

> [!abstract] Resumen
>
> - AWS Builder Center cumplió su primer aniversario (lanzado el 9 de julio de 2025) y estrenó **Sandbox Environments**: entornos AWS gratuitos y preaprovisionados para talleres, activos por 8 horas, limitados a uno simultáneo y uno por semana, sin requerir cuenta personal ni tarjeta de crédito.
> - **AWS Security Hub** lanzó **Network Scanning**, que sondea recursos desde internet público para detectar alcanzabilidad real en entornos AWS y Azure, generando hallazgos con evidencia de puertos y servicios; se incluye en Security Hub Essentials sin costo extra y extiende la gestión unificada de postura, vulnerabilidades y respuesta a recursos de Microsoft Azure.
> - **Amazon SageMaker Studio** integró **despliegue y personalización en un clic con Hugging Face** ("Customize on SageMaker AI" / "Deploy on SageMaker AI"), aprovisionando entornos Studio en segundos con permisos preconfigurados para fine-tuning, evaluación y despliegue, y concediendo acceso GPU por defecto (G5, G6, G4dn) a clientes verificados.
> - **Amazon EKS Auto Mode y Amazon ECS Managed Instances** redujeron automáticamente las tarifas de gestión de instancias aceleradas desde el 1 de julio de 2026: 35 % en series G y 60 % en series P y AWS Trainium, aplicable a clústeres existentes sin acción del cliente.
> - **Amazon Aurora DSQL** puso en disponibilidad general **Change Data Capture (CDC)**, que transmite operaciones de inserción, actualización y borrado como eventos de cambio a Amazon Kinesis Data Streams con impacto nulo en la carga de trabajo y sin infraestructura que gestionar.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Resumen semanal de AWS: AWS Builder Center at 1 year, Network Scanning in Security Hub, Loom for AWS, and more (13 de julio de 2026)
> 
> AWS Builder Center turned one year old last week. Launched on July 9, 2025, la plataforma ha crecido desde un hub comunitario con votación de Deseos, perfiles comunitarios y una caja de herramientas hasta un ecosistema completo con entornos de sandbox, talleres, Espacios y una Builders’ Library. Para conmemorar el aniversario, Rick Suttles publicó una línea de tiempo completa de características que cubre todo lo enviado en el último año: AWS Capabilities by Region (1,500+ servicios across 37 Regions), Spaces for community-created groups, workshops with category and complexity filters, badges and streaks, article series, view counts, saved items, student status, availability notifications, sign-in with GitHub and Amazon, and sandbox environments. Jeff Barr published a retrospective summarizing Builder Center’s first year. Since launch, 5,548 authors have published 6,448 articles with more than 10.4 million page views combined. Builders have earned 99,226 badges since the badge system launched in March 2026. Community members have submitted 565 wishes, 10 of which have shipped with another 20 on the near-term roadmap. The top community article Building an AWS Study Buddy with MCP + Strands Agents SDK by Dineshraj Dhanapathy reached 50,000+ views. Chris Miller’s Migrating an EOL Linux Server to AWS in 8 Hours with Kiro followed at 45,000+, and Yash Aggarwal’s AIdeas: NeuroVoice – Multimodal AI for Early Screening of Neurological Diseases article reached 38,000+. The week’s headline addition is Sandbox Environments by Rick Suttles. Sandboxes give you a free, pre-provisioned AWS account to complete a workshop exercise. Each environment is active for 8 hours, after which the account and all its resources are automatically de-provisioned. You can have one active sandbox at a time and request one per week. No personal AWS account, credit card, or manual cleanup required. Last week’s launches Here’s what else happened this week. AWS Security Hub introduces Network Scanning – Security Hub introduced Network Scanning, a capability that identifies resources in your environment that are reachable from the public internet. Network Scanning probes your resources from the internet to detect actual reachability, complementing the existing network reachability findings in Security Hub that identify configurations that could make a resource reachable. It discovers public IP addresses, virtual machines, and load balancers across your AWS and Azure environments, identifies reachable ports, and determines what services are running behind them. Each reachable port generates a Security Hub finding with evidence of the port and service discovered. Security Hub Exposures then automatically correlates these findings with other findings and resource configurations to determine broader risk. Existing customers can enable Network Scanning in individual accounts and Regions, or across an organization through a configuration policy. For new customers, Network Scanning is on by default. It is included with Security Hub Essentials at no additional cost. Security Hub also extends unified security management to Microsoft Azure – Security Hub now monitors Microsoft Azure resources, providing unified posture management, vulnerability management, and security response across both clouds. It automatically discovers Azure VMs, container images, Function Apps, and identities, and evaluates them for misconfigurations, internet exposure, and software vulnerabilities. AWS and Azure findings appear in the same prioritized view with the same formats and automation workflows. Amazon SageMaker Studio integrates with Hugging Face for one-click model deployment and customization – You can now go from discovering a model on Hugging Face to working with it in SageMaker Studio in a single click. Select any supported model on Hugging Face and choose “Customize on SageMaker AI” or “Deploy on SageMaker AI” to land directly on the corresponding workflow page with the model pre-loaded. New customers receive a Studio environment created in seconds with pre-configured permissions for serverless model customization (including fine-tuning with custom reward functions for reinforcement learning), model evaluation, and deployment to SageMaker or Bedrock endpoints. Verified customers receive default GPU access to G5, G6, and G4dn instances without requesting quota increases, and quota utilization is visible directly inside the Studio environment. Amazon EKS Auto Mode and Amazon ECS Managed Instances reduce GPU management fees by up to 60% – Beginning July 1, 2026, EKS Auto Mode and ECS Managed Instances reduce management fees for accelerated instance types: G-series fees are down 35%, and P-series and AWS Trainium fees are down 60%. The reductions apply automatically to existing clusters and require no action from customers. Both services include capabilities built for accelerated workloads. EKS Auto Mode provides automatic parallel image pulling on GPU instances with local NVMe storage and accelerator-aware node repair. ECS Managed Instances provides GPU metrics through Amazon CloudWatch Container Insights and automatic health monitoring for GPU hardware failures. Amazon Aurora DSQL change data capture (CDC) is now generally available – Aurora DSQL CDC streams the results of insert, update, and delete operations as change events to Amazon Kinesis Data Streams. You can use it to synchronize data across microservices, trigger Lambda functions, or deliver changes to S3, Redshift, and OpenSearch Service through Amazon Data Firehose. CDC streaming is designed to have zero impact on database workload performance and requires no infrastructure to manage. For a full list of AWS announcements, be sure to keep an eye on the What’s New with AWS page. Other AWS news Here are some additional posts you may find useful: Building secure AI agents at scale: Introducing Loom for AWS – Loom is an open-source enterprise platform for building agents with AWS Strands Agents and deploying them on Amazon Bedrock AgentCore Runtime. It provides a unified management UI and backend API with identity provider integration, scope-based authorization, multi-persona navigation, and full lifecycle management for agents, memory, MCP servers, and agent-to-agent integrations. Loom enforces automated resource tagging for cost attribution, implements RBAC and ABAC for multi-tenant security, uses paved-path blueprints for agent deployments, manages identity propagation through delegated actor chains, integrates with AWS Agent Registry for discovery and governance, and supports human-in-the-loop review before sensitive actions. The project is available in AWS Labs on GitHub. Introducing Claude apps gateway for AWS – The Claude apps gateway is a self-hosted control plane that gives organizations centralized control over access, cost, and policy for Claude Code and Claude Desktop. It connects to any OIDC-compliant identity provider, enforces managed settings on every request, routes inference to Amazon Bedrock or Claude Platform on AWS, and supports per-user and per-group spend caps. The gateway runs as a stateless container in your private network, backed by a PostgreSQL database for short-lived sign-in state. No long-lived secrets are stored on developer machines. Deploy it through Amazon Bedrock to keep data within the AWS security boundary, or through Claude Platform on AWS for the native Claude platform experience. Introducing OAuth support for AWS MCP Server – You can now connect agents to the AWS MCP Server using browser-based OAuth with the same credentials you use for the AWS Console or CLI. The new sign-in path supports IAM federation, AWS IAM Identity Center, and root or IAM users. AWS Sign-In issues short-lived access tokens and refresh tokens, with automatic token management so developers stay authenticated across restarts. For headless use cases, a non-interactive flow lets applications with existing AWS credentials obtain OAuth access tokens through the create-oauth2-token-with-iam API. New governance controls include OAuth-specific IAM condition keys, token introspection and revocation, dynamic client registration, and CloudTrail audit elements. For a full list of AWS blog posts, be sure to keep an eye on the AWS Blogs page. Upcoming AWS events Check your calendar and sign up for upcoming AWS events: AWS Summits – Free in-person events for builders and innovators to learn, think big, and make new connections. Coming up: Taipei (July 15), Bogotá (July 30), Jakarta (August 6), Ciudad de México (August 12), Johannesburg (August 19), and Zurich (September 2). AWS Community Days – Community-led conferences planned and delivered by community leaders. Upcoming events include Yaoundé, Cameroon (July 25), Ahmedabad, India (July 25), Belo Horizonte, Brazil (August 22), Ottawa, Canada (August 22), Tulsa, USA (August 22), and Toronto, Canada (August 29). Visit the AWS Builder Center to meet other builders, contribute solutions, and find resources that help you keep building. Wishing everyone a restful and enjoyable summer. Whether you’re building, learning, or recharging, I hope you find time for all three. I’ll be heading to Scandinavia for a few weeks to trade the heat for some cooler weather and longer evenings. Come back next week for more news! — Esra

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - AWS Builder Center reached its first anniversary with over 5,548 authors publishing 6,448 articles viewed more than 10.4 million times, and introduced sandbox environments for free pre-provisioned AWS accounts.
> - Security Hub launched Network Scanning to identify resources reachable from the public internet across AWS and Azure, with findings automatically correlated to risk and enabled by default for new customers at no additional cost.
> - EKS Auto Mode and ECS Managed Instances began reducing GPU management fees by up to 60% on July 1, 2026, automatically applying to existing clusters without requiring customer action.

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> AWS Weekly Roundup presenta un conjunto de actualizaciones y nuevos productos en el ecosistema AWS, incluyendo el aniversario de Builder Center con sandboxes, Network Scanning en Security Hub e integraciones de IA. Estas tecnologías abarcan desde la educación y desarrollo de agentes hasta la seguridad multicloud y la optimización de costos en GPU. El contenido destaca herramientas que facilitan la construcción, despliegue y protección de aplicaciones modernas en la nube.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Estas actualizaciones aceleran el desarrollo de software al ofrecer entornos sandbox gratuitos y preconfigurados que eliminan la necesidad de cuentas personales o limpieza manual. Simplifican el despliegue de modelos de IA y automatizan la detección de vulnerabilidades de red expuestas a internet. Además, reducen los costos de infraestructura GPU y facilitan la sincronización de datos mediante CDC, permitiendo sistemas más ágiles y seguros.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | Usar sandboxes gratuitos de 8 horas · Explorar Builder Center y talleres · Acceder con GitHub o Amazon |
| Junior | Alta | OAuth en AWS MCP Server · Despliegue 1-click SageMaker-HuggingFace · Sandboxes para prácticas |
| Semi-Senior | Media | Aurora DSQL CDC a Kinesis · EKS Auto Mode GPU features · Gestionar costos de GPU |
| Senior | Alta | Arquitectura con Loom y AgentCore · Claude apps gateway policies · Seguridad multicloud Hub |
| Ingeniero de Software | Alta | Integración Hugging Face Studio · Streaming CDC sin impacto DB · Construir agentes con Strands |
| Ingeniero en Redes | Media | Network Scanning en Security Hub · Descubrimiento de IPs públicas · Monitoreo de puertos abiertos |
| DevOps / SRE | Alta | Reducción 60% cuotas GPU · Métricas GPU en CloudWatch · Auto Mode EKS y ECS |
| Ciberseguridad | Alta | Network Scanning proactivo · RBAC/ABAC en Loom · Monitoreo unificado Azure/AWS |


## Información técnica ⚒️

- **Fecha de lanzamiento:** 2026-07-13

## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-builder-center-at-one-year-network-scanning-in-security-hub-loom-for-aws-and-more-july-13-2026/](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-builder-center-at-one-year-network-scanning-in-security-hub-loom-for-aws-and-more-july-13-2026/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

AWS Builder Center turned one year old last week. Launched on July 9, 2025, the platform has grown from a community hub with Wishlist voting, community profiles, and a toolbox into a full ecosystem with sandbox environments, workshops, Spaces, and a Builders’ Library. To mark the anniversary, Rick Suttles published a full feature timeline covering everything shipped over the past year: AWS Capabilities by Region (1,500+ services across 37 Regions), Spaces for community-created groups, workshops with category and complexity filters, badges and streaks, article series, view counts, saved items, student status, availability notifications, sign-in with GitHub and Amazon, and sandbox environments. Jeff Barr published a retrospective summarizing Builder Center’s first year. Since launch, 5,548 authors have published 6,448 articles with more than 10.4 million page views combined. Builders have earned 99,226 badges since the badge system launched in March 2026. Community members have submitted 565 wishes, 10 of which have shipped with another 20 on the near-term roadmap. The top community article Building an AWS Study Buddy with MCP + Strands Agents SDK by Dineshraj Dhanapathy reached 50,000+ views. Chris Miller’s Migrating an EOL Linux Server to AWS in 8 Hours with Kiro followed at 45,000+, and Yash Aggarwal’s AIdeas: NeuroVoice – Multimodal AI for Early Screening of Neurological Diseases article reached 38,000+. The week’s headline addition is Sandbox Environments by Rick Suttles. Sandboxes give you a free, pre-provisioned AWS account to complete a workshop exercise. Each environment is active for 8 hours, after which the account and all its resources are automatically de-provisioned. You can have one active sandbox at a time and request one per week. No personal AWS account, credit card, or manual cleanup required. Last week’s launches Here’s what else happened this week. AWS Security Hub introduces Network Scanning – Security Hub introduced Network Scanning, a capability that identifies resources in your environment that are reachable from the public internet. Network Scanning probes your resources from the internet to detect actual reachability, complementing the existing network reachability findings in Security Hub that identify configurations that could make a resource reachable. It discovers public IP addresses, virtual machines, and load balancers across your AWS and Azure environments, identifies reachable ports, and determines what services are running behind them. Each reachable port generates a Security Hub finding with evidence of the port and service discovered. Security Hub Exposures then automatically correlates these findings with other findings and resource configurations to determine broader risk. Existing customers can enable Network Scanning in individual accounts and Regions, or across an organization through a configuration policy. For new customers, Network Scanning is on by default. It is included with Security Hub Essentials at no additional cost. Security Hub also extends unified security management to Microsoft Azure – Security Hub now monitors Microsoft Azure resources, providing unified posture management, vulnerability management, and security response across both clouds. It automatically discovers Azure VMs, container images, Function Apps, and identities, and evaluates them for misconfigurations, internet exposure, and software vulnerabilities. AWS and Azure findings appear in the same prioritized view with the same formats and automation workflows. Amazon SageMaker Studio integrates with Hugging Face for one-click model deployment and customization – You can now go from discovering a model on Hugging Face to working with it in SageMaker Studio in a single click. Select any supported model on Hugging Face and choose “Customize on SageMaker AI” or “Deploy on SageMaker AI” to land directly on the corresponding workflow page with the model pre-loaded. New customers receive a Studio environment created in seconds with pre-configured permissions for serverless model customization (including fine-tuning with custom reward functions for reinforcement learning), model evaluation, and deployment to SageMaker or Bedrock endpoints. Verified customers receive default GPU access to G5, G6, and G4dn instances without requesting quota increases, and quota utilization is visible directly inside the Studio environment. Amazon EKS Auto Mode and Amazon ECS Managed Instances reduce GPU management fees by up to 60% – Beginning July 1, 2026, EKS Auto Mode and ECS Managed Instances reduce management fees for accelerated instance types: G-series fees are down 35%, and P-series and AWS Trainium fees are down 60%. The reductions apply automatically to existing clusters and require no action from customers. Both services include capabilities built for accelerated workloads. EKS Auto Mode provides automatic parallel image pulling on GPU instances with local NVMe storage and accelerator-aware node repair. ECS Managed Instances provides GPU metrics through Amazon CloudWatch Container Insights and automatic health monitoring for GPU hardware failures. Amazon Aurora DSQL change data capture (CDC) is now generally available – Aurora DSQL CDC streams the results of insert, update, and delete operations as change events to Amazon Kinesis Data Streams. You can use it to synchronize data across microservices, trigger Lambda functions, or deliver changes to S3, Redshift, and OpenSearch Service through Amazon Data Firehose. CDC streaming is designed to have zero impact on database workload performance and requires no infrastructure to manage. For a full list of AWS announcements, be sure to keep an eye on the What’s New with AWS page. Other AWS news Here are some additional posts you may find useful: Building secure AI agents at scale: Introducing Loom for AWS – Loom is an open-source enterprise platform for building agents with AWS Strands Agents and deploying them on Amazon Bedrock AgentCore Runtime. It provides a unified management UI and backend API with identity provider integration, scope-based authorization, multi-persona navigation, and full lifecycle management for agents, memory, MCP servers, and agent-to-agent integrations. Loom enforces automated resource tagging for cost attribution, implements RBAC and ABAC for multi-tenant security, uses paved-path blueprints for agent deployments, manages identity propagation through delegated actor chains, integrates with AWS Agent Registry for discovery and governance, and supports human-in-the-loop review before sensitive actions. The project is available in AWS Labs on GitHub. Introducing Claude apps gateway for AWS – The Claude apps gateway is a self-hosted control plane that gives organizations centralized control over access, cost, and policy for Claude Code and Claude Desktop. It connects to any OIDC-compliant identity provider, enforces managed settings on every request, routes inference to Amazon Bedrock or Claude Platform on AWS, and supports per-user and per-group spend caps. The gateway runs as a stateless container in your private network, backed by a PostgreSQL database for short-lived sign-in state. No long-lived secrets are stored on developer machines. Deploy it through Amazon Bedrock to keep data within the AWS security boundary, or through Claude Platform on AWS for the native Claude platform experience. Introducing OAuth support for AWS MCP Server – You can now connect agents to the AWS MCP Server using browser-based OAuth with the same credentials you use for the AWS Console or CLI. The new sign-in path supports IAM federation, AWS IAM Identity Center, and root or IAM users. AWS Sign-In issues short-lived access tokens and refresh tokens, with automatic token management so developers stay authenticated across restarts. For headless use cases, a non-interactive flow lets applications with existing AWS credentials obtain OAuth access tokens through the create-oauth2-token-with-iam API. New governance controls include OAuth-specific IAM condition keys, token introspection and revocation, dynamic client registration, and CloudTrail audit elements. For a full list of AWS blog posts, be sure to keep an eye on the AWS Blogs page. Upcoming AWS events Check your calendar and sign up for upcoming AWS events: AWS Summits – Free in-person events for builders and innovators to learn, think big, and make new connections. Coming up: Taipei (July 15), Bogotá (July 30), Jakarta (August 6), Ciudad de México (August 12), Johannesburg (August 19), and Zurich (September 2). AWS Community Days – Community-led conferences planned and delivered by community leaders. Upcoming events include Yaoundé, Cameroon (July 25), Ahmedabad, India (July 25), Belo Horizonte, Brazil (August 22), Ottawa, Canada (August 22), Tulsa, USA (August 22), and Toronto, Canada (August 29). Visit the AWS Builder Center to meet other builders, contribute solutions, and find resources that help you keep building. Wishing everyone a restful and enjoyable summer. Whether you’re building, learning, or recharging, I hope you find time for all three. I’ll be heading to Scandinavia for a few weeks to trade the heat for some cooler weather and longer evenings. Come back next week for more news! — Esra

</details>

