---
type: update
id: ti-2026-002764
title: What Actually Happens When You Call `->save()` in Laravel Eloquent
aliases:
- What Actually Happens When You Call `->save()` in Laravel Eloquent
original_title: What Actually Happens When You Call `->save()` in Laravel Eloquent
company: ''
product: ''
version: ''
date: '2026-08-19'
created: '2026-08-19T16:00:00+00:00'
updated: '2026-08-20T03:14:04+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: DEV Community
source_url: https://dev.to/haseebmirza/what-actually-happens-when-you-call-save-in-laravel-eloquent-444f
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
- name: Ejecutar una consulta SQL directamente en el modelo
  confidence: high
- name: Usar la propiedad $this->exists para decidir qué hacer
  confidence: medium
- name: Usar la propiedad $this->created_at para decidir qué hacer
  confidence: medium
- name: Usar la propiedad $this->updated_at para decidir qué hacer
  confidence: medium
- name: Usar la propiedad $this->exists para decidir qué hacer
  confidence: high
- name: Usar la propiedad $this->created_at para decidir qué hacer
  confidence: medium
cssclasses:
- ti-note
---

# What Actually Happens When You Call `->save()` in Laravel Eloquent

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

> [!abstract] Resumen
>
> *   Cuando llamas a ->save() en Laravel Eloquent, se decide qué hacer con la base de datos.
> *   Si $this->exists es falso, se emite una consulta INSERT.
> *   Si es verdadero, se emite una consulta UPDATE.
> *   La diferencia entre INSERT y UPDATE es que si $this->exists es falso, se emite una consulta INSERT, mientras que si es verdadero, se emite una consulta UPDATE.
> *   La solución para evitar problemas de clonado es resetear manualmente la propiedad $exists.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> ¿Qué sucede cuando llamas a ->save() en Laravel Eloquent
> 
> La mayoría de los desarrolladores de Laravel llaman a ->save() cientos de veces al día. A menudo no saben qué sucede después de esa línea de código. Fui uno de ellos — hasta que heredé un códigobase donde Eloquent estaba comportándose de una manera que no podía explicar. Los modelos no actualizaban. Las eventos no se disparaban. Las fechas eran incorrectas. Tenía que abrir la fuente de Laravel y leerla. Lo que encontré sorprendióme. La Entrada — No es Solo "Guardar en la Base de Datos" Cuando llamas a $model->save(), la mayoría de los desarrolladores suponen que Laravel simplemente emite una consulta SQL. No. La primera cosa que hace ->save() es decidir qué hacer. Si $this->exists es falso, Laravel emite una consulta INSERT. Si es verdadero, Laravel emite una consulta UPDATE. Esto parece simple. Pero tiene consecuencias reales que sorprenden a los desarrolladores. ¿Cómo Sabes INSERT vs UPDATE El $exists property se establece en true al momento de que se obtiene un modelo de la base de datos — independientemente de si se utiliza find(), first(), get() o cualquier otra consulta que haga hydratar un modelo de existencia. Es falso cuando se crea un nuevo modelo manualmente: $user = new User(); // $exists = false → emite una consulta INSERT $user = User::find(1); // $exists = true → emite una consulta UPDATE Dónde esto causa problemas: Cuando se clona un modelo. $original = User::find(1); $copy = clone $original; $copy->email = 'new@example.com'; $copy->save(); // Actualiza el modelo original, no crea un nuevo. El clonado modelo todavía tiene $exists = true y el ID original. Laravel actualiza el ID original, no crea un nuevo. La solución — resetear manualmente: $copy = clone $original; $copy->exists = false; $copy->id = null; $copy->save(); // Emite una consulta INSERT con $exists = false.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Cambios significativos de producto
> - Nuevos modelos importantes
> - Lanzamientos disruptivos

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> Laravel Eloquent permite a los desarrolladores automatizar la creación y actualización de modelos de datos en la base de datos de manera eficiente y segura.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Laravel Eloquent permite a los desarrolladores automatizar la creación y actualización de modelos de datos en la base de datos de manera eficiente y segura, lo que reduce el tiempo y el esfuerzo necesarios para realizar tareas repetitivas.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| DevOps / SRE | Alta | Laravel Eloquent permite automatizar la creación y actualización de modelos de datos en la base de datos de manera eficiente y segura. · Laravel Eloquent permite crear y actualizar modelos de datos de manera rápida y fácil. |
| Ingeniero de Software | Baja | Laravel Eloquent permite automatizar la creación y actualización de modelos de datos en la base de datos de manera eficiente y segura. · Laravel Eloquent permite crear y actualizar modelos de datos de manera rápida y fácil. |
| Ciberseguridad | Alta | Laravel Eloquent permite automatizar la creación y actualización de modelos de datos en la base de datos de manera eficiente y segura. · Laravel Eloquent permite crear y actualizar modelos de datos de manera rápida y fácil. |
| Semi-Senior | Baja | Laravel Eloquent permite automatizar la creación y actualización de modelos de datos en la base de datos de manera eficiente y segura. · Laravel Eloquent permite crear y actualizar modelos de datos de manera rápida y fácil. |
| Trainee | Alta | Laravel Eloquent permite automatizar la creación y actualización de modelos de datos en la base de datos de manera eficiente y segura. · Laravel Eloquent permite crear y actualizar modelos de datos de manera rápida y fácil. |


## Precio 🪙

_No se ha detectado información de precios en la fuente._

## Alternativas 🔄

- **Ejecutar una consulta SQL directamente en el modelo** — confianza: high
- **Usar la propiedad $this->exists para decidir qué hacer** — confianza: medium
- **Usar la propiedad $this->created_at para decidir qué hacer** — confianza: medium
- **Usar la propiedad $this->updated_at para decidir qué hacer** — confianza: medium
- **Usar la propiedad $this->exists para decidir qué hacer** — confianza: high
- **Usar la propiedad $this->created_at para decidir qué hacer** — confianza: medium

## Fuente original 📜

[https://dev.to/haseebmirza/what-actually-happens-when-you-call-save-in-laravel-eloquent-444f](https://dev.to/haseebmirza/what-actually-happens-when-you-call-save-in-laravel-eloquent-444f)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Most Laravel developers call ->save() a hundred times a day. Almost none of them know what happens after that line executes. I was one of them — until I inherited a codebase where Eloquent was behaving in ways I could not explain. Models not updating. Events not firing. Timestamps wrong. I had to open the Laravel source code and actually read it. What I found surprised me. The Entry Point — It Is Not Just "Save to Database" When you call $model->save() , most developers assume Laravel just fires an SQL query. It does not. The first thing save() does is make a decision. It checks one property on your model: $this -> exists This single boolean decides everything. If $exists is false , Laravel runs an INSERT . If it is true , Laravel runs an UPDATE . That sounds simple. But it has real consequences that catch developers off guard. How Laravel Knows INSERT vs UPDATE The $exists property is set to true the moment a model comes from the database — whether you use find() , first() , get() , or any query that hydrates a model from existing records. It is false when you create a new model instance manually: $user = new User (); // $exists = false → will INSERT $user = User :: find ( 1 ); // $exists = true → will UPDATE Where this causes real problems: When you clone a model. $original = User :: find ( 1 ); $copy = clone $original ; $copy -> email = 'new@example.com' ; $copy -> save (); // Updates the ORIGINAL record — not a new one The cloned model still has $exists = true and the original primary key. Laravel will update the original row, not create a new one. The fix — reset it manually: $copy = clone $original ; $copy -> exists = false ; $copy -> id = null ; $copy -> save (); // Now it INSERTs correctly Knowing $exists exists saves you from this bug entirely. Before Anything Touches the Database Before Laravel runs any SQL, it fires model events. This is the order: saving — fires on every save, insert or update creating — fires only on INSERT updating — fires only on UPDATE If any listener on these events returns false , the save is cancelled completely. No query runs. This is how validation inside Observers works — and also why sometimes your save() silently does nothing. An Observer somewhere returned false and you never knew. Always check your Observers when a save mysteriously fails. After events, Laravel does something most developers never think about: Dirty checking. Laravel does not update every column. It only updates columns that actually changed since the model was loaded. This is tracked through $dirty — an array of changed attributes. $user = User :: find ( 1 ); $user -> name = 'Haseeb' ; // marks name as dirty $user -> save (); // only UPDATEs name — not every column This is a performance feature built into Eloquent. But it also means: If you set a value to the same thing it already was — nothing updates. No query runs. This is called a no-op save and it is intentional. The Actual Query Once events pass and dirty attributes are collected, Laravel builds the SQL. For an INSERT it uses performInsert() . For an UPDATE it uses performUpdate() . Both go through setKeysForSaveQuery() — a method that determines which column to use as the identifier for the WHERE clause on updates. By default this is your primary key. But you can override it: protected function setKeysForSaveQuery ( $query ) { $query -> where ( 'custom_column' , $this -> custom_column ); return $query ; } This is useful when you have composite keys or non-standard primary keys — something default Eloquent does not handle well out of the box. Timestamps are handled here too. If your model uses timestamps — which is the default — updated_at is set automatically on every UPDATE. created_at and updated_at are both set on INSERT. You do not touch them. Laravel handles them before the query runs. After the Save Once the query executes, Laravel fires the after-events: saved — fires on every save created — fires after INSERT updated — fires after UPDATE One thing most developers never use — $wasRecentlyCreated : $user -> save (); if ( $user -> wasRecentlyCreated ) { // This was a new record — send welcome email } This flag is set to true only on INSERT in the current request. It resets on the next load from database. Useful when you want to do something only on first creation — without adding extra logic to figure out whether you just inserted or updated. Real World Implications 1. Never call save() inside a loop // Bad — fires one query per iteration foreach ( $users as $user ) { $user -> status = 'active' ; $user -> save (); } // Good — one query for everything User :: whereIn ( 'id' , $userIds ) -> update ([ 'status' => 'active' ]); Every save() inside a loop is a separate database round trip. On 100 records that is 100 queries. Use bulk update() instead. 2. Use save() when you need events. Use update() when you need speed. save() fires all model events and goes through Eloquent's full lifecycle. update() called directly on a query builder skips all of that — no events, no observers, no dirty checking. Both are correct. Choose based on what you actually need. 3. Debugging weird Eloquent behaviour When save() does nothing — check: Is an Observer returning false ? Is the attribute actually dirty or same as before? Is $exists set correctly? These three questions explain 90% of mysterious Eloquent save issues. Why This Matters Beyond Trivia Understanding what happens inside ->save() is not about memorising Laravel internals. It is about understanding the decisions your framework makes on your behalf — so you can work with them instead of against them. The best Laravel developers I have worked with have all done this at least once. Not because they had to. Because they wanted to understand what they were actually building on. You do not need to do this for every method. But doing it for the ones you call every single day — like save() — changes how you debug, how you architect, and how you write code that does not surprise you later. What Is Your ->save() Equivalent? Every framework has methods we call without thinking. What is one Laravel method you use daily but have never fully looked into? Drop it in the comments — I will pick one and write about it next. Haseeb Mirza is a Laravel backend engineer building SaaS platforms, AI-powered applications, and automation systems. Open to senior backend roles and consulting projects. Connect on LinkedIn or find me on Upwork .

</details>

