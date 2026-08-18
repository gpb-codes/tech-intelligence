# Tech Intelligence

_Actualizado: 2026-08-18 05:01 UTC · Sistema local-first · Procesado con Ollama_

## Últimas actualizaciones

```dataview
TABLE date, importance, company, product, source FROM "02 - Updates" WHERE status = "published" SORT date DESC LIMIT 20
```


## IA

```dataview
TABLE date, importance, product FROM "02 - Updates/IA" WHERE contains(category, "IA") SORT date DESC LIMIT 10
```


## Developer Tools

```dataview
TABLE date, importance, product FROM "02 - Updates/Developer Tools" WHERE contains(category, "Developer Tools") SORT date DESC LIMIT 10
```


## Open Source

```dataview
TABLE date, importance, product FROM "02 - Updates/Open Source" WHERE contains(category, "Open Source") SORT date DESC LIMIT 10
```


## Cloud

```dataview
TABLE date, importance, product FROM "02 - Updates/Cloud" WHERE contains(category, "Cloud") SORT date DESC LIMIT 10
```


## Cybersecurity

```dataview
TABLE date, importance, product FROM "02 - Updates/Cybersecurity" WHERE contains(category, "Cybersecurity") SORT date DESC LIMIT 10
```


## Hardware

```dataview
TABLE date, importance, product FROM "02 - Updates/Hardware" WHERE contains(category, "Hardware") SORT date DESC LIMIT 10
```


## Productivity

```dataview
TABLE date, importance, product FROM "02 - Updates/Productivity" WHERE contains(category, "Productivity") SORT date DESC LIMIT 10
```


## General Tech

```dataview
TABLE date, importance, product FROM "02 - Updates/General Tech" WHERE contains(category, "General Tech") SORT date DESC LIMIT 10
```


## Cambios de precio

```dataview
TABLE date, product, pricing FROM "02 - Updates" WHERE pricing != "unknown" AND pricing != "open-source" SORT date DESC LIMIT 15
```


## Nuevos modelos

_Sin modelos detectados aún._

## Alternativas gratuitas / open source

_Sin alternativas detectadas aún._

## GitHub

_Sin actividad de GitHub aún._

## Tendencias / Investigación

_Sin investigaciones detectadas aún._

## Tech Radar

```dataview
TABLE status, category FROM "10 - Radar" SORT status DESC
```

Anillos: **ADOPT** · **TRIAL** · **ASSESS** · **HOLD**  
_El Radar se actualiza manualmente en `10 - Radar/`._
