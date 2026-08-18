---
type: update
id: ti-2026-002263
title: Upgrade Amazon EKS clusters with confidence using Kubernetes version rollbacks
aliases:
- Upgrade Amazon EKS clusters with confidence using Kubernetes version rollbacks
original_title: Upgrade Amazon EKS clusters with confidence using Kubernetes version
  rollbacks
company: AWS
product: Amazon EKS
version: ''
date: '2026-07-01'
created: '2026-07-01T17:20:30+00:00'
updated: '2026-08-18T21:02:03+00:00'
original_language: en
translated: true
importance: high
impact: high
pricing: paid
license: unknown
open_source: false
self_hosted: false
source: AWS News Blog
source_url: https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks/
source_type: rss
processed_by: openrouter
backend: opencodezen
model: nvidia/nemotron-3.5-lightning:free
insights: true
status: published
category: Cloud
subcategory: Managed Kubernetes
confidence: medium
example: false
tags:
- kubernetes
- eks
- rollback
- aws
- cloud
- managed
alternatives: []
cssclasses:
- ti-note
---

# Upgrade Amazon EKS clusters with confidence using Kubernetes version rollbacks

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🚀 Alto` · `💳 De pago`

| Campo | Valor |
| --- | --- |
| Empresa | **AWS** |
| Producto | **Amazon EKS** |
| Requisitos | Kubernetes versions supported by EKS Standard Support and Extended Support; compatible with both self-managed nodes and EKS Auto Mode |
| Precio | 💳 De pago |

> [!abstract] Resumen
>
> - Amazon EKS lanza **rollbacks de versión de Kubernetes**, permitiendo revertir una actualización del control plane a la versión menor anterior dentro de los **7 días posteriores** a la actualización.
> - La funcionalidad está disponible **sin costo adicional** en todas las regiones comerciales para clusters en soporte estándar y extendido, aplicándose a todos los clusters EKS (incluyendo nodos autogestionados).
> - Para **EKS Auto Mode**, el rollback incluye tanto el control plane como los nodos gestionados de forma coordinada, respetando los *Pod Disruption Budgets* y ofreciendo una **API de cancelación** para detener el proceso de rollback de nodos en cualquier momento.
> - EKS evalúa automáticamente la **preparación del cluster** mediante *Cluster Insights* (compatibilidad de nodos, add-ons) antes de ejecutar el rollback, aunque se puede forzar omitiendo estas comprobaciones.
> - Esta característica elimina la restricción histórica de "puerta de un solo sentido" en actualizaciones de Kubernetes, reduciendo el riesgo operativo y permitiendo a equipos en entornos regulados mantener clusters actualizados sin miedo a irreversibilidad.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Actualizar clusters de Amazon EKS con confianza usando rollbacks de versión de Kubernetes
> 
> Actualizar el control plane de Kubernetes ha sido durante mucho tiempo una puerta de un solo sentido. Kubernetes de código abierto no admite rollback del control plane, por lo que una vez que actualizas, no hay vuelta atrás.
> 
> La comunidad está logrando progresos reales aquí, y KEP-4330 introduce versiones emuladas para facilitar el rollback.
> 
> Pero en la práctica esta restricción ha empujado a las organizaciones a construir mecanismos de compensación elaborados como bake periods, stagger groups, automated sign offs, y ciclos de actualización de meses.
> 
> Con Kubernetes lanzando tres versiones menores al año, equipos que gestionan cientos de clusters, especialmente en entornos regulados, a menudo retrasan actualizaciones completamente porque no están seguros de que puedan recuperarse si algo sale mal. El resultado son clusters atrapados en versiones más antiguas, perdiendo parches de seguridad, y eventualmente chocando contra los plazos de soporte extendido.
> 
> Hoy anunciamos rollbacks de versión de Kubernetes para Amazon Elastic Kubernetes Service (Amazon EKS), una nueva característica que brinda a los administradores de clusters una red de seguridad al realizar actualizaciones de cluster. Con rollbacks de versión, puedes revertir una actualización de versión de Kubernetes dentro de los siete días si encuentras problemas después de actualizar, regresando tu cluster a su estado anterior y funcional. Donde enfoques como versiones emuladas mantienen un cluster en un estado de transición temporal, el rollback de EKS devuelve tu cluster a una versión completamente validada anterior que se ejecutó en producción, no una emulación de ella. Ahora, si actualizas un cluster de, digamos, Kubernetes 1.34 a 1.35 y descubres un problema de compatibilidad, puedes hacer rollback a 1.34 dentro de los siete días. No hay necesidad de reconstruir tu cluster o hacer malabares para solucionar bajo presión. Piensa en ello como un botón deshacer para actualizaciones de versión de Kubernetes. La característica admite hacer rollback una versión menor a la vez, acercándose al mismo enfoque incremental que EKS usa para actualizaciones. Y para ayudarte a hacer rollback de forma segura, EKS evalúa automáticamente la preparación de rollback de tu cluster a través de cluster insights, señalando elementos como la compatibilidad de versión de nodos o dependencias de add-on antes de proceder. Si ya has evaluado la situación y quieres moverte rápidamente, puedes usar el flag --force para omitir esas comprobaciones. Lo anterior se aplica a todos los clusters EKS, ya sea que gestiones tus propios nodos o dejes que AWS los maneje. Pero para clientes que han adoptado infraestructura totalmente gestionada, el rollback da un paso más adelante. Rollback para EKS Auto Mode EKS Auto Mode te brinda despliegue de un clic de clusters de Kubernetes listos para producción, automatizando la gestión de compute, networking, y storage para que puedas concentrarte en tus aplicaciones en lugar de en infraestructura. EKS Auto Mode introduce consideraciones adicionales para rollbacks de versión porque tanto el control plane como los nodos gestionados necesitan ser rollbacked juntos. Dado que los rollbacks de nodos respetan tus disruption budgets, el proceso puede tomar tiempo dependiendo de tu configuración. Para darte control sobre este proceso, hemos introducido una cancel API que te permite detener un rollback de nodos en cualquier punto. Si decides que el rollback está tomando demasiado tiempo o quieres cambiar tu enfoque, puedes cancelar y ajustar tus disruption budgets para acelerar las cosas, o elegir un camino diferente. Por defecto, EKS nunca omite tus disruption budgets durante un rollback porque priorizamos la estabilidad de la carga de trabajo. Siempre puedes elegir modificar o eliminar tus disruption budgets tú mismo para acelerar el proceso si es necesario.
> 
> Probémoslo
> 
> Para probar rollbacks de versión, navegué a la consola de Amazon EKS y seleccioné uno de mis clusters que había actualizado recientemente. Desde la página de configuración del cluster, puedo ver la opción para iniciar un rollback de versión, junto con información sobre mi ventana de rollback. Antes de iniciar el rollback, revisé los cluster insights para verificar si hay problemas potenciales. Los insights me mostraron el estado de mis nodos y señalaron cualquier cosa que debería abordar antes de proceder. Después de confirmar, el rollback comenzó. Mi cluster permaneció funcional durante todo el proceso. El rollback del control plane tomó aproximadamente 20 minutos, similar a una actualización estándar. Para mi cluster EKS Auto Mode, los nodos se rollbacked gracefully según mis configuraciones de disruption budgets. Una vez completado, mi cluster volvió a la versión anterior de Kubernetes, funcionando como se espera.
> 
> Ya disponibles rollbacks de versión para Amazon EKS están disponibles hoy sin costo adicional en todas las Regiones comerciales de AWS donde Amazon EKS está disponible. Solo pagas los costos estándar de EKS y compute que normalmente incurrirías. No hay cargos adicionales por usar la capacidad de rollback. Los rollbacks del control plane están disponibles para todos los clusters EKS, y los rollbacks de nodos están disponibles para clusters que ejecutan EKS Auto Mode. Los rollbacks de versión admiten clusters que ejecutan versiones de Kubernetes disponibles en EKS standard support y extended support. Para comenzar, visita la documentación de Amazon EKS o pruébala directamente en la consola de Amazon EKS.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Kubernetes native updates lack rollback capability, forcing organizations to delay updates and miss security patches
> - Amazon EKS version rollbacks allow reverting to a previous validated Kubernetes version within 7 days if issues arise
> - The rollback feature is available at no additional cost across all commercial AWS regions and supports both standard and extended Kubernetes support versions

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> Es una nueva característica de Amazon Elastic Kubernetes Service (EKS) que permite revertir actualizaciones de versiones de Kubernetes dentro de los siete días posteriores a la actualización. Actúa como un botón deshacer, devolviendo el clúster a una versión anterior y completamente validada en producción, en lugar de una emulación.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Facilita a los equipos mantener sus clústeres actualizados sin miedo a quedar atrapados en versiones inestables, asegurando la recepción continua de parches de seguridad. Además, reduce la necesidad de construir mecanismos de compensación elaborados y acelera los ciclos de actualización en entornos regulados.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Baja | Existe un botón deshacer para actualizaciones. · Ventana de rollback de siete días. |
| Junior | Media | Rollback a versión validada anterior. · Sin costo adicional en EKS. |
| Semi-Senior | Media | Revertir actualización dentro de 7 días. · Usar cluster insights para compatibilidad. |
| Senior | Alta | Rollback de una versión menor a vez. · Flag --force omite comprobaciones de EKS. · Auto Mode requiere rollback conjunto. |
| Ingeniero de Software | Media | Clúster funcional durante el rollback. · Actualizaciones ya no son irreversibles. |
| Ingeniero en Redes | Baja | EKS Auto Mode automatiza networking. · Rollback respeta configuraciones de red. |
| DevOps / SRE | Alta | Evaluar cluster insights antes de rollback. · Cancel API detiene rollback de nodos. · No omite disruption budgets por defecto. |
| Ciberseguridad | Alta | Facilita aplicar parches de seguridad. · Evita versiones antiguas vulnerables. · Soporta versiones en soporte extendido. |


## Información técnica ⚒️

- **Requisitos:** Kubernetes versions supported by EKS Standard Support and Extended Support; compatible with both self-managed nodes and EKS Auto Mode

## Precio 🪙

> [!money] 💳 De pago

## Fuente original 📜

[https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks/](https://aws.amazon.com/blogs/aws/upgrade-amazon-eks-clusters-with-confidence-using-kubernetes-version-rollbacks/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Upgrading a Kubernetes control plane has long been a one way door. Open source Kubernetes doesn’t support control plane rollback, so once you upgrade, there’s no going back. The community is making real progress here, and KEP-4330 introduces emulated versions to ease rollback. But in practice this constraint has pushed organizations to build elaborate compensating mechanisms like bake periods, stagger groups, automated sign offs, and months long upgrade cycles. With Kubernetes releasing three minor versions per year, teams managing hundreds of clusters, especially in regulated environments, often delay upgrades entirely because they aren’t confident they can recover if something goes wrong. The result is clusters stuck on older versions, missing security patches, and eventually running up against extended support timelines. Today, we’re announcing Kubernetes version rollbacks for Amazon Elastic Kubernetes Service (Amazon EKS) , a new feature that gives cluster administrators a safety net when performing cluster upgrades. With version rollbacks, you can reverse a Kubernetes version upgrade within seven days if you encounter issues after upgrading, returning your cluster to its previous working state. Where approaches like emulated versions keep a cluster in a transitional holding state, EKS version rollback returns your cluster to a fully validated previous version that ran in production, not an emulation of it. Now, if you upgrade a cluster from, say, Kubernetes 1.34 to 1.35 and discover a compatibility issue, you can roll back to 1.34 within seven days. There’s no need to rebuild your cluster or scramble to troubleshoot under pressure. Think of it as an undo button for Kubernetes version upgrades. The feature supports rolling back one minor version at a time, matching the same incremental approach EKS uses for upgrades. And to help you roll back safely, EKS automatically evaluates your cluster’s rollback readiness through cluster insights , flagging items like node version compatibility or add-on dependencies before you proceed. If you’ve already assessed the situation and want to move quickly, you can use the --force flag to bypass those checks. The above applies to all EKS clusters, whether you manage your own nodes or let AWS handle them. But for customers who have embraced fully managed infrastructure, rollback goes a step further. Rollback for EKS Auto Mode EKS Auto Mode gives you one click deployment of production ready Kubernetes clusters, automating compute, networking, and storage management so you can focus on your applications rather than infrastructure. EKS Auto Mode introduces additional considerations for version rollbacks because both the control plane and managed nodes need to be rolled back together. Since node rollbacks respect your pod disruption budgets, the process can take time depending on your configuration. To give you control over this process, we’ve introduced a cancel API that lets you stop a node rollback at any point. If you decide the rollback is taking too long or you want to change your approach, you can cancel and adjust your disruption budgets to accelerate things, or choose a different path forward. By default, EKS never bypasses your disruption budgets during a rollback because we prioritize workload stability. You can always choose to modify or remove disruption budgets yourself to speed up the process if needed. Let’s try it out To try version rollbacks, I navigated to the Amazon EKS console and selected one of my clusters that I had recently upgraded. From the cluster’s configuration page, I can see the option to initiate a version rollback, along with information about my current rollback window. Before initiating the rollback, I reviewed the rollback insights to check for any potential issues. The insights showed me the status of my nodes and flagged anything I should address before proceeding. After confirming, the rollback began. My cluster remained functional throughout the process. The control plane rollback took about 20 minutes, similar to a standard upgrade. For my EKS Auto Mode cluster, the nodes rolled back gracefully according to my disruption budget settings. Once complete, my cluster was back on the previous Kubernetes version, running as expected. Now available Kubernetes version rollbacks for Amazon EKS are available today at no additional cost in all commercial AWS Regions where Amazon EKS is available. You pay only for the standard EKS and compute costs you would normally incur. There are no extra charges for using the rollback capability. Control plane rollbacks are available for all EKS clusters, and node rollbacks are available for clusters running EKS Auto Mode. Version rollbacks support clusters running Kubernetes versions available in EKS standard support and extended support. To get started, visit the Amazon EKS documentation or try it out directly in the Amazon EKS console .

</details>

