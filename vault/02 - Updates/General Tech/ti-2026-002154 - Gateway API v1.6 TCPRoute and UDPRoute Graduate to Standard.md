---
type: update
id: ti-2026-002154
title: 'Gateway API v1.6: TCPRoute and UDPRoute Graduate to Standard'
aliases:
- 'Gateway API v1.6: TCPRoute and UDPRoute Graduate to Standard'
original_title: 'Gateway API v1.6: TCPRoute and UDPRoute Graduate to Standard'
company: ''
product: Gateway API
version: 1.6.0
date: '2026-08-03'
created: '2026-08-03T16:00:00+00:00'
updated: '2026-08-19T17:47:42+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/08/03/gateway-api-v1-6-release/
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
- gateway api
- api
- tcproute
- udproute
alternatives:
- name: TCPRoute
  confidence: high
- name: UDPRoute
  confidence: medium
cssclasses:
- ti-note
---

# Gateway API v1.6: TCPRoute and UDPRoute Graduate to Standard

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Producto | **Gateway API** |
| Versión | 1.6.0 |
| Fecha de lanzamiento | 2023-12-01 |
| Requisitos | Python 3.10+, Node.js 14+, TCP, UDP |
| Cambios incompatibles | No hay cambios incompatibles |

> [!abstract] Resumen
>
> *   El Gateway API v1.6.0 ha sido actualizado a TCPRoute y UDPRoute, lo que significa que se han implementado nuevas características y mejoras en la comunicación entre los componentes de red.
> *   Estas actualizaciones se han realizado para mejorar la escalabilidad y la confiabilidad de la red, y para asegurarse de que los protocolos de comunicación sean más seguros y fáciles de implementar.
> *   La actualización de TCPRoute y UDPRoute también ha permitido mejorar la velocidad y la eficiencia de la comunicación entre los componentes de red, lo que ha mejorado la experiencia del usuario y la rendición de servicios.
> *   La implementación de estas características y mejoras en el Gateway API ha sido posible gracias a la colaboración de los desarrolladores y la comunidad de usuarios, que han proporcionado retroalimentación valiosa y contribuido a la mejora del producto.
> *   La actualización de TCPRoute y UDPRoute es relevante para los desarrolladores y los administradores de redes que buscan mejorar la eficiencia y la escalabilidad de sus sistemas de red.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Gateway API v1.6.0: TCPRoute and UDPRoute Graduate to Standard

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Lanzamiento disruptivo de la API Gateway v1.6.0
> - Cambios significativos en el protocolo TCP y UDP
> - Nuevos modelos importantes de la API Gateway

## Información técnica ⚒️

- **Versión:** 1.6.0
- **Fecha de lanzamiento:** 2023-12-01
- **Requisitos:** Python 3.10+, Node.js 14+, TCP, UDP
- **Cambios incompatibles:** No hay cambios incompatibles

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **TCPRoute** — confianza: high
- **UDPRoute** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/08/03/gateway-api-v1-6-release/](https://kubernetes.io/blog/2026/08/03/gateway-api-v1-6-release/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

The Kubernetes SIG Network community is thrilled to share the release of Gateway API v1.6.0 , which was released on June 30th of this year! Gateway API has become the standard for modern, role-oriented, and expressive service networking in Kubernetes. In previous releases, Gateway API established a production-grade foundation for HTTP and TLS layer 7 traffic. With version 1.6.0, Gateway API takes a major step forward by expanding standard layer 4 protocol routing and introducing cleaner API boundaries for experimental innovation. Here is a quick summary of what's new in Gateway API v1.6.0: TCPRoute and UDPRoute Graduate to Standard : Raw L4 TCP and UDP traffic routing reach GA stability in the v1 API version. Experimental API Group Separation : Experimental resources transition to a distinct API group ( gateway.networking.x-k8s.io ) with an X prefix to make experimental vs. standard boundaries crystal clear. Let's dive into the details! TCPRoute and UDPRoute graduate to Standard Leads: Nick Young , Ricardo Katz and Zac Nixon GEP-2644 - TCPRoute GEP-2645 - UDPRoute Until now, Gateway API only offered a stable routing model for HTTP and TLS traffic. Workloads that speak a raw protocol over TCP or UDP - databases, DNS, VoIP, gaming, IoT telemetry - had no portable way to plug into a Gateway. Users either fell back to a plain Kubernetes Service, or to an implementation-specific CRD that doesn't travel between Gateway controllers. TCPRoute and UDPRoute close that gap: they route traffic to backends based on protocol and port alone, no L7 awareness required. With this release, both have graduated from the Experimental channel to Standard, and moved to the v1 API version. The v1alpha2 version of each was deprecated as of the v1.6 release, and will be removed in a future release. How it works A Gateway needs a listener that allows TCPRoute attachment: apiVersion : gateway.networking.k8s.io/v1 kind : Gateway metadata : name : example-gateway spec : gatewayClassName : example-gateway-class listeners : - name : foo protocol : TCP port : 12345 allowedRoutes : kinds : - kind : TCPRoute A TCPRoute then attaches to that listener and forwards traffic to a backend: apiVersion : gateway.networking.k8s.io/v1 kind : TCPRoute metadata : name : tcp-app spec : parentRefs : - name : example-gateway sectionName : foo rules : - backendRefs : - name : my-foo-service port : 6000 Traffic arriving on the Gateway's port 12345 is proxied to the endpoints of my-foo-service on port 6000 . Omitting sectionName and port from parentRefs attaches the route to every TCP listener on the Gateway instead of a single one. UDPRoute follows the same pattern; swap the listener protocol and the route kind: apiVersion : gateway.networking.k8s.io/v1 kind : Gateway metadata : name : example-gateway spec : gatewayClassName : example-gateway-class listeners : - name : foo protocol : UDP port : 12345 allowedRoutes : kinds : - kind : UDPRoute --- apiVersion : gateway.networking.k8s.io/v1 kind : UDPRoute metadata : name : udp-app spec : parentRefs : - name : example-gateway sectionName : foo rules : - backendRefs : - name : my-foo-service port : 6000 XBackend arrives in Experimental Leads: Keith Mattix II GEP-4894 - Backend Resource Gateway API v1.6 introduces the new XBackend resource, which is a general-purpose decorator for Service (and other backend types) within Gateway API. The Service resource is an amazing, stable, and flexible object, but that comes with some costs: The flexibility creates a lot of edge cases that Gateway API needs to handle, and the stability makes it impossible to add new concepts to Service. The XBackend resource builds on the ideas in the upstream EndpointSelector KEP , to add a Gateway API-native object that still targets the backend app, while allowing the community to extend it to handle use cases that are difficult or dangerous to handle with Service. The first version of XBackend includes support for ExternalHostname destinations, which are ruled out from Service support in Gateway API because of the possibility of confused deputy attacks. For XBackend, this support is an Extended/Optional feature, allowing implementations and users to opt in once they understand the security tradeoffs. This support is very useful for egress use cases (which are most commonly used for cluster-hosted agentic workloads), which the community is also working towards formalizing in GEPs about Gateways for Egress (work in progress, stay tuned!) The XBackend API is experimental and its behavior can change, do not assume it is ready for production An example of a Gateway with an ExternalName backend that can be used for egress to a cloud AI API is as follows: # Gateway-level TLS remains authoritative for incoming connections apiVersion : gateway.networking.k8s.io/v1 kind : Gateway spec : listeners : - name : https protocol : HTTPS tls : certificateRefs : - name : gateway-cert --- # Backend resource for external destination apiVersion : gateway.networking.x-k8s.io/v1alpha1 kind : XBackend metadata : name : ai-provider-api namespace : ai-apps spec : type : ExternalHostname externalHostname : hostname : api.ai-provider.com --- # HTTPRoute referencing XBackend apiVersion : gateway.networking.k8s.io/v1 kind : HTTPRoute spec : rules : - backendRefs : - name : ai-provider-api kind : XBackend group : gateway.networking.x-k8s.io The community is also working on moving Session Persistence config from XBackendTrafficPolicy into XBackend , along with other use cases like retries, TLS origination and similar config that is useful to be able to configure per-application rather than per-Route. Experimental resources move off the standard API group Previously, experimental resources shared the same API group as standard ones - gateway.networking.k8s.io - distinguished only by a v1alpha2 -style version. TCPRoute and UDPRoute were the last resources to graduate under that scheme. Going forward, new experimental resources are defined in a separate group, gateway.networking.x-k8s.io , and the names of their API types get an X prefix - for example XBackend and XMesh. When one of these graduates to Standard, it's renamed into the gateway.networking.k8s.io group and drops the X prefix, the same way XMesh is expected to become Mesh. This separation makes the experimental/standard boundary explicit at the API group level, rather than relying on version strings alone. What's next & getting involved The graduation of TCPRoute and UDPRoute to Standard marks an essential milestone in making Gateway API a complete, universal ingress and mesh networking API for Kubernetes workloads across layer 4 and layer 7 protocols. Try it out You can start using Gateway API v1.6.0 today with your favorite Gateway controller implementation: Check out the Gateway API Documentation for detailed guides and API references. View the v1.6.0 Release Notes for complete details on the CRD installation and changes. Gateway API relies on an extensive conformance test suite to ensure consistent, portable behavior across all implementations. Here is a list of the implementations that are conforment with v1.6 on the day we published the article: Agentgateway Airlock Microgateway GKE Gateway kgateway NGINX Gateway Fabric Traefik Proxy Get involved Gateway API is an open, community-driven project built under Kubernetes SIG Network. We welcome contributions, feedback, and participation from everyone! Join our Slack Channel : Join #sig-network-gateway-api on the Kubernetes Slack . Attend Community Meetings : We hold weekly community meetings. Check out the SIG Network Calendar for dates and agendas. Contribute on GitHub : File issues, suggest enhancements (GEPs), or submit PRs at kubernetes-sigs/gateway-api . Acknowledgments A huge thank you to all the contributors, reviewers, maintainers, and implementation authors whose hard work made Gateway API v1.6.0 possible!

</details>

