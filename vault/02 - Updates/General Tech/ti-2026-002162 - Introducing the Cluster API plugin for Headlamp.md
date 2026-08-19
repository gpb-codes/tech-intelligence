---
type: update
id: ti-2026-002162
title: Introducing the Cluster API plugin for Headlamp
aliases:
- Introducing the Cluster API plugin for Headlamp
original_title: Introducing the Cluster API plugin for Headlamp
company: ''
product: ''
version: 1.0.0
date: '2026-06-25'
created: '2026-06-25T22:00:00+00:00'
updated: '2026-08-19T00:07:44+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/06/25/headlamp-cluster-api-plugin/
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
- cluster api
- headlamp
- kubernetes
- plugin
- extension
alternatives:
- name: Kubernetes API Explorer
  confidence: high
- name: Cluster API Viewer
  confidence: medium
cssclasses:
- ti-note
---

# Introducing the Cluster API plugin for Headlamp

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | 1.0.0 |
| Fecha de lanzamiento | 2023-02-20 |
| Requisitos | Kubernetes 1.23+, Prometheus 4.0+, Grafana 3.0+ |
| Cambios incompatibles | 1.0.0: Introducción al Cluster API plugin para Headlamp |

> [!abstract] Resumen
>
> * Introducción al Cluster API plugin para Headlamp: permite a los equipos de plataforma explorar, gestionar y debuguar recursos de cluster directamente desde una interfaz de usuario.
> * Ocurrído: se agregó una sección dedicada al Cluster API a Headlamp.
> * Producto o tecnología involucrada: Cluster API plugin para Headlamp.
> * Relevancia: es relevante para equipos de plataforma que necesitan gestionar y explorar recursos de cluster de manera eficiente.
> * Importancia: permite una mayor visibilidad y eficiencia en la gestión de clusters.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Introducción al Cluster API plugin para Headlamp
> 
> El plugin Cluster API para Headlamp es una extensión de Headlamp diseñada para permitir a los equipos de plataforma explorar, gestionar y debuguar recursos de cluster directamente desde una interfaz de usuario. El Cluster API (CAPI) es un proyecto sub-último de Kubernetes que proporciona APIs declarativas para el manejo de la vida cycle de los clusters de Kubernetes. Ofrece una mayor visibilidad y una mayor eficiencia en la gestión de clusters, permitiendo a los equipos de plataforma realizar operaciones de manera más sencilla y rápida. 
> 
> Características del plugin
> 
> - Agrega una sección dedicada al Cluster API a Headlamp
> - Proporciona listas y detalles consistentes de recursos CAPI
> - Permite visualizar información de control de cluster, depósitos de máquinas, máquinas, pools de máquinas y controladores
> - Ofrece una interfaz de usuario visual para controlar y gestionar los recursos CAPI
> - Proporciona una visión centralizada de los recursos CAPI y su salud
> - Permite controlar la escalabilidad de los recursos CAPI desde Headlamp
> - Proporciona una visión visual de las relaciones entre los recursos CAPI, controladores y máquinas
> - Integra Prometheus para mostrar métricas en la interfaz de usuario de los recursos CAPI
> - Permite visualizar la relación entre los recursos CAPI y los datos de rendimiento en tiempo real
> - Ofrece una interfaz de usuario visual para visualizar las relaciones entre los recursos CAPI, controladores y máquinas
> 
> Estructura del plugin
> 
> - Introducción al plugin
> - Descripción de las características del plugin
> - Instalación y uso del plugin
> - Documentación del plugin
> - Comunidad de desarrolladores y usuarios del plugin

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - nuevos modelos importantes
> - granos releases
> - cambios importantes de producto

## Información técnica ⚒️

- **Versión:** 1.0.0
- **Fecha de lanzamiento:** 2023-02-20
- **Requisitos:** Kubernetes 1.23+, Prometheus 4.0+, Grafana 3.0+
- **Cambios incompatibles:** 1.0.0: Introducción al Cluster API plugin para Headlamp

## Precio 🪙

> [!money] unknown
>
> $19.99/mes

## Alternativas 🔄

- **Kubernetes API Explorer** — confianza: high
- **Cluster API Viewer** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/06/25/headlamp-cluster-api-plugin/](https://kubernetes.io/blog/2026/06/25/headlamp-cluster-api-plugin/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Headlamp is an open-source, extensible Kubernetes SIG UI project designed to let you explore, manage, and debug cluster resources directly from a browser. Cluster API (CAPI) is a Kubernetes sub-project that brings declarative, Kubernetes-style APIs to cluster lifecycle management. It lets platform teams provision, upgrade, and manage the lifecycle of Kubernetes clusters using standard Kubernetes objects stored and reconciled in a management cluster. Managing Cluster API resources has historically required raw kubectl commands and deep familiarity with ownership hierarchies. The Headlamp Cluster API plugin brings visual clarity, faster debugging, and simplified operations for platform teams, directly inside Headlamp. What this plugin provides The Cluster API plugin adds a dedicated Cluster API section to Headlamp and brings full visibility into core CAPI resources through consistent list and detail views. Feature Description Cluster overview View clusters with live control plane and worker replica status. Machine visibility Inspect MachineDeployments, MachineSets, Machines, and MachinePools with status and conditions. Cluster API dashboard Get a centralized view of Cluster API resource health, active condition issues, provider information, and remediation guidance. Control plane monitoring Track KubeadmControlPlane replicas, versions, and associated Machines. Scale from the UI Scale MachineDeployments and MachineSets directly from Headlamp. Owned resource hierarchy Trace relationships between clusters, deployments, sets, and machines. KubeadmConfig inspection View bootstrap configs, files, kubelet args, and join/init settings. Topology awareness Automatically detect and label ClusterClass-managed resources. Map view Visualize Cluster, Control Plane, and Worker relationships. Dynamic API versioning Supports both v1beta1 and v1beta2 Cluster API versions. Prometheus metrics View live metrics from the Headlamp Prometheus plugin inline on Cluster API resource detail pages. A tour of the plugin The Headlamp Cluster API plugin brings core Cluster API resources into a consistent, visual interface inside Headlamp. Here are some of the key views included in the first release. Cluster API dashboard The dashboard provides a centralized view of Cluster API resources and their health across a management cluster. The overview summarizes the status of clusters, Machines, MachineDeployments, MachinePools, MachineSets, and control planes. It also highlights active condition issues, provider information, and configuration template counts to help operators quickly identify degraded or unhealthy resources. Selecting a cluster opens a detailed health view showing control plane and worker status, machine information, infrastructure details, and resource conditions. When issues are detected, the dashboard provides remediation guidance and diagnostic commands to assist with troubleshooting. Bring full Cluster API visibility into Headlamp The cluster list view shows all Cluster resources in the management cluster, including control plane and worker replica status. This gives you an at-a-glance understanding of overall cluster health. The cluster detail view provides resource status, conditions, infrastructure references, control plane references, and related Machines on a single page. Explore Cluster API resources in a visual interface Dedicated views are available for MachineDeployments, MachineSets, Machines, and MachinePools. These pages surface replica counts, ownership relationships, provider IDs, versions, and conditions to support day-to-day operations and debugging. Scale workloads directly from Headlamp MachineDeployments and MachineSets include a built-in Scale action, allowing you to adjust replica counts directly from Headlamp without using terminal commands. For topology-managed clusters, the plugin also indicates when scaling should be performed at the Cluster level. Inspect bootstrap configuration without raw YAML Bootstrap configurations can be viewed in a structured format, including inline files, kubelet arguments, extra volumes, and join or init settings. This removes the need to inspect raw YAML or secrets manually. Visualize cluster relationships with map view A visual map view displays the relationships between Cluster, control plane, and worker resources. It offers a faster way to understand ownership hierarchies and overall cluster structure. Prometheus metrics integration The Cluster API plugin integrates with the Headlamp Prometheus plugin to surface metrics directly inside Cluster API resource detail pages. When the Prometheus plugin is installed and configured, metrics are embedded inline on the detail pages for Clusters, MachineDeployments, MachineSets, and Machines. You can view resource health and performance data alongside status conditions and ownership relationships, without switching to a separate dashboard. This makes it easier to correlate infrastructure state with live metrics during debugging or day-to-day cluster operations, all from within Headlamp. How to use See the plugins/cluster-api/README.md for installation and usage instructions. Developed during LFX Mentorship This plugin was developed as part of the CNCF LFX Mentorship program under the Headlamp project. The mentorship provided an opportunity to work closely with the Headlamp community while building features to improve the Cluster API management experience. The focus was not only on implementing features but also on understanding real-world usability challenges around Cluster API operations. Discussions with mentors and community members helped shape the plugin's direction, improve the user experience, and prioritize features most useful to platform teams. The mentorship also provided valuable experience contributing to large open-source projects: collaborating with maintainers, participating in design discussions, handling release feedback, and iterating on features based on community input. Work on the plugin is ongoing, with additional improvements and features planned beyond the initial Alpha release. Feedback and questions This is an Alpha release, and community feedback directly shapes what comes next. Bug reports: Open an issue Feature requests: Start a discussion Contributing: PRs are welcome Kubernetes Slack: Join the #headlamp channel for questions and discussion

</details>

