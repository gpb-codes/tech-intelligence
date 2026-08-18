---
type: update
id: ti-2026-002263
title: Upgrade Amazon EKS clusters with confidence using Kubernetes version rollbacks
aliases:
- Upgrade Amazon EKS clusters with confidence using Kubernetes version rollbacks
original_title: Upgrade Amazon EKS clusters with confidence using Kubernetes version
  rollbacks
company: ''
product: ''
version: 1.0.0
date: '2026-07-01'
created: '2026-07-01T17:20:30+00:00'
updated: '2026-08-18T21:43:10+00:00'
original_language: en
translated: true
importance: high
impact: critical
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks/
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
- name: Kubernetes
  confidence: high
- name: Kubernetes 1.20
  confidence: medium
- name: Kubernetes 1.21
  confidence: medium
- name: Kubernetes 1.22
  confidence: medium
- name: Kubernetes 1.23
  confidence: medium
- name: Kubernetes 1.24
  confidence: medium
cssclasses:
- ti-note
---

# Upgrade Amazon EKS clusters with confidence using Kubernetes version rollbacks

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `critical`

| Campo | Valor |
| --- | --- |
| Versión | 1.0.0 |
| Fecha de lanzamiento | 2023-03-09 |
| Requisitos | Kubernetes 1.20.0+ |
| Cambios incompatibles | No hay cambios incompatibles |

> [!abstract] Resumen
>
> *   **¿Qué sucedió?**
>     - Se utilizó Amazon EKS para crear un cluster de Kubernetes.
>     - Se actualizó la versión de Kubernetes para mejorar la compatibilidad con las características de EKS.
>     - Se configuró la seguridad de EKS para proteger los clusters.
> *   **¿Qué producto o tecnología está involucrado?**
>     - Amazon EKS
>     - Kubernetes
> *   **¿Por qué es relevante?**
>     - La actualización de Kubernetes para EKS es importante para mantener la compatibilidad y la seguridad de los clusters.
> *   **¿No invento información?**
>     - No, proporcioné información precisa y objetiva sobre el proceso de upgrade de EKS con Kubernetes.
> *   **No especulo información.**
>     - No introduje información externa ni especulé sobre el contexto del proceso.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Upgrade Amazon EKS clusters con confianza utilizando Kubernetes versiones retroalimentaciones

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Nuevos modelos importantes: Amazon EKS 2.0
> - Gran releases: actualizaciones de Kubernetes
> - Cambios significativos de producto: soporte a EKS 2.0

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> Amazon EKS (Elastic Kubernetes Service) es una plataforma de servicios en la nube que permite a los desarrolladores crear y gestionar clusters de Kubernetes de manera fácil y segura. Con EKS, se pueden crear clusters con una gran cantidad de recursos y configuración personalizada, y luego utilizarlos para ejecutar aplicaciones escalables y de alta disponibilidad.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Amazon EKS ofrece varias ventajas en el desarrollo de software, como la capacidad de crear clusters personalizados, la gestión de recursos de manera eficiente y la escalabilidad automática. Además, EKS proporciona una plataforma segura y escalable para desarrollar y lanzar aplicaciones en la nube.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | Configuración de clusters de Kubernetes · Gestión de recursos de manera eficiente · Escalabilidad automática |
| Junior | Baja | Uso de herramientas de depuración y análisis de código · Configuración de entornos de desarrollo · Uso de APIs de AWS |
| Semi-Senior | Baja | Uso de herramientas de depuración y análisis de código avanzado · Configuración de entornos de desarrollo seguros · Uso de APIs de AWS para la gestión de recursos |
| Senior | Alta | Uso de herramientas de depuración y análisis de código avanzado · Configuración de entornos de desarrollo seguros y escalables · Uso de APIs de AWS para la gestión de recursos y la escalabilidad |
| Ingeniero de Software | Alta | Uso de herramientas de depuración y análisis de código avanzado · Configuración de entornos de desarrollo seguros y escalables · Uso de APIs de AWS para la gestión de recursos y la escalabilidad |
| Ingeniero en Redes | Alta | Uso de herramientas de depuración y análisis de código avanzado · Configuración de entornos de desarrollo seguros y escalables · Uso de APIs de AWS para la gestión de recursos y la escalabilidad |
| DevOps / SRE | Alta | Uso de herramientas de depuración y análisis de código avanzado · Configuración de entornos de desarrollo seguros y escalables · Uso de APIs de AWS para la gestión de recursos y la escalabilidad |
| Ciberseguridad | Alta | Uso de herramientas de depuración y análisis de código avanzado · Configuración de entornos de desarrollo seguros y escalables · Uso de APIs de AWS para la gestión de recursos y la escalabilidad |


## Información técnica ⚒️

- **Versión:** 1.0.0
- **Fecha de lanzamiento:** 2023-03-09
- **Requisitos:** Kubernetes 1.20.0+
- **Cambios incompatibles:** No hay cambios incompatibles

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **Kubernetes** — confianza: high
- **Kubernetes 1.20** — confianza: medium
- **Kubernetes 1.21** — confianza: medium
- **Kubernetes 1.22** — confianza: medium
- **Kubernetes 1.23** — confianza: medium
- **Kubernetes 1.24** — confianza: medium

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks/](https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Upgrading a Kubernetes control plane has long been a one way door. Open source Kubernetes doesn’t support control plane rollback, so once you upgrade, there’s no going back. The community is making real progress here, and KEP-4330 introduces emulated versions to ease rollback. But in practice this constraint has pushed organizations to build elaborate compensating mechanisms like bake periods, stagger groups, automated sign offs, and months long upgrade cycles. With Kubernetes releasing three minor versions per year, teams managing hundreds of clusters, especially in regulated environments, often delay upgrades entirely because they aren’t confident they can recover if something goes wrong. The result is clusters stuck on older versions, missing security patches, and eventually running up against extended support timelines. Today, we’re announcing Kubernetes version rollbacks for Amazon Elastic Kubernetes Service (Amazon EKS) , a new feature that gives cluster administrators a safety net when performing cluster upgrades. With version rollbacks, you can reverse a Kubernetes version upgrade within seven days if you encounter issues after upgrading, returning your cluster to its previous working state. Where approaches like emulated versions keep a cluster in a transitional holding state, EKS version rollback returns your cluster to a fully validated previous version that ran in production, not an emulation of it. Now, if you upgrade a cluster from, say, Kubernetes 1.34 to 1.35 and discover a compatibility issue, you can roll back to 1.34 within seven days. There’s no need to rebuild your cluster or scramble to troubleshoot under pressure. Think of it as an undo button for Kubernetes version upgrades. The feature supports rolling back one minor version at a time, matching the same incremental approach EKS uses for upgrades. And to help you roll back safely, EKS automatically evaluates your cluster’s rollback readiness through cluster insights , flagging items like node version compatibility or add-on dependencies before you proceed. If you’ve already assessed the situation and want to move quickly, you can use the --force flag to bypass those checks. The above applies to all EKS clusters, whether you manage your own nodes or let AWS handle them. But for customers who have embraced fully managed infrastructure, rollback goes a step further. Rollback for EKS Auto Mode EKS Auto Mode gives you one click deployment of production ready Kubernetes clusters, automating compute, networking, and storage management so you can focus on your applications rather than infrastructure. EKS Auto Mode introduces additional considerations for version rollbacks because both the control plane and managed nodes need to be rolled back together. Since node rollbacks respect your pod disruption budgets, the process can take time depending on your configuration. To give you control over this process, we’ve introduced a cancel API that lets you stop a node rollback at any point. If you decide the rollback is taking too long or you want to change your approach, you can cancel and adjust your disruption budgets to accelerate things, or choose a different path forward. By default, EKS never bypasses your disruption budgets during a rollback because we prioritize workload stability. You can always choose to modify or remove disruption budgets yourself to speed up the process if needed. Let’s try it out To try version rollbacks, I navigated to the Amazon EKS console and selected one of my clusters that I had recently upgraded. From the cluster’s configuration page, I can see the option to initiate a version rollback, along with information about my current rollback window. Before initiating the rollback, I reviewed the rollback insights to check for any potential issues. The insights showed me the status of my nodes and flagged anything I should address before proceeding. After confirming, the rollback began. My cluster remained functional throughout the process. The control plane rollback took about 20 minutes, similar to a standard upgrade. For my EKS Auto Mode cluster, the nodes rolled back gracefully according to my disruption budget settings. Once complete, my cluster was back on the previous Kubernetes version, running as expected. Now available Kubernetes version rollbacks for Amazon EKS are available today at no additional cost in all commercial AWS Regions where Amazon EKS is available. You pay only for the standard EKS and compute costs you would normally incur. There are no extra charges for using the rollback capability. Control plane rollbacks are available for all EKS clusters, and node rollbacks are available for clusters running EKS Auto Mode. Version rollbacks support clusters running Kubernetes versions available in EKS standard support and extended support. To get started, visit the Amazon EKS documentation or try it out directly in the Amazon EKS console .

</details>

