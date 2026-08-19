---
type: update
id: ti-2026-002184
title: 'Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta)'
aliases:
- 'Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta)'
original_title: 'Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta)'
company: ''
product: ''
version: '1.36'
date: '2026-04-27'
created: '2026-04-27T18:35:00+00:00'
updated: '2026-08-19T01:38:41+00:00'
original_language: en
translated: true
importance: medium
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/
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
- name: 'Kubernetes v1.35: Flexible Pod Resources for Suspended Jobs (beta)'
  confidence: medium
- name: 'Kubernetes v1.34: Flexible Pod Resources for Suspended Jobs (beta)'
  confidence: medium
- name: 'Kubernetes v1.33: Flexible Pod Resources for Suspended Jobs (beta)'
  confidence: medium
- name: 'Kubernetes v1.32: Flexible Pod Resources for Suspended Jobs (beta)'
  confidence: medium
cssclasses:
- ti-note
---

# Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta)

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟡 Media` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | 1.36 |
| Fecha de lanzamiento | 2023-04-23T150405.678 |
| Cambios incompatibles | Cambios incompatibles con los requisitos de recursos |

> [!abstract] Resumen
>
> *   **Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta)**: La característica permite modificar las solicitudes y límites de contenedores en el template de pod de una Job para suspenderla.
> *   **¿Por qué las recursos mutable para Jobs suspendidos?**: Los trabajos de batch y aprendizaje automático suelen tener requisitos de recursos que no son precisamente conocidos al momento de su creación del Job, lo que requiere ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido.
> *   **Involucrarse en este feature**: Se ha desarrollado por SIG Apps y se puede comunicar a través de los canales Slack channel #sig-apps y Slack channel #wg-batch.
> *   **Involucrarse en este problema**: El problema de KEP-5440.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta)
> 
> Kubernetes v1.36 promueve la capacidad de modificar las solicitudes y límites de contenedores en el template de pod de una Job para suspenderla. Esta característica se introdujo como alpha en v1.35 y permite a los controladores de recursos de la red ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido, antes de que comience o se resuma. ¿Por qué las recursos mutable para Jobs suspendidos? Los trabajos de batch y aprendizaje automático suelen tener requisitos de recursos que no son precisamente conocidos al momento de su creación del Job. La asignación de recursos óptima depende de la capacidad del cluster actual, prioridades de la cola y la disponibilidad de hardware especializado como GPUs. Antes de esta característica, las requisitos de recursos en el template de Job estaban fijos una vez que se habían establecido. Si un controlador de recursos de la red determinaba que una Job suspendida debía ejecutar con recursos diferentes, la única opción era eliminar y recrear la Job, perdiendo cualquier asociación de metadata, status o historia. Esta característica también proporciona una forma de permitir que un Job específico de una CronJob progrese lentamente con recursos reducidos en lugar de fracasar si el cluster está muy cargado. Considera un Job de aprendizaje automático que inicialmente requiere 4 GPUs: apiVersion: batch/v1 kind: Job metadata: nombre: training-job-example-abcd123 etiquetas: app.kubernetes.io/name: trainer spec: suspender: true template: metadata: annotations: kubernetes.io/description: "Aprendizaje automático, ID abcd123" spec: contenedores: - nombre: trainer imagen: example-registry.example.com/training:2026-04-23T150405.678 recursos: requests: cpu: "8" memoria: "32Gi" ejemplo-hardware-vendor.com/gpu: "4" limites: cpu: "8" memoria: "32Gi" ejemplo-hardware-vendor.com/gpu: "4" restartPolicy: Never Un cambiar de Job que estaba suspendido puede esperar que todas las Pods de ese Job estén terminando antes de modificar las recursos. El servidor de API rechaza las modificaciones de recursos mientras la actividad de los Pods sea mayor que cero. Política de reemplazo de Pods Considera establecer la política de reemplazo de Pods si los Jobs que se suspenden pueden tener Pods fallidos. La política de reemplazo de Pods asegura que los Pods de reemplazo se crean solo después de que los Pods anteriores hayan terminado completamente, evitando la contención de recursos entre Pods. Alcance de la DRA (Resource Claims) (DRAC) recursosClaimTemplates permanecen inmutables si se utilizan. Si tu trabajo utiliza DRAC, debes recrear las templates de reclamo de recursos separadamente para coincidir con las modificaciones de recursos. Involucrarse En este feature se desarrolló por SIG Apps. Se ha recibido feedback de ambos grupos y se puede comunicar a través de los siguientes canales: Slack channel #sig-apps . Slack channel #wg-batch . El problema de KEP-5440.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Nuevos modelos importantes
> - Granos releases
> - Cambios significativos de producto

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta) es una característica de Kubernetes que permite a los controladores de recursos de la red modificar las solicitudes y límites de contenedores en el template de pod de una Job para suspenderla.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Kubernetes v1.36: Mutable Pod Resources for Suspended Jobs (beta) permite a los controladores de recursos de la red ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido, lo que facilita la asignación de recursos óptimos y reduce la carga del cluster.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | La capacidad de modificar las solicitudes y límites de contenedores en el template de Job para suspenderla. · La asignación de recursos óptimos depende de la capacidad del cluster actual, prioridades de la cola y la disponibilidad de hardware especializado como GPUs. |
| Junior | Media | La capacidad de ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido. · La capacidad de reducir la carga del cluster y mejorar la asignación de recursos. |
| Semi-Senior | Alta | La capacidad de modificar las solicitudes y límites de contenedores en el template de Job para suspenderla. · La capacidad de ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido. · La capacidad de reducir la carga del cluster y mejorar la asignación de recursos. |
| Senior | Alta | La capacidad de modificar las solicitudes y límites de contenedores en el template de Job para suspenderla. · La capacidad de ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido. · La capacidad de reducir la carga del cluster y mejorar la asignación de recursos. |
| Ingeniero de Software | Alta | La capacidad de modificar las solicitudes y límites de contenedores en el template de Job para suspenderla. · La capacidad de ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido. · La capacidad de reducir la carga del cluster y mejorar la asignación de recursos. |
| Ingeniero en Redes | Alta | La capacidad de modificar las solicitudes y límites de contenedores en el template de Job para suspenderla. · La capacidad de ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido. · La capacidad de reducir la carga del cluster y mejorar la asignación de recursos. |
| DevOps / SRE | Alta | La capacidad de modificar las solicitudes y límites de contenedores en el template de Job para suspenderla. · La capacidad de ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido. · La capacidad de reducir la carga del cluster y mejorar la asignación de recursos. |
| Ciberseguridad | Alta | La capacidad de modificar las solicitudes y límites de contenedores en el template de Job para suspenderla. · La capacidad de ajustar las especificaciones de CPU, memoria, GPU y recursos adicionales en el template de Job mientras está suspendido. · La capacidad de reducir la carga del cluster y mejorar la asignación de recursos. |


## Información técnica ⚒️

- **Versión:** 1.36
- **Fecha de lanzamiento:** 2023-04-23T150405.678
- **Cambios incompatibles:** Cambios incompatibles con los requisitos de recursos

## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Alternativas 🔄

- **Kubernetes v1.35: Flexible Pod Resources for Suspended Jobs (beta)** — confianza: medium
- **Kubernetes v1.34: Flexible Pod Resources for Suspended Jobs (beta)** — confianza: medium
- **Kubernetes v1.33: Flexible Pod Resources for Suspended Jobs (beta)** — confianza: medium
- **Kubernetes v1.32: Flexible Pod Resources for Suspended Jobs (beta)** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/](https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Kubernetes v1.36 promotes the ability to modify container resource requests and limits in the pod template of a suspended Job to beta. First introduced as alpha in v1.35, this feature allows queue controllers and cluster administrators to adjust CPU, memory, GPU, and extended resource specifications on a Job while it is suspended, before it starts or resumes running. Why mutable pod resources for suspended Jobs? Batch and machine learning workloads often have resource requirements that are not precisely known at Job creation time. The optimal resource allocation depends on current cluster capacity, queue priorities, and the availability of specialized hardware like GPUs. Before this feature, resource requirements in a Job's pod template were immutable once set. If a queue controller like Kueue determined that a suspended Job should run with different resources, the only option was to delete and recreate the Job, losing any associated metadata, status, or history. This feature also provides a way to let a specific Job instance for a CronJob progress slowly with reduced resources, rather than outright failing to run if the cluster is heavily loaded. Consider a machine learning training Job initially requesting 4 GPUs: apiVersion : batch/v1 kind : Job metadata : name : training-job-example-abcd123 labels : app.kubernetes.io/name : trainer spec : suspend : true template : metadata : annotations : kubernetes.io/description : "ML training, ID abcd123" spec : containers : - name : trainer image : example-registry.example.com/training:2026-04-23T150405.678 resources : requests : cpu : "8" memory : "32Gi" example-hardware-vendor.com/gpu : "4" limits : cpu : "8" memory : "32Gi" example-hardware-vendor.com/gpu : "4" restartPolicy : Never A queue controller managing cluster resources might determine that only 2 GPUs are available. With this feature, the controller can update the Job's resource requests before resuming it: apiVersion : batch/v1 kind : Job metadata : name : training-job-example-abcd123 labels : app.kubernetes.io/name : trainer spec : suspend : true template : metadata : annotations : kubernetes.io/description : "ML training, ID abcd123" spec : containers : - name : trainer image : example-registry.example.com/training:2026-04-23T150405.678 resources : requests : cpu : "4" memory : "16Gi" example-hardware-vendor.com/gpu : "2" limits : cpu : "4" memory : "16Gi" example-hardware-vendor.com/gpu : "2" restartPolicy : Never Once the resources are updated, the controller resumes the Job by setting spec.suspend to false , and the new Pods are created with the adjusted resource specifications. How it works The Kubernetes API server relaxes the immutability constraint on pod template resource fields specifically for suspended Jobs. No new API types have been introduced; the existing Job and pod template structures accommodate the change through relaxed validation. The mutable fields are: spec.template.spec.containers[*].resources.requests spec.template.spec.containers[*].resources.limits spec.template.spec.initContainers[*].resources.requests spec.template.spec.initContainers[*].resources.limits Resource updates are permitted when the following conditions are met: The Job has spec.suspend set to true . For a Job that was previously running and then suspended, all active Pods must have terminated ( status.active equals 0) before resource mutations are accepted. Standard resource validation still applies. For example, resource limits must be greater than or equal to requests, and extended resources must be specified as whole numbers where required. What's new in beta With the promotion to beta in Kubernetes v1.36, the MutablePodResourcesForSuspendedJobs feature gate is enabled by default. This means clusters running v1.36 can use this feature without any additional configuration on the API server. Try it out If your cluster is running Kubernetes v1.36 or later, this feature is available by default. For v1.35 clusters, enable the MutablePodResourcesForSuspendedJobs feature gate on the kube-apiserver . You can test it by creating a suspended Job, updating its container resources using kubectl edit or a controller, and then resuming the Job: # Create a suspended Job kubectl apply -f my-job.yaml --server-side # Edit the resource requests kubectl edit job training-job-example-abcd123 # Resume the Job kubectl patch job training-job-example-abcd123 -p '{"spec":{"suspend":false}}' Considerations Running Jobs that are suspended If you suspend a Job that was already running, you must wait for all of that Job's active Pods to terminate before modifying resources. The API server rejects resource mutations while status.active is greater than zero. This prevents inconsistency between running Pods and the updated pod template. Pod replacement policy When using this feature with Jobs that may have failed Pods, consider setting podReplacementPolicy: Failed . This ensures that replacement Pods are only created after the previous Pods have fully terminated, preventing resource contention from overlapping Pods. ResourceClaims Dynamic Resource Allocation (DRA) resourceClaimTemplates remain immutable. If your workload uses DRA, you must recreate the claim templates separately to match any resource changes. Getting involved This feature was developed by SIG Apps This feature was developed by SIG Apps with input from WG Batch . Both groups welcome feedback as the feature progresses toward stable. You can reach out through: Slack channel #sig-apps . Slack channel #wg-batch . The KEP-5440 tracking issue.

</details>

