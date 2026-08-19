---
type: update
id: ti-2026-002170
title: 'Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager'
aliases:
- 'Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager'
original_title: 'Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller
  Manager'
company: ''
product: ''
version: ''
date: '2026-05-15'
created: '2026-05-15T18:35:00+00:00'
updated: '2026-08-19T17:41:07+00:00'
original_language: en
translated: true
importance: medium
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/
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
- name: route_controller_route_sync_total
  confidence: high
- name: route_controller_route_sync_total
  confidence: medium
cssclasses:
- ti-note
---

# Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟡 Media` · `🚀 Alto`

> [!abstract] Resumen
>
> *   **Kubernetes v1.36**: Introducción de una nueva métrica para la sincronización de rutas en el Manager de Controladores de la Nube (CCM) de Route Controller en k8s.io/cloud-provider.
> *   **Nueva métrica**: route_controller_route_sync_total, que sube cada vez que las rutas se sincronizan con el proveedor de infraestructura.
> *   **Reconciliación de rechazos basada en watch**: Introducción de esta métrica para ayudar a los operadores a validar la característica de CloudControllerManagerWatchBasedRoutesReconciliation.
> *   **Característica gate**: El manager de controles de la nube de la route controller se ha convertido en un enfoque de rechazo basado en watch que solo se reconcilia cuando los nodos cambian.
> *   **Beneficios**: Reducción de la presión en las APIs rate-limítadas, permitiendo a los operadores utilizar más eficientemente sus reservas.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Kubernetes v1.36: Nueva métrica para la sincronización de rutas en el Manager de Controladores de la Nube
> 
> Este artículo originalmente fue publicado con un fecha incorrecta. Fue posteriormente republishado, datado el 15 de mayo de 2026. Kubernetes v1.36 introduce una nueva counter métrica route_controller_route_sync_total al implementación del manager de controles de la nube (CCM) de route controller en k8s.io/cloud-provider. Esta métrica sube cada vez que las rutas se sincronizan con el proveedor de infraestructura. Reconciliación de rechazos basada en watch. Esta métrica fue agregada para ayudar a los operadores a validar la característica de CloudControllerManagerWatchBasedRoutesReconciliation introducida en Kubernetes v1.35. Esta característica gate switcha el manager de controles de la nube de la route controller de intervalo fijo a un enfoque de rechazo basado en watch que solo se reconcilia cuando los nodos cambian. Esto reduce los llamados a API a la infraestructura, reduciendo la presión en las APIs rate-limítadas y permite a los operadores utilizar más eficientemente sus reservas. Para probar esta métrica, compara route_controller_route_sync_total con la característica gate desactivada (default) versus activada. En clusters donde los cambios de nodos son infrecuentes, se espera que se vea una disminución significativa en la tasa de sincronización con la característica gate activada. Ejemplo: comportamiento esperado Con la característica gate desactivada (el default intervalo fijo), el contador sube steadymente independientemente de si hay cambios de nodos ocurridos: # Después de 10 minutos sin cambios de nodos route_controller_route_sync_total 60 # Después de 20 minutos, sin cambios de nodos route_controller_route_sync_total 120 Con la característica gate activada (reconciliación basada en watch), el contador solo sube cuando los nodos son agregados, eliminados o actualizados: # Después de 10 minutos sin cambios de nodos route_controller_route_sync_total 1 # Después de 20 minutos, sin cambios de nodos — contador unchanged route_controller_route_sync_total 1 # Un nuevo nodo entra en el cluster — contador sube route_controller_route_sync_total 2 La diferencia es especialmente visible en clusters estables donde los nodos rara vez cambian. ¿Dónde puedo dar mi opinión? Si tienes una opinión, sienta bien en las siguientes canales: El canal #sig-cloud-provider en Kubernetes Slack El problema KEP-5237 en GitHub El sitio web de la comunidad SIG Cloud Provider para otras canales ¿Cómo puedo aprender más? Para más detalles, consulte KEP-5237.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Nueva métrica para la sincronización de rutas en el Manager de Controladores de la Nube
> - Introducción de una nueva counter métrica route_controller_route_sync_total
> - Reconciliación de rechazos basada en watch para mejorar la eficiencia de los operadores

## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Alternativas 🔄

- **route_controller_route_sync_total** — confianza: high
- **route_controller_route_sync_total** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/](https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

This article was originally published with the wrong date. It was later republished, dated the 15th of May 2026. Kubernetes v1.36 introduces a new alpha counter metric route_controller_route_sync_total to the Cloud Controller Manager (CCM) route controller implementation at k8s.io/cloud-provider . This metric increments each time routes are synced with the cloud provider. A/B testing watch-based route reconciliation This metric was added to help operators validate the CloudControllerManagerWatchBasedRoutesReconciliation feature gate introduced in Kubernetes v1.35 . That feature gate switches the route controller from a fixed-interval loop to a watch-based approach that only reconciles when nodes actually change. This reduces unnecessary API calls to the infrastructure provider, lowering pressure on rate-limited APIs and allowing operators to make more efficient use of their available quota. To A/B test this, compare route_controller_route_sync_total with the feature gate disabled (default) versus enabled. In clusters where node changes are infrequent, you should see a significant drop in the sync rate with the feature gate turned on. Example: expected behavior With the feature gate disabled (the default fixed-interval loop), the counter increments steadily regardless of whether any node changes occurred: # After 10 minutes with no node changes route_controller_route_sync_total 60 # After 20 minutes, still no node changes route_controller_route_sync_total 120 With the feature gate enabled (watch-based reconciliation), the counter only increments when nodes are actually added, removed, or updated: # After 10 minutes with no node changes route_controller_route_sync_total 1 # After 20 minutes, still no node changes — counter unchanged route_controller_route_sync_total 1 # A new node joins the cluster — counter increments route_controller_route_sync_total 2 The difference is especially visible in stable clusters where nodes rarely change. Where can I give feedback? If you have feedback, feel free to reach out through any of the following channels: The #sig-cloud-provider channel on Kubernetes Slack The KEP-5237 issue on GitHub The SIG Cloud Provider community page for other communication channels How can I learn more? For more details, refer to KEP-5237 .

</details>

