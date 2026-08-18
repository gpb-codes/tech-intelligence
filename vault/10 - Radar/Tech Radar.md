---
type: radar
title: Tech Radar
aliases: [Radar]
cssclasses: [ti-note]
---

# ⛰️ Tech Radar

<span class="ti-runes">ᛟ ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ ᛟ</span>

El Radar clasifica tecnologías según su madurez y utilidad para ti. Cada tecnología es una nota con `type: trend` y un campo `ring`.

## Anillos ⚔️

| Anillo | Significado | Color |
| ------ | ----------- | ----- |
| **ADOPT** | Estándar de facto: úsala de forma normal | 🟢 |
| **TRIAL** | Vale la pena probarla en proyectos controlados | 🔵 |
| **ASSESS** | Investigarla antes de decidir | 🟡 |
| **HOLD** | Esperar; aún no adoptarla | 🔴 |

## Radar actual

```dataview
TABLE ring AS "Anillo", category AS "Categoría", date AS "Añadido", file.link AS "Nota"
FROM "10 - Radar"
WHERE type = "trend"
SORT ring ASC, date DESC
```

## Por anillo

```dataview
LIST
FROM "10 - Radar"
WHERE type = "trend" AND ring = "ADOPT"
SORT date DESC
```

### TRIAL

```dataview
LIST
FROM "10 - Radar"
WHERE type = "trend" AND ring = "TRIAL"
SORT date DESC
```

### ASSESS

```dataview
LIST
FROM "10 - Radar"
WHERE type = "trend" AND ring = "ASSESS"
SORT date DESC
```

### HOLD

```dataview
LIST
FROM "10 - Radar"
WHERE type = "trend" AND ring = "HOLD"
SORT date DESC
```

## Cómo usar

1. Usa la plantilla `[[Trend]]` (en `12 - Templates/`) para cada tecnología.
2. Coloca las notas aquí, en `10 - Radar/`, con su `ring`.
3. El Dashboard muestra el radar vía Dataview.

## Actualización automática

El sistema crea notas `trend` para tecnologías detectadas con estado inicial `ASSESS`; tú decides cuándo promocionarlas a `TRIAL` o `ADOPT`.