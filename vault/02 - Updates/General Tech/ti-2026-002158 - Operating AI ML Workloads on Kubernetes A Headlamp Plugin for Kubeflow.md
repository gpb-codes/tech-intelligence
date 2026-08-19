---
type: update
id: ti-2026-002158
title: 'Operating AI/ML Workloads on Kubernetes: A Headlamp Plugin for Kubeflow'
aliases:
- 'Operating AI/ML Workloads on Kubernetes: A Headlamp Plugin for Kubeflow'
original_title: 'Operating AI/ML Workloads on Kubernetes: A Headlamp Plugin for Kubeflow'
company: ''
product: ''
version: ''
date: '2026-07-13'
created: '2026-07-13T20:00:00+00:00'
updated: '2026-08-19T18:09:47+00:00'
original_language: en
translated: true
importance: high
impact: medium
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/07/13/introducing-headlamp-plugin-for-kubeflow/
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
- name: Kubernetes Cluster Management Tools
  confidence: high
- name: Kubeflow Plugin for Kubernetes
  confidence: medium
cssclasses:
- ti-note
---

# Operating AI/ML Workloads on Kubernetes: A Headlamp Plugin for Kubeflow

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🌐 Medio`

> [!abstract] Resumen
>
> * Operaciones de trabajo de AI/ML en clusters Kubernetes: 
>   - Plugin de Headlamp para Kubeflow
> * Introducción al plugin Headlamp
> * Descripción del plugin Headlamp
> * Ventajas del plugin Headlamp
> * Uso del plugin Headlamp
> * Patrones de implementación de CRDs
> * Uso de Headlamp en otros plataformas
> * Desarrollo del plugin Headlamp
> * Licencia del plugin Headlamp
> * Uso del plugin Headlamp en la comunidad de Kubeflow

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Operaciones de trabajo de AI/ML en clusters Kubernetes: Plugin de Headlamp para Kubeflow
> 
> Las reglas:
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
> - Operaciones de trabajo de AI/ML en clusters Kubernetes
> - Plugin de Headlamp para Kubeflow
> - Introducción al plugin Headlamp
> - Descripción del plugin Headlamp
> - Ventajas del plugin Headlamp
> - Uso del plugin Headlamp
> - Patrones de implementación de CRDs
> - Uso de Headlamp en otros plataformas
> - Desarrollo del plugin Headlamp
> - Licencia del plugin Headlamp
> - Uso del plugin Headlamp en la comunidad de Kubeflow

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Mantener el significado
> - No inventar información
> - No agregar información

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> Headlamp es un plugin de Kubeflow diseñado para operar operaciones de trabajo de AI/ML en clusters Kubernetes, permitiendo a los desarrolladores automatizar y optimizar las operaciones de trabajo de inteligencia artificial y aprendizaje automático en entornos de cluster Kubernetes.

> [!tip] ¿En qué ayuda al desarrollo?
>
> El plugin Headlamp ayuda a los desarrolladores a automatizar y optimizar las operaciones de trabajo de AI/ML en clusters Kubernetes, lo que puede mejorar la productividad y reducir el tiempo de desarrollo.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | C · r · e |
| Junior | Media | C · r · e |
| Semi-Senior | Baja | C · r · e |
| Senior | Alta | C · r · e |
| Ingeniero de Software | Alta | C · r · e |
| Ingeniero en Redes | Alta | C · r · e |
| DevOps / SRE | Alta | C · r · e |
| Ciberseguridad | Baja | C · r · e |


## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Alternativas 🔄

- **Kubernetes Cluster Management Tools** — confianza: high
- **Kubeflow Plugin for Kubernetes** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/07/13/introducing-headlamp-plugin-for-kubeflow/](https://kubernetes.io/blog/2026/07/13/introducing-headlamp-plugin-for-kubeflow/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Kubernetes has quietly become the default platform for AI and machine learning. Whether you run notebook servers for data scientists, schedule distributed training jobs, tune hyperparameters, or orchestrate multi-step ML pipelines, those workloads increasingly land on a Kubernetes cluster. Kubeflow is one of the most popular ways to assemble that stack, and it does so the Kubernetes-native way: every capability is exposed as a Custom Resource Definition (CRD). That design is a gift to cluster operators, because it means ML workloads can be observed and managed with the same primitives as everything else in the cluster. But in practice the specialized ML dashboards that ship with these platforms hide the Kubernetes layer underneath. When a notebook is stuck or a training run fails, the operator is often left dropping back to kubectl to find out what actually happened at the Pod level. This post introduces the Headlamp Kubeflow plugin , which closes that gap by surfacing Kubeflow's custom resources directly inside a general-purpose Kubernetes UI. It is a worked example of a pattern any CRD-heavy platform can follow: meet operators where they already work, and show them the cluster-level truth. Headlamp itself is an extensible Kubernetes web UI maintained under Kubernetes SIG UI and licensed under Apache 2.0. It runs as a desktop app or in-cluster, and its plugin system lets anyone add first-class views for custom resources. Why operators need a different view Purpose-built ML dashboards help data scientists submit experiments, pipelines, and notebooks. Cluster operators and site reliability engineers (SREs) troubleshoot the Kubernetes resources underneath, and they ask different questions: Why is a notebook stuck? Is it ImagePullBackOff , OOMKilled , or a Pod waiting on a PersistentVolumeClaim? Which Run resources failed recently across namespaces? Which parameter set does a Katib Experiment report as optimal? Do TrainJob resources reference the expected TrainingRuntime resources? Which batch workloads are running, and what state does Kubernetes report? The Headlamp Kubeflow plugin helps answer these questions by reading directly from the Kubernetes API server. It shows Pod conditions, Kubernetes failure reasons, and resources across namespaces without requiring an intermediary ML service or database. What the plugin covers Kubeflow is modular, and teams often install only the components they need. The plugin discovers the Kubeflow API groups on a cluster and displays only the corresponding sections. The plugin supports the following component families and API resources: Kubeflow components and API resources supported by the Headlamp plugin Component Purpose API resources Notebooks Provides development environments such as Jupyter, VS Code, and RStudio Notebook, Profile, PodDefault Pipelines Defines and tracks pipelines, versions, experiments, runs, and schedules Pipeline, PipelineVersion, Run, RecurringRun, Experiment Katib Automates hyperparameter tuning and neural architecture search Experiment, Trial, Suggestion Training Runs distributed training workloads such as PyTorch and TensorFlow jobs TrainJob, TrainingRuntime, ClusterTrainingRuntime Spark Runs large-scale data processing with Apache Spark SparkApplication, ScheduledSparkApplication What you can see Inspect notebook Pods The Notebook detail view shows Pod conditions and their reason and message fields. It also shows CPU, memory, and GPU requests and limits; volume mounts and their backing types, such as PersistentVolumeClaim, ConfigMap, Secret, or emptyDir ; environment variables that reference Secret or ConfigMap objects; sidecar containers; and node tolerations. This view consolidates information that would otherwise require several kubectl describe commands. Inspect hyperparameter tuning The Katib views show the tuning algorithm, search space, every Trial with its live status, and the current best Trial with its metric values and parameter assignments. They also show the early-stopping configuration and the number of Trial resources that stopped early, so you can follow the search without leaving the cluster UI. Inspect pipeline state without the backend database The Pipelines views read Kubernetes API resources directly and do not query the Kubeflow Pipelines API service or backend database. You can inspect stored pipeline state even when that service is unavailable. The Pipeline detail view compares the latest and previous PipelineVersion specifications in a side-by-side YAML diff. Run views show state and duration, RecurringRun views show human-readable schedules, and the artifacts view aggregates pipelineRoot values from recent Run resources. Map ML resources The plugin registers a Headlamp map source that renders Notebook, Profile, PodDefault, Experiment, Pipeline, SparkApplication, and TrainJob resources as graph nodes. It draws edges between supported resources based on .metadata.ownerReferences . Headlamp also shows inline summaries for these resource types when you hover over them. Try it The Kubeflow plugin README explains installation and local-cluster setup, including a lightweight CRD-only path for evaluation. Because the plugin discovers installed API groups, you can use it with an existing modular Kubeflow installation or create an evaluation cluster with only the CRDs and sample resources. Apply the pattern to other platforms Kubeflow illustrates a broader pattern. Platforms often model domain-specific workflows with custom resources. Their dashboards focus on those workflows, while Kubernetes operators also need the state of the underlying API resources and Pods. A CRD-driven plugin in a general Kubernetes UI can expose that state without making operators switch between unrelated tools. The plugin uses the Apache 2.0 license and is developed under Kubernetes SIG UI. To report a problem or contribute an improvement, use the Headlamp plugins repository's issue tracker or pull requests .

</details>

