---
type: update
id: ti-2026-002279
title: 'React''s Activity Component: Hide UI Without Losing Its State'
aliases:
- 'React''s Activity Component: Hide UI Without Losing Its State'
original_title: 'React''s Activity Component: Hide UI Without Losing Its State'
company: ''
product: ''
version: '1.0'
date: '2026-08-18'
created: '2026-08-18T08:05:29+00:00'
updated: '2026-08-18T21:31:33+00:00'
original_language: en
translated: true
importance: medium
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: DEV Community
source_url: https://dev.to/grimicorn/reacts-activity-component-hide-ui-without-losing-its-state-jem
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
- name: useState
  confidence: high
- name: useReducer
  confidence: medium
- name: useContext
  confidence: medium
- name: useReducer
  confidence: high
- name: useContext
  confidence: medium
cssclasses:
- ti-note
---

# React's Activity Component: Hide UI Without Losing Its State

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`🟡 Media` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | 1.0 |
| Fecha de lanzamiento | 2023-03-01 |
| Requisitos | React 17.0.2, Webpack 5.11.0 |
| Cambios incompatibles | No changes |

> [!abstract] Resumen
>
> * React: Component de actividad oculta el UI sin perder su estado
> * User: Inicia una acción de tipo "componer" y envía una solicitud al servidor
> * Compose tab: Cambia la configuración de la notificación
> * Settings tab: Cambia la configuración de la notificación
> * Draft: Se elimina de la lista de tareas

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> React's Activity Component: Hide UI Without Losing Its State
> 
> A user types half a message into the compose tab, flips over to the settings tab to change a notification preference, flips back, and the draft is gone.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Nuevos modelos importantes
> - Cambio significativo de producto
> - Cambio importante de precio

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> React's Activity Component es un componente de React que permite ocultar la interfaz de usuario (UI) sin perder su estado, lo que permite una experiencia de usuario más eficiente y segura.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Este componente de React permite a los desarrolladores crear aplicaciones más rápidas y fáciles de usar, ya que permite ocultar la UI y mantener su estado, lo que reduce la cantidad de código necesario y mejora la experiencia del usuario.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Trainee | Alta | Ocultar la UI sin perder su estado · Mantenimiento de la interfaz de usuario · Optimización de la experiencia del usuario |
| Junior | Baja | Ocultar la UI sin perder su estado · Mantenimiento de la interfaz de usuario · Optimización de la experiencia del usuario |
| Semi-Senior | Baja | Ocultar la UI sin perder su estado · Mantenimiento de la interfaz de usuario · Optimización de la experiencia del usuario |
| Senior | Alta | Ocultar la UI sin perder su estado · Mantenimiento de la interfaz de usuario · Optimización de la experiencia del usuario |
| Ingeniero de Software | Alta | Ocultar la UI sin perder su estado · Mantenimiento de la interfaz de usuario · Optimización de la experiencia del usuario |
| Ingeniero en Redes | Alta | Ocultar la UI sin perder su estado · Mantenimiento de la interfaz de usuario · Optimización de la experiencia del usuario |
| DevOps / SRE | Alta | Ocultar la UI sin perder su estado · Mantenimiento de la interfaz de usuario · Optimización de la experiencia del usuario |
| Ciberseguridad | Alta | Ocultar la UI sin perder su estado · Mantenimiento de la interfaz de usuario · Optimización de la experiencia del usuario |


## Información técnica ⚒️

- **Versión:** 1.0
- **Fecha de lanzamiento:** 2023-03-01
- **Requisitos:** React 17.0.2, Webpack 5.11.0
- **Cambios incompatibles:** No changes

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **useState** — confianza: high
- **useReducer** — confianza: medium
- **useContext** — confianza: medium
- **useReducer** — confianza: high
- **useContext** — confianza: medium

## Fuente original 📜

[https://dev.to/grimicorn/reacts-activity-component-hide-ui-without-losing-its-state-jem](https://dev.to/grimicorn/reacts-activity-component-hide-ui-without-losing-its-state-jem)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

A user types half a message into the compose tab, flips over to the settings tab to change a notification preference, flips back, and the draft is gone. You know exactly why: {tab === 'compose' && <Compose />} unmounted the subtree, and unmounting throws away state. The usual fixes are all a little sad. Lift the state up and thread it back down through props. Park it in a store that exists only to survive an unmount. Or render everything at once behind a display: none class and eat the mount cost of every panel on first paint. React 19.2 added a first-class answer instead: <Activity> . Two modes and a boundary Activity is a component you import from react directly. It takes a mode prop that is either visible or hidden , and it wraps the subtree you want to keep alive. import { Activity } from " react " ; function Workspace ({ tab }) { return ( <> < Activity mode = { tab === " compose " ? " visible " : " hidden " } > < Compose /> </ Activity > < Activity mode = { tab === " settings " ? " visible " : " hidden " } > < Settings /> </ Activity > </> ); } When a boundary goes hidden, React hides its children with display: none rather than removing them. Every useState and useReducer value in the subtree is preserved, and so is the DOM state that React normally has no opinion about: scroll offsets, uncontrolled input values, the current playback position of a <video> . Flip back to visible and the panel is exactly where the user left it, with no restoration logic on your side. Hidden does not mean paused This is the part that trips people up, so it's worth being blunt about it: hiding an Activity runs your cleanup functions. Every useEffect and useLayoutEffect cleanup in the subtree fires, exactly as if the component had unmounted. Sockets close, intervals clear, observers disconnect. When the boundary becomes visible again, the setup functions run again. That is the behavior you want most of the time. A hidden panel holding an open WebSocket is a resource leak with extra steps. function LivePrices ({ symbol }) { const [ quotes , setQuotes ] = useState ({}); useEffect (() => { const socket = new WebSocket ( `wss://example.com/quotes/ ${ symbol } ` ); socket . onmessage = ( e ) => setQuotes ( JSON . parse ( e . data )); return () => socket . close (); }, [ symbol ]); return < QuoteTable rows = { quotes } />; } Wrapped in a hidden Activity , the socket closes but quotes survives. Come back and the table paints immediately with the last known numbers, then updates as fresh messages arrive. The user sees stale-but-plausible data instead of a spinner. The practical requirement is that your Effects have to tolerate running more than once, which is the same discipline StrictMode's double-invoke has been enforcing in development for years. Pre-rendering what nobody has clicked yet Hidden boundaries are not inert. React still renders them, at the lowest priority it has. That turns Activity into a way to warm up a route before the user asks for it. < Activity mode = { route === " /reports " ? " visible " : " hidden " } > < ReportsPage /> </ Activity > The reports page mounts, its data fetches start, its component tree gets built, all in the gaps between higher-priority work. Navigation then feels instant because most of the work already happened. The catch: lowest priority is the only priority you get. There is no knob for tuning it, and if the hidden subtree is genuinely expensive it still competes for the same main thread as everything visible. Activity reorders work; it does not make it free. React 19.2's DevTools Performance Tracks are the right place to check whether a background boundary is actually paying for itself. The other cost is DOM weight. Hidden children remain in the document, so twenty hidden panels are twenty panels' worth of nodes that the browser still has to keep in memory and account for in style recalculation. Activity is aimed at a handful of heavy, stateful regions, such as tab groups, wizard steps, and a route you're fairly confident is next. It is not a blanket replacement for conditional rendering, and a list of a thousand rows should still unmount. What it retires If you've written a useRef cache to stash a component's scroll position, or added a slice to Zustand whose only job was surviving an unmount, or hand-rolled a hidden class plus a pile of if (!visible) return guards inside your Effects, that's the pattern Activity collapses into one boundary. It shipped stable in React 19.2, so there's no canary flag to opt into. Pick the tab group in your app that annoys you most, wrap each panel, and delete the state-preservation scaffolding you built around it. The official reference covers the remaining edge cases, including how it interacts with Suspense.

</details>

