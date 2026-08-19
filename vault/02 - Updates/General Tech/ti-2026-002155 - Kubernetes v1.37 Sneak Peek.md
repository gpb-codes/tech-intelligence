---
type: update
id: ti-2026-002155
title: Kubernetes v1.37 Sneak Peek
aliases:
- Kubernetes v1.37 Sneak Peek
original_title: Kubernetes v1.37 Sneak Peek
company: ''
product: ''
version: '1.37'
date: '2026-07-31'
created: '2026-07-31T16:00:00+00:00'
updated: '2026-08-19T18:05:44+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/07/31/kubernetes-v1-37-sneak-peek/
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
- name: Fluentd
  confidence: high
- name: Fluentd
  confidence: medium
cssclasses:
- ti-note
---

# Kubernetes v1.37 Sneak Peek

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | 1.37 |
| Fecha de lanzamiento | Sneak Peek |

> [!abstract] Resumen
>
> - **Mantenga el significado exacto**: Mantenga la información original sin alterarla.
> - **No invente información**: No agregue datos que no estén presentes en el contenido original.
> - **No agregues información**: No incluya datos adicionales que no se mencionen en el contenido.
> - **Mantenga nombres propios**: Utilice nombres propios para las empresas, productos y tecnologías.
> - **Mantenga nombres de productos**: Utilice nombres propios para los productos, manteniendo la versión y la fecha de lanzamiento.
> - **No invente nombres de empresas**: Utilice nombres propios para las empresas, manteniendo la información de contacto y la información de propiedad intelectual.
> - **No agregues información externa**: No incluya información externa como URLs, comandos o términos técnicos no propios.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Kubernetes v1.37 Sneak Peek
> 
> - Mantenga el significado exacto.
> - No invente información.
> - No agregues información.
> - Mantenga nombres propios.
> - Mantenga nombres de productos.
> - Mantenga nombres de empresas.
> - Mantenga versiones.
> - Mantenga fechas.
> - Mantenga precios.
> - Mantenga URLs.
> - Mantenga comandos.
> - Mantenga términos técnicos cuando sea mejor mantenerlos en inglés.
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
> Kubernetes es un sistema de gestión de contenedores y aplicaciones descentralizadas que permite la automoción y la escalabilidad de aplicaciones en la nube.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Kubernetes ayuda a los desarrolladores a crear aplicaciones escalables, fáciles de mantener y escalables, y a reducir el tiempo de respuesta a los problemas en la nube.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | Automatización de la escalabilidad de aplicaciones · Gestión de contenedores y aplicaciones descentralizadas · Reducción del tiempo de respuesta a los problemas en la nube |
| Junior | Baja | Gestión de aplicaciones descentralizadas · Automatización de la escalabilidad de aplicaciones · Reducción del tiempo de respuesta a los problemas en la nube |
| Semi-Senior | Baja | Gestión de aplicaciones descentralizadas · Automatización de la escalabilidad de aplicaciones · Reducción del tiempo de respuesta a los problemas en la nube |
| Senior | Baja | Gestión de aplicaciones descentralizadas · Automatización de la escalabilidad de aplicaciones · Reducción del tiempo de respuesta a los problemas en la nube |
| Ingeniero de Software | Alta | Desarrollo de aplicaciones escalables y fáciles de mantener · Automatización de la gestión de aplicaciones · Reducción del tiempo de respuesta a los problemas en la nube |
| Ingeniero en Redes | Alta | Desarrollo de redes escalables y fáciles de mantener · Automatización de la gestión de redes · Reducción del tiempo de respuesta a los problemas en la nube |
| DevOps / SRE | Alta | Desarrollo de aplicaciones escalables y fáciles de mantener · Automatización de la gestión de aplicaciones · Reducción del tiempo de respuesta a los problemas en la nube |
| Ciberseguridad | Baja | Desarrollo de aplicaciones seguras y fáciles de mantener · Automatización de la gestión de aplicaciones · Reducción del tiempo de respuesta a los problemas en la nube |


## Información técnica ⚒️

- **Versión:** 1.37
- **Fecha de lanzamiento:** Sneak Peek

## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Alternativas 🔄

- **Fluentd** — confianza: high
- **Fluentd** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/07/31/kubernetes-v1-37-sneak-peek/](https://kubernetes.io/blog/2026/07/31/kubernetes-v1-37-sneak-peek/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

As we get closer to the release date for Kubernetes v1.37, the project develops and matures, features may be deprecated, removed, or replaced with better ones for the project's overall health. This blog outlines some of the planned changes for the Kubernetes v1.37 release that the release team feels you should be aware of for the continued maintenance of your Kubernetes environment and keeping up to date with the latest changes. The information below reflects the current status of the v1.37 release and may change before the actual release date. Deprecations and removals for Kubernetes v1.37 Kubectl: kubectl run --filename/-f to be deprecated The --filename (or -f ) flag for kubectl run is being deprecated as the generated pod is always built purely from CLI arguments like NAME and --image . See kubernetes/kubernetes#138671 for the original issue and discussion. Kubelet: Static Pods can no longer reference Secrets or ConfigMaps Static Pods were never meant to read API resources directly, since they aren't created through the API server — but a bug let them reference Secrets or ConfigMaps via fields like configMapRef or secretRef . That bug is now fixed: as of v1.37 these references are strictly prohibited, and the PreventStaticPodAPIReferences feature gate that previously let you opt out of the restriction has been removed. See kubernetes/kubernetes#140226 for the original issue and discussion. Deprecating kube-proxy's support for ipvs mode kube-proxy support for ipvs mode was introduced in v1.8 to resolve iptables performance bottlenecks. However, since the kernel ipvs API alone cannot fully implement Kubernetes Services, ipvs mode continues to use iptables underneath ( KEP-3866, "The ipvs mode of kube-proxy will not save us" ). Clusters running kube-proxy in ipvs mode (or mode: ipvs in KubeProxyConfiguration) would now be logging a deprecation warning on startup. The deprecation timeline looks like this: By v1.40, ipvs mode for kube-proxy is expected to be disabled by default (still selectable via the feature gate) By v1.43, support for ipvs mode would be removed entirely KEP-5495, Graduation Criteria . To confirm which mode you’re currently running, use: kubectl -n kube-system get configmap kube-proxy -o jsonpath = '{.data.config\.conf}' | grep 'mode:' To understand the rationale behind this deprecation, see KEP-5495: Deprecate ipvs mode in kube-proxy . Ongoing major changes Future removal of cgroup v1 support As modern Linux distributions and container runtimes use cgroup v2 as the default, support for the legacy cgroup v1 is officially being phased out. Since the v1.35 release, the failCgroupV1 setting has defaulted to true. Consequently, the kubelet will fail to initialize on any nodes that still rely on cgroup v1 unless an explicit configuration override is applied. apiVersion : kubelet.config.k8s.io/v1beta1 kind : KubeletConfiguration failCgroupV1 : false # temporary override Using this override should be considered a short-term fix. Advanced resource management capabilities, such as In-Place Pod Resizing and Tiered Memory Protection, depend entirely on cgroup v2. While the override remains available in Kubernetes v1.37, users are encouraged to migrate to cgroup v2, as support for cgroup v1 is planned to be removed in a future release. To learn more about this deprecation, refer to KEP-5573: Remove cgroup v1 support . Breaking changes in Kubernetes v1.37 SELinux volume relabeling ("SELinuxMount") graduates to GA SELinuxMount is expected to reach GA and be enabled by default in v1.37. Volumes would then be mounted with -o context=<label> (the mount option default) instead of being recursively relabeled, but only when the volume's CSI driver opts in via a CSIDriver that sets .spec seLinuxMount: true . Because a single mount can only hold one SELinux context, pods with different SELinux labels sharing a volume on the same node (which previously coexisted under recursive relabeling) may now fail to start. To retain the previous recursive behavior for a specific workload, set seLinuxChangePolicy: Recursive in the Pod spec. Clusters without SELinux enabled see no effect at all. To learn more, check SELinux Volume Label Changes goes GA (and likely implications in v1.37) Featured enhancements of Kubernetes v1.37 Metrics API goes GA The metrics.k8s.io API is expected to graduate to Stable (GA) in Kubernetes v1.37 after spending nearly nine years in Beta. The API provides a standard way to retrieve CPU and memory usage for pods and nodes, powering widely used Kubernetes features such as the Horizontal Pod Autoscaler (HPA) and commands like kubectl top . This graduation recognizes the API's stability and widespread adoption, with no functional changes expected. Both v1 and v1beta1 will remain usable during the transition, enabling developers to adopt the stable API at their own pace without breaking existing workflows. To learn more about this enhancement, refer to KEP-5207: metrics.k8s.io API definition . Kubelet in UserNS a.k.a. Rootless Mode Traditionally, Kubernetes node components such as the kubelet run with root privileges on the host. While necessary for many deployments, this also means that a vulnerability in one of these components could potentially have a greater impact on the underlying system. With Kubernetes v1.37, kubelet in User Namespace (Rootless Mode) is expected to graduate to Beta. This enhancement allows Kubernetes node components to run inside a Linux user namespace as an unprivileged user on the host while still behaving as root within the namespace. By reducing the need for host-level root privileges, it adds an extra layer of isolation and helps limit the impact of potential vulnerabilities affecting node components. To learn more about this enhancement, refer to KEP-2033: Kubelet in UserNS(aka Rootless Mode) . Volume health monitor Historically, Kubernetes has lacked an API for CSI drivers to report storage failures, which become evident only through failed mounts or hung I/O. Since remediation controllers had nothing machine-readable to act upon, the only way to figure out the root cause behind this failure was to cross-reference Kubernetes objects alongside external vendor dashboards. In Kubernetes v1.37, this KEP resets graduation to Alpha after an initial implementation in v1.21 and introduces four new CSI RPCs. The controller plugin reports the health of storage volumes using ControllerListVolumeHealth (lists unhealthy volumes) and ControllerGetVolumeHealth (checks a specific volume). A controller-side health monitor polls these CSI controllers and stores the results in PersistentVolumeClaim.status.healthStatus . On the node side, the kubelet calls NodeGetVolumeHealth to obtain the health of individual volumes on that node and records it in Pod.status.volumeHealth , while NodeGetStorageHealth reports the health of the drivers registered to a node in CSINode.status.storageHealth . The error vocabulary is kept simple, extensible, and machine-parsable ( Inaccessible , Degraded , etc.), with further driver-specific elaboration available via reason and message . Finally, the controller-side and node-side reports are kept independent and are hence displayed separately, providing a more holistic view of storage health to consumers. To learn more about this enhancement, refer to KEP-1432: Volume Health Monitor . Want to know more? New features and deprecations are also announced in the Kubernetes release notes. We will formally announce what's new in Kubernetes v1.37 as part of the CHANGELOG for that release. Kubernetes v1.37 release is planned for Wednesday, August 26th, 2026 . Stay tuned for updates! You can see the announcements of changes in the release notes for: Kubernetes v1.36 Kubernetes v1.35 Kubernetes v1.34 Kubernetes v1.33 Get involved The simplest way to get involved with Kubernetes is by joining one of the many Special Interest Groups (SIGs) that align with your interests. If you don't know where to start, join our monthly New Contributor Orientations where we teach the community how the project is structured, and we'll guide you on how to make your first contribution to the project. Read more on how to become a Kubernetes Contributor Read more about what’s happening with Kubernetes on our blog Join us on Slack Follow us on X Follow us on LinkedIn Follow us on Bluesky for the latest updates Join the community discussion on Discuss Post questions (or answer questions) on Stack Overflow Share your Kubernetes End User Story Learn more about the Kubernetes Release Team

</details>

