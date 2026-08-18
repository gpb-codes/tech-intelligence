---
type: template
title: Company
desc: Plantilla para una empresa del ecosistema
---

---
type: company
name: ""
aliases: []
founded: ""
hq: ""
employees: ""
website: ""
public: false
ticker: ""
focus: ""
tags: []
created: ""
updated: ""
cssclasses: [ti-note]
---

# {{name}}

`🏢 Empresa`

## Qué hace

> [!abstract] En una frase
> 

## Productos / Modelos

- 

## Cobertura reciente

```dataview
TABLE date, product, importance FROM "02 - Updates" WHERE company = "{{name}}" SORT date DESC LIMIT 10
```

## Notas