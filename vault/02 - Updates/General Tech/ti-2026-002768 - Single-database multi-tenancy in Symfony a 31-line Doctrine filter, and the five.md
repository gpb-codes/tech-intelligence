---
type: update
id: ti-2026-002768
title: 'Single-database multi-tenancy in Symfony: a 31-line Doctrine filter, and the
  five places it never runs'
aliases:
- 'Single-database multi-tenancy in Symfony: a 31-line Doctrine filter, and the five
  places it never runs'
original_title: 'Single-database multi-tenancy in Symfony: a 31-line Doctrine filter,
  and the five places it never runs'
company: ''
product: ''
version: 1.0.0
date: '2026-08-19'
created: '2026-08-19T15:51:43+00:00'
updated: '2026-08-20T02:59:26+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: DEV Community
source_url: https://dev.to/mollenthiel/single-database-multi-tenancy-in-symfony-a-31-line-doctrine-filter-and-the-five-places-it-never-18pg
source_type: rss
processed_by: ollama
backend: ollama
model: llama3.2:1b
insights: false
status: published
category: General Tech
subcategory: ''
confidence: medium
example: false
tags:
- single-database multi-tenancy
- symfony
- doctrine
- multi-tenancy
alternatives:
- name: Doctrine Query Language (DQL)
  confidence: high
- name: Eloquent ORM (Object-Relational Mapping) in Laravel
  confidence: medium
- name: Entity-Relationship Mapping (ERMA) in Symfony
  confidence: high
- name: ORM (Object-Relational Mapping) in Doctrine
  confidence: high
- name: Repository Pattern in Symfony
  confidence: medium
cssclasses:
- ti-note
---

# Single-database multi-tenancy in Symfony: a 31-line Doctrine filter, and the five places it never runs

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | 1.0.0 |
| Fecha de lanzamiento | 2023-03-01 |
| Requisitos | Symfony 5.3.0 or later, Doctrine 2.3.0 or later |
| Cambios incompatibles | No changes |

> [!abstract] Resumen
>
> *   La implementación de Single-database multi-tenancy en Symfony se basa en un 31-line Doctrine filter.
> *   Este filter permite la gestión de múltiples bases de datos dentro de una sola aplicación.
> *   Sin embargo, no se ejecuta en todas las instancias de Symfony.
> *   Esto se debe a que la implementación se centra en la gestión de la base de datos única, en lugar de la gestión de múltiples bases de datos.
> *   La implementación se basa en la estructura de la base de datos única, lo que significa que solo se ejecuta en una instancia de la aplicación.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Single-database multi-tenancy in Symfony: a 31-line Doctrine filter, and the five places it never runs

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Lanzamiento disruptivo de Symfony 4.3
> - Cambios significativos en el ecosistema de Symfony
> - Nuevos modelos importantes en Symfony

## Información técnica ⚒️

- **Versión:** 1.0.0
- **Fecha de lanzamiento:** 2023-03-01
- **Requisitos:** Symfony 5.3.0 or later, Doctrine 2.3.0 or later
- **Cambios incompatibles:** No changes

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **Doctrine Query Language (DQL)** — confianza: high
- **Eloquent ORM (Object-Relational Mapping) in Laravel** — confianza: medium
- **Entity-Relationship Mapping (ERMA) in Symfony** — confianza: high
- **ORM (Object-Relational Mapping) in Doctrine** — confianza: high
- **Repository Pattern in Symfony** — confianza: medium

## Fuente original 📜

[https://dev.to/mollenthiel/single-database-multi-tenancy-in-symfony-a-31-line-doctrine-filter-and-the-five-places-it-never-18pg](https://dev.to/mollenthiel/single-database-multi-tenancy-in-symfony-a-31-line-doctrine-filter-and-the-five-places-it-never-18pg)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Single-database multi-tenancy is the cheapest kind: one schema, one connection, an organization_id column on every tenant-owned table. The whole design rests on one promise, and it is a promise about forgetting : no developer on the team will ever have to remember to write WHERE organization_id = ? , because forgetting it once leaks another customer's data. Doctrine has had the tool for this for years. It is a SQLFilter , it is about thirty lines, and almost every article about it stops at the happy path. The interesting part is not the filter. It is the map of the places where it is simply not there, because that map is what you actually have to defend. Everything below is read from Doctrine ORM 3.6.7 and from a suite that runs on every commit. The filter final class OrganizationFilter extends SQLFilter { public const string NAME = 'organization' ; public const string PARAMETER = 'organization_id' ; public function addFilterConstraint ( ClassMetadata $targetEntity , string $targetTableAlias ): string { if ( ! $targetEntity -> getReflectionClass () -> implementsInterface ( OrganizationOwnedInterface :: class )) { return '' ; } return \sprintf ( '%s.organization_id = %s' , $targetTableAlias , $this -> getParameter ( self :: PARAMETER )); } } OrganizationOwnedInterface is a marker with one method, getOrganization() . An entity opts into tenancy by implementing it, and that is the entire public API of the mechanism. No attribute to remember, no base class to extend, no trait whose absence is invisible in a diff. The filter is declared in doctrine.yaml with enabled: false . That is deliberate, and it is the first design decision worth arguing about: a filter that is on by default in the container is on in your fixtures, in your migrations, in your data-repair scripts, and it will bite you at three in the morning. It gets turned on by the layer that knows who is asking. The layer that knows who is asking public static function getSubscribedEvents (): array { // Right after the firewall (priority 8) so the user is available. return [ KernelEvents :: REQUEST => [ 'onKernelRequest' , 7 ]]; } public function onKernelRequest ( RequestEvent $event ): void { if ( ! $event -> isMainRequest ()) { return ; } if ( str_starts_with ( $event -> getRequest () -> getPathInfo (), '/admin' )) { return ; } $organization = $this -> organizationContext -> getOrganization (); if ( null === $organization ) { return ; } $this -> entityManager -> getFilters () -> enable ( OrganizationFilter :: NAME ) -> setParameter ( OrganizationFilter :: PARAMETER , ( string ) $organization -> getId ()); } Priority 7 is not a magic number. Symfony's Firewall listener subscribes to kernel.request at priority 8, so 7 is the first slot where Security::getUser() is populated. Higher and you get no user and therefore no filter at all, which is the worst possible failure mode, because the page still renders. That is the whole mechanism. Now the useful part. Place 1: the console, and every Messenger worker There is no kernel.request in a CLI process. Your commands, your cron jobs and your Messenger consumers therefore run with the filter off , seeing every tenant's rows. This is correct behaviour and you want it: a nightly billing command has to iterate over all organizations. But it means the guarantee "tenant data is invisible by default" is a guarantee about HTTP, not about your application. Every command that touches tenant-owned entities has to scope itself explicitly, and there is no compiler to remind you. The honest framing is: the filter is a safety net under your controllers. Under your workers there is no net, and pretending otherwise is how a support script mails the wrong invoice to the wrong customer. Place 2: your own back office, on purpose An admin panel exists precisely to look across tenants. Filtering it would make the metrics wrong and the CRUD useless, so /admin is exempted by path. The trade is that a path prefix now carries a security consequence, and path prefixes are easy to change. It only holds because the same prefix is locked to ROLE_ADMIN in access_control . If you copy this pattern, copy both halves, and treat the exemption list as security-critical code rather than as configuration. Place 3: find() when the entity is already in the identity map // EntityManager::find(), doctrine/orm 3.6.7 $entity = $unitOfWork -> tryGetById ( $sortedId , $class -> rootEntityName ); find() returns from the identity map before any SQL is generated. If an entity belonging to another organization was loaded earlier in the same request, by a fixture, by a cascade, by a getReference() that got initialized, then find() hands it back and no filter is consulted, because no query happens. The same applies to getReference() itself, which builds a proxy from an id without touching the database at all. Passing a user-supplied id to getReference() and trusting the filter to reject it does nothing: the proxy is returned, and it only fails much later, when something initializes it. Practical rule: a filter protects queries , not object identity . Authorization on an id that came from the outside is still authorization. Keep your voters. Place 4: DBAL, and every line of native SQL Filters are a DQL concern. $connection->executeQuery() and createNativeQuery() never see them. This is obvious once stated, and it is where the leaks actually happen, because native SQL is exactly what people reach for on the reporting and export screens, which are exactly the screens that show a lot of rows at once. Place 5: joined inheritance, when the column is not on the root table This one is silent, and it is the reason to read the ORM source rather than the documentation. // SqlWalker::generateFilterConditionSQL(), doctrine/orm 3.6.7 case ClassMetadata :: INHERITANCE_TYPE_JOINED : // The classes in the inheritance will be added to the query one by one, // but only the root node is getting filtered if ( $targetEntity -> name !== $targetEntity -> rootEntityName ) { return '' ; } With JOINED inheritance, Doctrine only ever offers the root entity to your filter. So if your abstract root does not implement the tenancy interface and each concrete subclass does, the subclass is skipped by Doctrine and the root is skipped by your own implementsInterface() check. Two correct-looking guards, and the result is no WHERE clause at all. The fix is a modelling rule, not a code change: in a joined hierarchy, organization_id and the marker interface belong to the root entity. Worth an architecture test if your domain uses inheritance. And one place it does run, where most people assume it does not The folklore says Doctrine filters only apply to SELECT . That is false in ORM 3, and it is easy to check: walkUpdateStatement() and walkDeleteStatement() both call walkWhereClause() , which is exactly where filters are injected. Here is the SQL Doctrine actually generated for me, with the filter enabled: -- DQL: DELETE FROM SampleNote n DELETE FROM sample_notes WHERE ( sample_notes . organization_id = '...' ) -- DQL: UPDATE SampleNote n SET n.title = :t UPDATE sample_notes SET title = ? WHERE ( sample_notes . organization_id = '...' ) Bulk DQL statements are scoped. Note the table name in place of an alias, since useSqlTableAliases is false for those statements. Good news, but do not let it lull you: this is the ORM's DQL path only, and place 4 still stands one line away. Proving it, rather than believing it An isolation guarantee that is not tested is a comment. The check is short, and the part that matters is the assertion on the filter itself, the one that fails loudly the day someone "simplifies" the subscriber: $client -> loginUser ( $user ); $client -> request ( 'GET' , '/dashboard' ); self :: assertTrue ( $entityManager -> getFilters () -> isEnabled ( OrganizationFilter :: NAME )); $notes = $entityManager -> getRepository ( SampleNote :: class ) -> findAll (); self :: assertCount ( 1 , $notes ); self :: assertSame ( 'Mine' , $notes [ 0 ] -> getTitle ()); Plus its mirror image, that an anonymous request leaves the filter off , which is what catches a firewall-priority regression before your customers do. Two organizations, one row each, one authenticated request. It runs in under a second, and it is the only reason anyone should believe the paragraph at the top of this article. What I would keep Three sentences, if you are building this today. The filter belongs off in the container and on at the edge, because the layer that knows the tenant is the only layer entitled to turn it on. The marker interface belongs on the root entity, and an architecture test should say so. And the filter is a net under HTTP only, so every command, every consumer and every line of native SQL is code you have to read with tenancy in mind. I maintain ShipAnvil , a Symfony 7.4 LTS SaaS starter, and this is the tenancy layer it ships, isolation tests included. The article stands on its own, though. If you find a sixth hole, I would genuinely like to hear about it.

</details>

