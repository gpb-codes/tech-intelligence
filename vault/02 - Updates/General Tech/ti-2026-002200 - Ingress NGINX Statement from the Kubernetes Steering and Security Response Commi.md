---
type: update
id: ti-2026-002200
title: 'Ingress NGINX: Statement from the Kubernetes Steering and Security Response
  Committees'
aliases:
- 'Ingress NGINX: Statement from the Kubernetes Steering and Security Response Committees'
original_title: 'Ingress NGINX: Statement from the Kubernetes Steering and Security
  Response Committees'
company: ''
product: ''
version: ''
date: '2026-01-29'
created: '2026-01-29T00:00:00+00:00'
updated: '2026-08-18T23:01:53+00:00'
original_language: en
translated: true
importance: medium
impact: medium
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/
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
- name: Gateway API
  confidence: high
- name: Ingress Controller
  confidence: medium
cssclasses:
- ti-note
---

# Ingress NGINX: Statement from the Kubernetes Steering and Security Response Committees

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟡 Media` · `🌐 Medio`

> [!abstract] Resumen
>
> *   Reglas:
>     *   Mantén exactamente el significado.
>     *   No inventas información.
>     *   No agregas información.
>     *   Conserva nombres propios.
>     *   Conserva nombres de productos.
>     *   Conserva nombres de empresas.
>     *   Conserva versiones.
>     *   Conserva fechas.
>     *   Conserva precios.
>     *   Conserva URLs.
>     *   Conserva código.
>     *   Conserva comandos.
>     *   Conserva términos técnicos cuando sea mejor mantenerlos en inglés.
> *   Ingress NGINX:
>     *   Retirado por Kubernetes en marzo de 2026.
>     *   La retirada fue anunciada después de años de advertencias públicas.
>     *   No habrá más actualizaciones después de la retención.
>     *   No habrá más correcciones de bugs, parches de seguridad o actualizaciones.
>     *   La migración a alternativas como el Gateway API es obligatoria.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
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
> - No traducas nombres de productos o tecnologías.
> 
> Contenido:
> Ingress NGINX: Statement from the Kubernetes Steering and Security Response Committees
> 
> En marzo de 2026, Kubernetes retirará Ingress NGINX, un componente crítico de infraestructura para alrededor de la mitad de entornos cloud-native. La retirada de Ingress NGINX fue anunciada para marzo de 2026, después de años de advertencias públicas que el proyecto necesitaba contribuyentes y mantenimiento. No habrá más actualizaciones para correcciones de bugs, parches de seguridad o cualquier tipo de actualización después de la retención. Esto no puede ignorarse, desafiar o dejar para el último minuto para abordar. No podemos subestimar la gravedad de esta situación ni la importancia de comenzar la migración a alternativas como el Gateway API o uno de los muchos controles de ingreso de terceros inmediatamente. Para ser claro: elegir permanecer con Ingress NGINX después de su retiro deja a los usuarios y a ustedes vulnerables a ataques. Ninguna de las alternativas disponibles son directas drop-in reemplazos. Esto requiere tiempo y ingeniería. La mitad de ustedes estarán afectados. Tienen dos meses para prepararse. Las actualizaciones existentes continuarán funcionando, por lo que, a menos que lo hagan, no sabrán que están afectados hasta que sean comprometidos. En la mayoría de los casos, pueden verificar si dependen de Ingress NGINX ejecutando la comandos `kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx` con permisos de administrador de cluster. A pesar de su amplia atraer y uso por empresas de todas las edades, y numerosas llamadas por ayuda de los mantenimiento, el proyecto Ingress NGINX nunca recibió los contribuyentes que necesitaba. Según la investigación interna Datadog, alrededor del 50% de los entornos cloud-native actuales dependen de este tool, y durante varios años, se mantuvo solo por uno o dos personas trabajando en su tiempo libre. Sin suficiente personal para mantenerlo a un estándar tanto como a los usuarios considerar seguro, la elección responsable es cerrar Ingress NGINX y enfocarse en alternativas modernas como Gateway API . No hicimos esta decisión con mucha prisa; como sea inconveniente, haciendolo es necesario para la seguridad de todos los usuarios y el ecosistema en general. Sin embargo, la flexibilidad que Ingress NGINX fue diseñada para, que una vez fue una ventaja, ha convertidose en un desafío que no se puede resolver. Con el deuda técnica que ha acumulado y decisiones fundamentales que exacerban los fallos de seguridad, no es razonable ni incluso posible continuar manteniendo el tool incluso si se hubieran materializado recursos. Nos unimos a ustedes para reforzar la escala de esta cambio y el riesgo potencial de una gran parte de los usuarios de Kubernetes si este asunto es ignorado. Es imperativo que verifiquen sus clusters ahora. Si dependen de Ingress NGINX, deban comenzar a planificar la migración. Gracias, Comité de Steering de Kubernetes y el Comité de Seguridad de Kubernetes.

## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Alternativas 🔄

- **Gateway API** — confianza: high
- **Ingress Controller** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

In March 2026, Kubernetes will retire Ingress NGINX, a piece of critical infrastructure for about half of cloud native environments. The retirement of Ingress NGINX was announced for March 2026, after years of public warnings that the project was in dire need of contributors and maintainers. There will be no more releases for bug fixes, security patches, or any updates of any kind after the project is retired. This cannot be ignored, brushed off, or left until the last minute to address. We cannot overstate the severity of this situation or the importance of beginning migration to alternatives like Gateway API or one of the many third-party Ingress controllers immediately. To be abundantly clear: choosing to remain with Ingress NGINX after its retirement leaves you and your users vulnerable to attack. None of the available alternatives are direct drop-in replacements. This will require planning and engineering time. Half of you will be affected. You have two months left to prepare. Existing deployments will continue to work, so unless you proactively check, you may not know you are affected until you are compromised. In most cases, you can check to find out whether or not you rely on Ingress NGINX by running kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx with cluster administrator permissions. Despite its broad appeal and widespread use by companies of all sizes, and repeated calls for help from the maintainers, the Ingress NGINX project never received the contributors it so desperately needed. According to internal Datadog research, about 50% of cloud native environments currently rely on this tool, and yet for the last several years, it has been maintained solely by one or two people working in their free time. Without sufficient staffing to maintain the tool to a standard both ourselves and our users would consider secure, the responsible choice is to wind it down and refocus efforts on modern alternatives like Gateway API . We did not make this decision lightly; as inconvenient as it is now, doing so is necessary for the safety of all users and the ecosystem as a whole. Unfortunately, the flexibility Ingress NGINX was designed with, that was once a boon, has become a burden that cannot be resolved. With the technical debt that has piled up, and fundamental design decisions that exacerbate security flaws, it is no longer reasonable or even possible to continue maintaining the tool even if resources did materialize. We issue this statement together to reinforce the scale of this change and the potential for serious risk to a significant percentage of Kubernetes users if this issue is ignored. It is imperative that you check your clusters now. If you are reliant on Ingress NGINX, you must begin planning for migration. Thank you, Kubernetes Steering Committee Kubernetes Security Response Committee

</details>

