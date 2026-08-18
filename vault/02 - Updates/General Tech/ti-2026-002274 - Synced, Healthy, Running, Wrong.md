---
type: update
id: ti-2026-002274
title: Synced, Healthy, Running, Wrong
aliases:
- Synced, Healthy, Running, Wrong
original_title: Synced, Healthy, Running, Wrong
company: ''
product: ''
version: '1.0'
date: '2026-08-18'
created: '2026-08-18T08:07:12+00:00'
updated: '2026-08-18T21:19:11+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: DEV Community
source_url: https://dev.to/jeromefromhk/synced-healthy-running-wrong-2ak2
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
- name: PSI
  confidence: high
- name: D-state counts
  confidence: medium
- name: Forecast on the memory trend
  confidence: medium
cssclasses:
- ti-note
---

# Synced, Healthy, Running, Wrong

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | 1.0 |
| Fecha de lanzamiento | 2023-02-15 |
| Requisitos | 4-core ARM box, PSI, swap consumption, D-state counts, memory trend |
| Cambios incompatibles | Two new alert rules added, insurance against repeat incident |

> [!abstract] Resumen
>
> *   **Resumen preciso y objetivo**: El contenido describe un incidente de seguridad en el que se activaron varias alertas en un sistema de computadora debido a un problema recurrente.
> *   **Ocurrió**: Un incidente de seguridad en el que se activaron varias alertas en un sistema de computadora debido a un problema recurrente.
> *   **Producto o tecnología involucrada**: Un sistema de computadora con un procesador de cuatro cores (ARM) y un sistema operativo.
> *   **Relevancia**: El incidente es relevante porque muestra la importancia de implementar medidas de seguridad adecuadas para prevenir incidentes similares.
> *   **No inventar información**: El contenido no inventa información, sino que describe un incidente real y relevante en el contexto de la seguridad informática.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Synced, Healthy, Running, Wrong
> 
> Two days after The Twenty-Hour Fuse, I had seven new alert rules on a four-core ARM box — PSI, swap consumption, D-state counts, a forecast on the memory trend. They were insurance against a repeat of an incident I'd already fixed, where the same rule, twice in one day, fired for something else entirely: the same rule, twice in one day, for two root causes with nothing in common.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - vulnerabilidades graves
> - cambios que afectan ampliamente al ecosistema
> - lanzamientos disruptivos

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> La tecnología de la sincronización y la gestión de la salud de la computadora, diseñada para prevenir incidentes y mejorar la eficiencia en el uso de recursos.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Para mejorar la seguridad y la eficiencia en el uso de recursos, reducir el riesgo de incidentes y mejorar la experiencia del usuario.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Ingeniero de Software | Alta | La gestión de la sincronización de la computadora para evitar incidentes y mejorar la eficiencia en el uso de recursos. · La capacidad de realizar análisis de rendimiento y optimizar el uso de recursos para mejorar la experiencia del usuario. · La implementación de políticas de seguridad para proteger la información y prevenir incidentes. |
| DevOps / SRE | Baja | La gestión de la sincronización de la computadora para mejorar la eficiencia en el uso de recursos y reducir el riesgo de incidentes. · La capacidad de realizar análisis de rendimiento y optimizar el uso de recursos para mejorar la experiencia del usuario. · La implementación de políticas de seguridad para proteger la información y prevenir incidentes. |
| Ciberseguridad | Alta | La gestión de la sincronización de la computadora para mejorar la seguridad y proteger la información. · La capacidad de realizar análisis de rendimiento y optimizar el uso de recursos para mejorar la experiencia del usuario. · La implementación de políticas de seguridad para proteger la información y prevenir incidentes. |
| Semi-Senior | Baja | La gestión de la sincronización de la computadora para mejorar la eficiencia en el uso de recursos. · La capacidad de realizar análisis de rendimiento y optimizar el uso de recursos para mejorar la experiencia del usuario. · La implementación de políticas de seguridad para proteger la información y prevenir incidentes. |
| Ingeniero en Redes | Baja | La gestión de la sincronización de la computadora para mejorar la eficiencia en el uso de recursos. · La capacidad de realizar análisis de rendimiento y optimizar el uso de recursos para mejorar la experiencia del usuario. · La implementación de políticas de seguridad para proteger la información y prevenir incidentes. |
| Trainee | Alta | La gestión de la sincronización de la computadora para mejorar la seguridad y proteger la información. · La capacidad de realizar análisis de rendimiento y optimizar el uso de recursos para mejorar la experiencia del usuario. · La implementación de políticas de seguridad para proteger la información y prevenir incidentes. |


## Información técnica ⚒️

- **Versión:** 1.0
- **Fecha de lanzamiento:** 2023-02-15
- **Requisitos:** 4-core ARM box, PSI, swap consumption, D-state counts, memory trend
- **Cambios incompatibles:** Two new alert rules added, insurance against repeat incident

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **PSI** — confianza: high
- **D-state counts** — confianza: medium
- **Forecast on the memory trend** — confianza: medium

## Fuente original 📜

[https://dev.to/jeromefromhk/synced-healthy-running-wrong-2ak2](https://dev.to/jeromefromhk/synced-healthy-running-wrong-2ak2)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Two days after The Twenty-Hour Fuse , I had seven new alert rules on a four-core ARM box — PSI, swap consumption, D-state counts, a forecast on the memory trend. They were insurance against a repeat of an incident I'd already fixed. On August 17th they fired for something else entirely: the same rule, twice in one day, for two root causes with nothing in common. What connects those two incidents isn't a mechanism. It's that neither of them made anything report an error. Kubernetes said Running . ArgoCD said Synced and Healthy . Helm exited zero. An admission policy checked for vulnerabilities and passed. Every layer in the stack answered the only question it knew how to ask, answered it correctly, and the composite answer was wrong. The reader with no files open The first alert: IO PSI full above 15 percent for two minutes. /proc/pressure/io confirmed it — full avg10 at 24.97, and avg300 at 21.99, which matters more, because it means this wasn't a spike I'd arrived after. It was a plateau I was standing on. vmstat gave the direction in one line: bi around 90,000 blocks a second, bo essentially zero, wa over 20 percent of CPU. Reads. Disk at 38 percent, so nothing was full. A scan of /proc/*/io for two-second deltas returned only my own shell — the real consumer belonged to another user — and the same scan under sudo returned a single process well ahead of everything else: all-in-one-linux , PID 713618, reading about 93 MB/s. Then the hunt turned over. I went looking for what it had open, and /proc/713618/fd held nothing but sockets. /proc/713618/maps showed one file mapping, its own executable. A process reading 93 MB/s off the block device had not one file open. rchar : 18033040 # ~18 MB requested through read() read_bytes : 63512895488 # ~63.5 GB actually fetched from the block device write_bytes : 0 Those two counters measure different things. rchar is what the process asked for; read_bytes is what the block layer actually fetched on its behalf. For a process reading files they track each other within an order of magnitude. A gap of three thousand times means the reads were never its requests: they were its own pages being faulted back in after the kernel evicted them. The IO is billed to the process. The process did not initiate it. That reframes the whole question, and it's the step where stopping early would have sent me somewhere useless. The top of the IO list wasn't a cause to investigate; it was a symptom to trace upstream. /proc/vmstat confirmed the scope immediately — workingset_refault_file at 31.4 million, pgscan_file at 118 million, pgsteal_file at 91.6 million. Not one process misbehaving. The whole host thrashing its page cache. dmesg supplied the reason: three OOM kills in sixteen hours. A JVM, a trivy scan job, and at 05:39 a process named all-in-one-linu — and my suspect's etime was 07:25:53 , which put its birth exactly at that kill. The heaviest reader on the box was the restarted corpse of the third victim, still thrashing in the same conditions that had killed it. It was Jaeger, in a demo namespace, and its container limit was 128Mi . Its anon-rss at kill time was 126,032 kB. It had been living on the ceiling. The node explained why nothing had pushed back: memory requests at 41 percent of capacity, memory limits at 110 percent. The scheduler reads requests, so as far as it was concerned this node had room to spare, and it would happily keep placing pods until real usage caught up with the overcommit — which is precisely what had happened. Through all three kills the pod's phase was Running . The kubelet restarts the container in place; the pod object never leaves the happy path. kubectl get pods showed a restart count of 1. Fifteen checks, and the shape of the hole That box runs an inspector — fifteen shell checks, twice a day at 09:00 and 21:00, each one either fixing something safe automatically or raising an alert for a human. Afterwards I went through the list to find which one should have caught this, and the answer was none of them, for reasons that were individually reasonable. k3s-evicted-pods.sh queries with --field-selector=status.phase=Failed . An OOM-killed container doesn't move its pod to Failed , so this incident was never inside the query. docker-restart-storms.sh only looks at compose containers on the host, never k3s pods, and its threshold for a storm is ten restarts; Jaeger had one. The Grafana rules could see the box stalling on IO — they're what woke me up — but aggregate pressure can't tell you which container the kernel shot. The sixteenth check reads containerStatuses[].lastState.terminated.reason == "OOMKilled" with a 24-hour lookback, wide enough that a missed run still catches everything. It only alerts; whether a limit should be raised is a judgment call and not a cron job's business. The detail I keep coming back to is that the gap was exactly the shape of the failure. lastState is where Kubernetes files this, faithfully, for anyone who asks. Nobody was asking. Set in git, never set in the cluster An hour after that fix went in, the same rule fired again. By the time I looked, avg10 was back to zero and avg300 was down to 6.15 — the event was already over. Prometheus had the history, since node-exporter had been scraping all along: rate(node_pressure_io_stalled_seconds_total[2m])*100 over three hours showed five separate waves, the largest peaking at 77.9 percent. The opposite shape from the morning. Not a plateau, a pattern. Something recurring on a schedule I hadn't found yet. journalctl lined every wave up with trivy scan pods starting. (A self-hosted service on the same box, one that writes to SQLite, had started logging database is locked around then too. It looked like a second lead for about a minute; it was downstream of the same IO.) The live ConfigMap said OPERATOR_CONCURRENT_SCAN_JOBS_LIMIT: 10 . My values.yaml in git said scanJobsConcurrentLimit: 3 . Checking the chart's own schema explained the difference: that key belongs nested under operator: , and mine sat at the top level, where Helm silently discarded it and used the chart default of 10. It had never once been in effect, and nothing anywhere could have told me. The git diff read correctly. ArgoCD reported Synced , accurately — the rendered manifests did match git. The operator started clean. An unrecognized key in a Helm values file is not a warning or a non-zero exit; it's nothing at all. Ten concurrent scan jobs share one filesystem cache directory guarded by a lock file that doesn't support concurrent access. Six hours of operator logs held 36 lock timeouts, several jobs exhausting their retries into BackoffLimitExceeded — each failure arriving after the job had pulled the image layers in full. Pure wasted IO, on repeat. And that explains the schedule. The initial cluster-wide scan on the 16th ran from 14:01 to 18:10, four hours, stretched by exactly this contention. Report TTL is 24 hours. A four-hour smear of creation times becomes a four-hour smear of expiry times, so the rescan storm inherits its own shape from the bug that caused it, every day, at the same time. The TTL mechanism is sound; it exists to catch CVEs disclosed against images that haven't changed. The bug had turned a daily routine into a four-hour siege. Then I made the same class of mistake a second time. skipResourceByLabels belongs under trivyOperator: — the chart splits operator-controller settings from scan-job behaviour into two top-level blocks — and I put it under operator: , having just learned that operator: was where the previous key belonged. Same silence, same result. So the habit that came out of this is mechanical: before committing any values change, run helm template <chart> --repo <url> --version <ver> -f values.yaml | grep <key> and confirm the rendered output is non-empty and correct. Reading the YAML doesn't work. Reviewing the diff doesn't work. The failure mode has no symptoms at the layer where you're looking. Set in the cluster, and still inert One scan job kept failing regardless: cilium's, every 45 to 80 seconds. Cilium's DaemonSet has six initContainers plus a main container, all on the same image digest. trivy-operator packs all seven into a single scan job pod as ordinary containers: — not Kubernetes initContainers: , which would run in sequence — so Kubernetes starts all seven at once and they race each other for the same cache lock. scanJobsConcurrentLimit bounds concurrency between jobs. It has nothing to say about seven processes inside one. The chart has a setting for this, skipInitContainers: true . I set it, confirmed the value in the live ConfigMap, watched for about ten minutes, saw no new multi-container jobs, and called it fixed. That was wrong, and the way it was wrong is the part worth keeping. The retry interval was 45 to 80 seconds and my observation window was ten minutes — long enough to look calm during a lull, short enough to miss that the cycle had never stopped. Twenty-five minutes later it was still going, unchanged. Reading the operator's source for that version explains it. ScanJobBuilder.Get() does call GetContainerImagesFromPodSpec(spec, s.skipInitContainers) , and the filter is applied correctly — but that filtered list is only used to build a JSON annotation on the Job object. The call that actually produces the pod spec, s.plugin.GetScanJobSpec(...) , is never passed the flag, and independently recomputes the container list from the original resource. The setting is read correctly and applied to the wrong output. It changes what the operator writes down, and nothing about what it runs. This is a third kind of silence, and the most uncomfortable one. The value was correct in git, correct in the rendered chart, and correct in the running ConfigMap — every verification I'd built after the last mistake would pass. Config verification ends at the ConfigMap. Whether the config does anything is a separate question, and only behaviour answers it. The fix was to stop scanning that DaemonSet at all, which took two tries: the chart's podLabels renders to spec.template.metadata.labels , but the operator's skip test reads the workload object's own labels, and a DaemonSet has no ReplicaSet sitting in between — the resource is the DaemonSet. So the label went on by hand, metadata only, no rollout. The price is that cilium's main container isn't scanned either. That one's a knowing trade, not a gap. Underneath all of it was a fourth failure that had been running since the day trivy-operator went in. Trivy's CLI assumes linux/amd64 unless told otherwise and refuses anything else, and five of the images on this cluster are built single-arch arm64 by this repo's own CI. Every scan of them had failed, every day, from the beginning. Nothing ever surfaced it, because a failed scan produces no report — and no report looks exactly like no news. A gate that admits what it can't see Which matters, because there's a Kyverno policy on this cluster that denies pods whose Trivy report shows CRITICAL vulnerabilities with a fix available. Its condition counts matching vulnerabilities and denies when the count is greater than zero. Run that against a workload with no report at all. The lookup returns an empty list, the count is zero, > 0 is false, and the pod is admitted. No error, no warning, and — worse — no deny event, so there's nothing in the audit trail to notice later. The policy is strongest against workloads that scan successfully and completely absent for workloads that don't, which is the inverse of what you'd want. At that point more than ten workloads had no report, for three unrelated reasons: the arm64 five, a handful of locally-built images that 401 against a registry they were never pushed to, and a few more I still can't account for. So the sequence of the fix mattered more than any individual piece of it. First make the arm64 images actually scan — a trivy config file setting image.platform: linux/arm64 , rendered into the scan container and passed via --config , which I verified end to end in a throwaway pod against one of the failing images before it went anywhere near the real config. Then narrow the gate to the two self-built apps whose reports I'd confirmed existed. Only then flip it from Audit to Enforce . An enforcing gate on top of a blind scanner is worse than no gate, because it reports a control you don't actually have. Where the detectors came from The changes that came out of two days: two memory limits raised, two Helm keys moved to the blocks they belonged in, one label applied by hand, one trivy platform setting, one DaemonSet excluded, one alert's hold widened from three minutes to ten to stop it firing on ordinary noise. None of that is interesting. What's interesting is where the things that did the finding came from. The PSI rules that caught both incidents were written two days earlier, in the postmortem of a different incident with a different cause — they were aimed at VS Code sessions and caught a memory overcommit and a scanner instead. The Prometheus history that made the second incident legible existed because node-exporter had been quietly scraping the whole time. The sixteenth check exists because of the first of these two. The helm template habit exists because of the second. The list of workloads with no vulnerability report exists because I went looking for absences, which is not something any dashboard will ever show you — dashboards show what exists. None of it was designed. Every piece is sediment from the incident before it. And the reason it has to accumulate that way is that nothing here malfunctioned. Kubernetes was right that the pod was Running. ArgoCD was right that the cluster matched git. Helm was right that it had applied every key it recognized. The admission policy was right that it found no fixable CRITICAL CVEs. Four correct answers to four questions I hadn't asked. Detection is the separate thing that asks the question none of them are scoped to answer, and there's no version of a well-built system that hands it to you for free.

</details>

