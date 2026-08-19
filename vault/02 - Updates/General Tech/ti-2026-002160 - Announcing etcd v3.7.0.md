---
type: update
id: ti-2026-002160
title: Announcing etcd v3.7.0
aliases:
- Announcing etcd v3.7.0
original_title: Announcing etcd v3.7.0
company: ''
product: ''
version: 3.7.0
date: '2026-07-08'
created: '2026-07-08T12:00:00+00:00'
updated: '2026-08-19T17:58:07+00:00'
original_language: en
translated: true
importance: high
impact: medium
pricing: free
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/07/08/announcing-etcd-3.7/
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
tags:
- etcd
- v3.7.0
- minor release
- distributed key-value store
- core kubernetes component
alternatives:
- name: Confluent KSQL
  confidence: high
- name: Apache Cassandra
  confidence: medium
cssclasses:
- ti-note
---

# Announcing etcd v3.7.0

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟢 Alta` · `🌐 Medio` · `💰 Gratis`

| Campo | Valor |
| --- | --- |
| Versión | 3.7.0 |
| Fecha de lanzamiento | 2023-03-01 |
| Requisitos | etcd v3.7.0 |
| Cambios incompatibles | RangeStream feature, performance improvements, protobuf overhaul |
| Precio | 💰 Gratis |

> [!abstract] Resumen
>
> * Etcd v3.7.0 se lanza con la nueva versión minor de la base de datos distribuida y componente de Kubernetes popular.
> * La nueva versión incluye la implementación de la característica RangeStream, así como varias mejoras de rendimiento y una revisión profunda de protobuf.
> * La eliminación de la versión v2store y la completión de la actualización de protobuf son aspectos clave de la actualización.
> * Etcd v3.7.0 es relevante para los desarrolladores de sistemas y aplicaciones que buscan mejorar la escalabilidad y la eficiencia de sus infraestructuras.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Announcing etcd v3.7.0
> 
> This article is a mirror of the original announcement Today, SIG etcd is releasing etcd v3.7.0, the latest minor release of the popular distributed key-value store and core Kubernetes component. v3.7 ships the long-requested RangeStream feature, delivers several other performance improvements, removes the last remnants of the legacy v2store, and completes a major protobuf overhaul.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - RangeStream
> - performance improvements
> - protobuf overhaul

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> etcd v3.7.0 es una versión minor de la popular distribución de clave-valor y componente clave de Kubernetes, que proporciona un almacenamiento centralizado y escalable para aplicaciones de código abierto.

> [!tip] ¿En qué ayuda al desarrollo?
>
> etcd v3.7.0 ofrece varias mejoras de rendimiento y despliegue, incluyendo la implementación de la función de cadena de rango (RangeStream), que permite a las aplicaciones acceder y manipular los datos de manera más eficiente.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. · La implementación de la función de cadena de rango (RangeStream) permite a las aplicaciones acceder y manipular los datos de manera más eficiente. |
| Junior | Media | Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. · La implementación de la función de cadena de rango (RangeStream) permite a las aplicaciones acceder y manipular los datos de manera más eficiente. |
| Semi-Senior | Alta | Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. · La implementación de la función de cadena de rango (RangeStream) permite a las aplicaciones acceder y manipular los datos de manera más eficiente. · Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. |
| Senior | Alta | Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. · La implementación de la función de cadena de rango (RangeStream) permite a las aplicaciones acceder y manipular los datos de manera más eficiente. · Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. |
| Ingeniero de Software | Alta | Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. · La implementación de la función de cadena de rango (RangeStream) permite a las aplicaciones acceder y manipular los datos de manera más eficiente. · Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. |
| Ingeniero en Redes | Alta | Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. · La implementación de la función de cadena de rango (RangeStream) permite a las aplicaciones acceder y manipular los datos de manera más eficiente. · Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. |
| DevOps / SRE | Alta | Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. · La implementación de la función de cadena de rango (RangeStream) permite a las aplicaciones acceder y manipular los datos de manera más eficiente. · Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. |
| Ciberseguridad | Alta | Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. · La implementación de la función de cadena de rango (RangeStream) permite a las aplicaciones acceder y manipular los datos de manera más eficiente. · Etcd es una herramienta de almacenamiento centralizado y escalable que permite a las aplicaciones de código abierto acceder y manipular los datos de manera eficiente. |


## Información técnica ⚒️

- **Versión:** 3.7.0
- **Fecha de lanzamiento:** 2023-03-01
- **Requisitos:** etcd v3.7.0
- **Cambios incompatibles:** RangeStream feature, performance improvements, protobuf overhaul

## Precio 🪙

> [!money] 💰 Gratis
>
> $20/mes

## Alternativas 🔄

- **Confluent KSQL** — confianza: high
- **Apache Cassandra** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/07/08/announcing-etcd-3.7/](https://kubernetes.io/blog/2026/07/08/announcing-etcd-3.7/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

This article is a mirror of the original announcement Today, SIG etcd is releasing etcd v3.7.0 , the latest minor release of the popular distributed key-value store and core Kubernetes component. v3.7 ships the long-requested RangeStream feature, delivers several other performance improvements, removes the last remnants of the legacy v2store, and completes a major protobuf overhaul. You can download etcd v3.7.0 here: Source code Binaries Official container images This release also includes new versions of the two core etcd dependencies, bbolt v1.5.0 and raft v3.7.0 . For instructions on installing etcd, see the install documentation . For the full list of changes, see the etcd v3.7 changelog . A heartfelt thank you to all the contributors who made this release possible! Major features The most significant changes in v3.7.0 include: RangeStream — stream large result sets in chunks instead of buffering the whole response. Keys-only range requests, faster and more reliable leases, and several other performance improvements . etcd now boots entirely from v3store , eliminating a long-standing dependency on the legacy v2 store A completed protobuf overhaul , replacing outdated protobuf libraries with fully supported ones. etcd v3.7 ships with bbolt v1.5.1 and raft v3.7.0 . Features RangeStream In etcd v3.6 and earlier, it is challenging to work with requests that return large result sets. The database would buffer the full result set before sending, leading to unpredictable latency and memory usage, both on the server and the client. The RangeStream RPC lets calling applications accept result sets in chunks, reducing latency and making buffering memory usage more predictable. Instructions on how to use RangeStream in gRPC calls and in etcdctl can be found in the etcd documentation. Users should try it out for their own applications. In coordinated releases, the RangeStream feature will become available to users running the upcoming v1.37 of Kubernetes by enabling the EtcdRangeStream feature gate. This early and planned adoption is possible thanks to the merger of etcd and Kubernetes development in 2023. Performance improvements v3.7 delivers multiple specific performance improvements, both for the Kubernetes control plane and for other use cases. Kubernetes users should see a significant decrease in overall CPU usage by the etcd members, compared with v3.6. Keys-only range optimization etcd v3.7.0 includes a keys-only Range optimization ( #21791: keys-only Range optimization ). When processing a keys_only Range request or etcdctl get --keys-only , etcd reads solely from its in-memory index. It returns the matched keys without loading all serialized values from bbolt as it did previously. The only exception where loading from bbolt is still required is when keys_only Range requests must be sorted by value (i.e., when SortTarget is set to VALUE). This reduces unnecessary backend reads and memory use for workloads that only need key names, making large keys-only range requests more efficient. Faster, more reliable etcd leases v3.7 improves lease expiration and renewal: LeaseRevoke requests are now prioritized to ensure timely lease expiration during overload ( #20492: stability enhancement during overload conditions ). The new FastLeaseKeepAlive feature enables faster lease renewal by skipping the wait for the applied index ( #20589: etcdserver: improve linearizable renew lease ). Faster find() operations etcd 3.7 improves the performance of concurrent watches on keys by making find() operations faster ( #19768: adt: split interval tree by right endpoint on matched left endpoints ). Other features Protobuf overhaul v3.7 migrates and replaces multiple outdated protobuf libraries with fully supported dependencies. This includes replacing github.com/golang/protobuf and github.com/gogo/protobuf with the fully-supported google.golang.org/protobuf ( #14533: Protobuf: cleanup both golang/protobuf and gogo/protobuf ), and migrating grpc-logging to grpc-middleware v2 ( #20420: Migrate grpc-logging to grpc-middleware v2 ). As well as improving security and maintainability, this refactor has been shown to reduce CPU usage by etcd components. While these changes are not expected to directly affect users running etcd via official binaries or container images, they may affect users who depend on etcd Go modules, such as the client SDK or packages under api/ or pkg/ . These consumers may need to update their code or dependencies due to protobuf and related API changes introduced in this release. More detailed information is available from the API change tracking issue . Unix socket support etcd now supports Unix socket endpoints ( #19760: Add Support for Unix Socket endpoints ), enabling local communication without a TCP port. Since this is restricted to single-member clusters, it is mainly aimed at development, testing, and edge device use-cases. Bootstrap from v3store One of the major changes in etcd v3.7 is that the server now bootstraps entirely from the v3 store ( #20187 Bootstrap etcdserver from v3store ), eliminating its dependency on the legacy v2 store during startup. This milestone is the result of a long-term effort spanning multiple releases, from v3.4 through v3.7. It resolves a long-standing technical debt, significantly simplifies the bootstrap workflow, and lays the foundation for future improvements to etcd. To maintain backward compatibility, etcd v3.7 continues to generate v2 snapshots. As a result, the --snapshot-count flag is also retained in v3.7. This is the last remaining dependency on the legacy v2 store, and both the v2 snapshot generation and the --snapshot-count flag will be removed in v3.8. etcdutl timeouts All etcdutl commands now have a timeout command line argument ( #20708: etcdutl: enable timeout functionality for all commands ), so offline utility commands no longer block indefinitely when holding a lock. Setting the authentication token directly Client v3 now allows users to set the JWT directly, offering more flexibility in authentication options ( #16803: clientv3: allow setting JWT directly , #20747: clientv3: disable auth retry when token is set ), Retrieve AuthStatus without authenticating Clients can check their AuthStatus without attempting to authenticate first, eliminating some application overhead ( #20802: etcdserver: remove permission check on AuthStatus api ). New watch metrics v3.7 adds optional watch send-loop metrics ( #21030: Instrument watchstream send loop ) for better observability of the watch path: etcd_debugging_server_watch_send_loop_watch_stream_duration_seconds etcd_debugging_server_watch_send_loop_watch_stream_duration_per_event_seconds etcd_debugging_server_watch_send_loop_control_stream_duration_seconds etcd_debugging_server_watch_send_loop_progress_duration_seconds There is also a new etcd_server_request_duration_seconds metric ( #21038: Add metric etcd_server_request_duration_seconds ). etcdctl command cleanup etcdctl commands were reorganized for clarity ( #20162: etcdctl: organize etcdctl subcommand ) and global command line arguments are now hidden to streamline help output ( #20493: etcdctl: hide global flags ). Upgrading This release contains breaking changes, particularly around the removal of legacy v2 components. Users should review the upgrade guide before upgrading their nodes. As with all minor releases, perform a rolling upgrade one member at a time and confirm cluster health between steps. Experimental flags removed All deprecated experimental flags have been removed ( #19959: Cleanup the deprecated experimental flags ). Features in etcd now follow the Kubernetes-style feature-gate lifecycle (Alpha → Beta → GA) introduced in v3.6, rather than the old --experimental prefix. If your configuration still relies on --experimental-* command line arguments, migrate to using the corresponding feature gates or stable command line arguments before you upgrade to etcd 3.7. Legacy V2 API packages and code cleanup To remove the dependencies on v2store, the following components have been removed: v2 discovery ( #20109: Remove v2discovery ) packages removed, v2 request support ( #21263: Remove v2 Request and apply_v2.go ) v2 client support ( #20117: Remove client/internal/v2 ). These changes may create some breakage for users, particularly those who have not already updated to v3.6.11 or later. Users should report any blockers encountered, or cases that need better upgrade documentation. Non-blocking client creation etcd no longer honors the deprecated grpc.WithBlock dial option ( #21942: Make the etcd client creation non-blocking ). To preserve the previous blocking behavior when needed, follow the guidance in grpc-go's anti-patterns documentation . Multiarch container images only For users relying on the official etcd container images, v3.7 will be distributed only as multiarch containers. Architecture-tagged images will not be available, so adjust deployments accordingly. API changes As with every etcd release, there are a number of API changes. These are designed to be backwards-compatible to the extent possible, but may require adjustment by some users. See our API documentation page for full information. bbolt v1.5.1 etcd v3.7 depends on, and includes, v1.5.1 of the bbolt storage engine. v1.5 includes several improvements to functionality and performance, including: Database file size limits : users may set, and bbolt will enforce, file size limits. When a bolt database exceeds these limits it will refuse to accept writes until the database is compacted or the limit is changed. Disable statistics for performance : users may set NoStatistics to limit overhead from locks taken by the database statistics viewer. More efficient hashmap processing : merge spans faster and with less overhead. raft v3.7.0 etcd 3.7 depends on, and includes, v3.7.0 of the raft consensus engine. v3.7 includes several improvements, including: Update the bootstrap process : v3.7 now allows booting from partly initialized snapshots, supporting etcd's initializing directly from v3store. Improve the ReadIndex flow to prevent stale reads by injecting a unique identifier into the heartbeat context for read-only operations. raft v3.7.0 also includes the same protobuf library updates and refactoring as etcd does. Dependency updates Other dependency updates include a bump to golang.org/x/crypto v0.52.0 for CVE resolution ( #21903: [release-3.7] Bump golang.org/x/crypto to v0.52.0 ), an OpenTelemetry contrib update to v0.61.0 ( #20017: Update otelgrpc to v0.61.0 ), and compilation with Go 1.26.4 ( #21891: [release-3.7] Update Go to 1.26.4 ). Contributors etcd v3.7.0 is the product of more than a hundred contributors across the community. Thank you to everyone who wrote code, reviewed PRs, filed and triaged issues, and helped test the alpha, beta, and release candidates. Leads The SIG etcd leads for the v3.7 release are ivanvc , serathius , ahrtr , fuweid , siyuanfoundation , and jberkus . Ivan leads our release team. Other contributors ah8ad3 , ajaysundark , aladesawe , amosehiguese , ArkaSaha30 , ashikjm , AwesomePatrol , dims , Elbehery , gangli113 , henrybear327 , Jille , jmhbnz , joshuazh-x , kishen-v , lavishpal , liggitt , marcelfranca , miancheng7 , mmorel-35 , MrDXY , mrueg , purpleidea , qsyqian , redwrasse , ronaldngounou , skitt , spzala , tcchawla , tjungblu , vivekpatani , wenjiaswe New contributors A special welcome to the contributors who made their first etcd contribution in this cycle — including Jeffrey Ying , whose work drove the RangeStream feature. New contributors can have a substantial impact on etcd; if you’d like to get involved, see the contributor guide . 1911860538 , 4rivappa , aaronjzhang , abdurrehman107 , ABin-Huang , adeptvin1 , aditya7880900936 , AHBICJ , akstron , alliasgher , aman4433 , aojea , apullo777 , AR21SM , arturmelanchyk , AshrafAhmed9 , asttool , asutorufa , BBQing , beforetech , boqishan , caltechustc , carsontham , christophsj , chuanye-gao , cnuss , cuiweixie , dmvolod , Dogacel , dongjiang1989 , EduardoVega , evertrain , eyupcanakman , gaganhr94 , goingforstudying-ctrl , greenblade29 , Himanshu-370 , HossamSaberX , huajianxiaowanzi , hwdef , ishan-gupta2005 , ishan16696 , ivangsm , JasonLove-Coding , Jefftree , jihogh , jonathan-albrecht-ibm , joshjms , kairosci , kei01234kei , kjgorman , kovan , kstrifonoff , Kunalbehbud , letreturn , lorenz , m4l1c1ou5 , madhav-murali , madvimer , majiayu000 , marcus-hodgson-antithesis , mattsains , mcrute , mingl1 , MohanadKh03 , mstrYoda , NAM-MAN , neeraj542 , nicknikolakakis , nihalmaddala , niuyueyang1996 , notandruu , ntdkhiem , nwnt , olamilekan000 , pigeio , pjsharath28 , progmem , Qian-Cheng-nju , quocvibui , ravisastryk , robin-vidal , robinkb , rockswe , roman-khimov , rsafonseca , sahilpatel09 , SalehBorhani , SebTardif , seshachalam-yv , shashwat010 , shivamgcodes , shuan1026 , silentred , sneaky-potato , socketpair , srri , subrajeet-maharana , sxllwx , tchap , tsujiri , tzfun , upamanyus , uzairhameed , varunu28 , vihasmakwana , wendy-ha18 , xiaoxiangirl , xigang , xUser5000 , yagikota , yajianggroup , yedou37 , Zanda256 , zechariahkasina , zhijun42 , zhoujiaweii Feedback can be shared through: GitHub issues #sig-etcd slack channel in Kubernetes Slack etcd-dev mailing list

</details>

