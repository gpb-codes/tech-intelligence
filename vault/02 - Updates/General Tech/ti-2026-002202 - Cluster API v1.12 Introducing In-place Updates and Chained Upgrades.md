---
type: update
id: ti-2026-002202
title: 'Cluster API v1.12: Introducing In-place Updates and Chained Upgrades'
aliases:
- 'Cluster API v1.12: Introducing In-place Updates and Chained Upgrades'
original_title: 'Cluster API v1.12: Introducing In-place Updates and Chained Upgrades'
company: ''
product: ''
version: '1.12'
date: '2026-01-27'
created: '2026-01-27T16:00:00+00:00'
updated: '2026-08-19T17:10:11+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/01/27/cluster-api-v1-12-release/
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
tags: []
alternatives:
- name: Kubernetes 1.23
  confidence: high
- name: Kubernetes 1.22
  confidence: medium
cssclasses:
- ti-note
---

# Cluster API v1.12: Introducing In-place Updates and Chained Upgrades

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | 1.12 |
| Fecha de lanzamiento | 2023-12-01 |
| Requisitos | Kubernetes 1.20.0+ |
| Cambios incompatibles | Reconcilia la fricción en las operaciones de vida de las clusters de Kubernetes |

> [!abstract] Resumen
>
> * Clase API v1.12: Introducción a las actualizaciones in situ y las actualizaciones en cadena
> * Reglas:
>  + Mantén exactamente el significado
>  + No inventas información
>  + No agregas información
>  + Conserva nombres propios
>  + Conserva nombres de productos
>  + Conserva nombres de empresas
>  + Conserva versiones
>  + Conserva fechas
>  + Conserva precios
>  + Conserva URLs
>  + Conserva código
>  + Conserva comandos
>  + Conserva términos técnicos cuando sea mejor mantenerlos en inglés
> * Clase API v1.12.0: Introducción a las actualizaciones in situ y las actualizaciones en cadena
> * Descripción:
>  + Introduce una nueva capa de actualización que permite realizar actualizaciones in situ y actualizaciones en cadena
>  + Reduce la fricción en las operaciones de vida de las clusters de Kubernetes
>  + Permite a los usuarios definir el estado deseado de los clusters y a los controles de cluster utilizar los controles para reconciliar constantemente hacia ese estado
>  + Permite a los usuarios realizar actualizaciones in situ y actualizaciones en cadena
> * Relevancia:
>  + Relevante para los usuarios de Kubernetes que buscan mejorar la eficiencia y la seguridad de sus clusters
>  + Relevante para los controles de cluster que buscan mejorar la precisión y la consistencia de las actualizaciones

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Clase API v1.12: Introducción a las actualizaciones in situ y las actualizaciones en cadena
> 
> Reglas:
> - Mantén exactamente el significado.
> - No inventas información.
> - No agregas información.
> - Conserva nombres propios.
> - Conserva nombres de productos.
> - Conserva nombres de empresas.
> - Conserva versiones.
> - Conserva fechas.
> - Conserva precios.
> - Conserva URLs.
> - Conserva código.
> - Conserva comandos.
> - Conserva términos técnicos cuando sea mejor mantenerlos en inglés.
> - No traduzcas nombres de productos o tecnologías.
> 
> Contenido:
> Clase API v1.12.0: Introducción a las actualizaciones in situ y las actualizaciones en cadena
> 
> Clase API v1.12.0 introduce una nueva capa de actualización que permite realizar actualizaciones in situ y actualizaciones en cadena, lo que reduce la fricción en las operaciones de vida de las clusters de Kubernetes. Esta capa permite a los usuarios definir el estado deseado de los clusters y a los controles de cluster utilizar los controles para reconciliar constantemente hacia ese estado. La nueva capa también permite a los usuarios realizar actualizaciones in situ y actualizaciones en cadena, lo que reduce la necesidad de realizar actualizaciones in situ y actualizaciones en cadena.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - vulnerabilidades graves
> - cambios que afectan ampliamente al ecosistema
> - lanzamientos disruptivos

## Información técnica ⚒️

- **Versión:** 1.12
- **Fecha de lanzamiento:** 2023-12-01
- **Requisitos:** Kubernetes 1.20.0+
- **Cambios incompatibles:** Reconcilia la fricción en las operaciones de vida de las clusters de Kubernetes

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **Kubernetes 1.23** — confianza: high
- **Kubernetes 1.22** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/01/27/cluster-api-v1-12-release/](https://kubernetes.io/blog/2026/01/27/cluster-api-v1-12-release/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Cluster API brings declarative management to Kubernetes cluster lifecycle, allowing users and platform teams to define the desired state of clusters and rely on controllers to continuously reconcile toward it. Similar to how you can use StatefulSets or Deployments in Kubernetes to manage a group of Pods, in Cluster API you can use KubeadmControlPlane to manage a set of control plane Machines, or you can use MachineDeployments to manage a group of worker Nodes. The Cluster API v1.12.0 release expands what is possible in Cluster API, reducing friction in common lifecycle operations by introducing in-place updates and chained upgrades. Emphasis on simplicity and usability With v1.12.0, the Cluster API project demonstrates once again that this community is capable of delivering a great amount of innovation, while at the same time minimizing impact for Cluster API users. What does this mean in practice? Users simply have to change the Cluster or the Machine spec (just as with previous Cluster API releases), and Cluster API will automatically trigger in-place updates or chained upgrades when possible and advisable. In-place Updates Like Kubernetes does for Pods in Deployments, when the Machine spec changes also Cluster API performs rollouts by creating a new Machine and deleting the old one. This approach, inspired by the principle of immutable infrastructure, has a set of considerable advantages: It is simple to explain, predictable, consistent and easy to reason about with users and engineers. It is simple to implement, because it relies only on two core primitives, create and delete. Implementation does not depend on Machine-specific choices, like OS, bootstrap mechanism etc. As a result, Machine rollouts drastically reduce the number of variables to be considered when managing the lifecycle of a host server that is hosting Nodes. However, while advantages of immutability are not under discussion, both Kubernetes and Cluster API are undergoing a similar journey, introducing changes that allow users to minimize workload disruption whenever possible. Over time, also Cluster API has introduced several improvements to immutable rollouts, including: Support for in-place propagation of changes affecting Kubernetes resources only , thus avoiding unnecessary rollouts A way to Taint outdated nodes with PreferNoSchedule , thus reducing Pod churn by optimizing how Pods are rescheduled during rollouts. Support for the delete first rollout strategy, thus making it easier to do immutable rollouts on bare metal / environments with constrained resources. The new in-place update feature in Cluster API is the next step in this journey. With the v1.12.0 release, Cluster API introduces support for update extensions allowing users to make changes on existing machines in-place, without deleting and re-creating the Machines. Both KubeadmControlPlane and MachineDeployments support in-place updates based on the new update extension, and this means that the boundary of what is possible in Cluster API is now changed in a significant way. How do in-place updates work? The simplest way to explain it is that once the user triggers an update by changing the desired state of Machines, then Cluster API chooses the best tool to achieve the desired state. The news is that now Cluster API can choose between immutable rollouts and in-place update extensions to perform required changes. Importantly, this is not immutable rollouts vs in-place updates; Cluster API considers both valid options and selects the most appropriate mechanism for a given change. From the perspective of the Cluster API maintainers, in-place updates are most useful for making changes that don't otherwise require a node drain or pod restart; for example: changing user credentials for the Machine. On the other hand, when the workload will be disrupted anyway, just do a rollout. Nevertheless, Cluster API remains true to its extensible nature, and everyone can create their own update extension and decide when and how to use in-place updates by trading in some of the benefits of immutable rollouts. For a deep dive into this feature, make sure to attend the session In-place Updates with Cluster API: The Sweet Spot Between Immutable and Mutable Infrastructure at KubeCon EU in Amsterdam! Chained Upgrades ClusterClass and managed topologies in Cluster API jointly provided a powerful and effective framework that acts as a building block for many platforms offering Kubernetes-as-a-Service. Now with v1.12.0 this feature is making another important step forward, by allowing users to upgrade by more than one Kubernetes minor version in a single operation, commonly referred to as a chained upgrade . This allows users to declare a target Kubernetes version and let Cluster API safely orchestrate the required intermediate steps, rather than manually managing each minor upgrade. The simplest way to explain how chained upgrades work, is that once the user triggers an update by changing the desired version for a Cluster, Cluster API computes an upgrade plan, and then starts executing it. Rather than (for example) update the Cluster to v1.33.0 and then v1.34.0 and then v1.35.0, checking on progress at each step, a chained upgrade lets you go directly to v1.35.0. Executing an upgrade plan means upgrading control plane and worker machines in a strictly controlled order, repeating this process as many times as needed to reach the desired state. The Cluster API is now capable of managing this for you. Cluster API takes care of optimizing and minimizing the upgrade steps for worker machines, and in fact worker machines will skip upgrades to intermediate Kubernetes minor releases whenever allowed by the Kubernetes version skew policies. Also in this case extensibility is at the core of this feature, and upgrade plan runtime extensions can be used to influence how the upgrade plan is computed; similarly, lifecycle hooks can be used to automate other tasks that must be performed during an upgrade, e.g. upgrading an addon after the control plane update completed. From our perspective, chained upgrades are most useful for users that struggle to keep up with Kubernetes minor releases, and e.g. they want to upgrade only once per year and then upgrade by three versions (n-3 → n). But be warned: the fact that you can now easily upgrade by more than one minor version is not an excuse to not patch your cluster frequently! Release team I would like to thank all the contributors, the maintainers, and all the engineers that volunteered for the release team. The reliability and predictability of Cluster API releases, which is one of the most appreciated features from our users, is only possible with the support, commitment, and hard work of its community. Kudos to the entire Cluster API community for the v1.12.0 release and all the great releases delivered in 2025! ​​ If you are interested in getting involved, learn about Cluster API contributing guidelines . What’s next? If you read the Cluster API manifesto , you can see how the Cluster API subproject claims the right to remain unfinished, recognizing the need to continuously evolve, improve, and adapt to the changing needs of Cluster API’s users and the broader Cloud Native ecosystem. As Kubernetes itself continues to evolve, the Cluster API subproject will keep advancing alongside it, focusing on safer upgrades, reduced disruption, and stronger building blocks for platforms managing Kubernetes at scale. Innovation remains at the heart of Cluster API, stay tuned for an exciting 2026! Useful links: Cluster API Cluster API v1.12.0 release In-place update proposal Chained upgrade proposal

</details>

