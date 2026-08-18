---
type: update
id: ti-2026-002251
title: Docker OIDC connections for GitHub Actions available for Docker Orgs
aliases:
- Docker OIDC connections for GitHub Actions available for Docker Orgs
original_title: Docker OIDC connections for GitHub Actions available for Docker Orgs
company: ''
product: ''
version: '1.0'
date: '2026-07-31'
created: '2026-07-31T16:30:48+00:00'
updated: '2026-08-18T21:50:28+00:00'
original_language: en
translated: true
importance: critical
impact: high
pricing: unknown
license: unknown
open_source: false
self_hosted: false
source: Docker Blog
source_url: https://www.docker.com/blog/docker-oidc-connections-for-github-actions-available-for-docker-orgs/
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
- docker
- github
- actions
- oidc
- ci/cd
alternatives:
- name: GitHub Actions OIDC connections
  confidence: high
- name: OIDC connections para GitHub Actions
  confidence: medium
cssclasses:
- ti-note
---

# Docker OIDC connections for GitHub Actions available for Docker Orgs

<span class="ti-runes">ᚠ ᚢ ᚦ ᚨ ᚱ ᚲ</span>

`critical` · `🚀 Alto`

| Campo | Valor |
| --- | --- |
| Versión | 1.0 |
| Fecha de lanzamiento | 2023-03-09 |
| Cambios incompatibles | No hay cambios incompatibles |

> [!abstract] Resumen
>
> *   Elimina las credenciales almacenadas en tus pipelines de CI/CD para proteger tu información personal.
> *   Utiliza Docker Orgs para gestionar tus contenedores y acceder a tus repositorios de GitHub de manera segura.
> *   Conectas con GitHub Actions para automatizar tareas de CI/CD y eliminar la necesidad de compartir credenciales.
> *   Protege tu información personal al almacenar tus credenciales en un entorno seguro.
> *   Utiliza Docker Orgs para gestionar tus contenedores y acceder a tus repositorios de GitHub de manera segura.

## ¿Qué ocurrió? ⚔️

> [!info] Traducción del anuncio
>
> Docker OIDC connections for GitHub Actions están disponibles para Docker Orgs. Elimina las credenciales almacenadas en tus pipelines de CI/CD.

## ¿Por qué importa? 🛡️

> [!success] Impacto
>
> - Lanza cambios disruptivos al ecosistema de Docker Orgs
> - Cambia lanzamientos importantes de Docker
> - Cambia cambios significativos de precio de Docker

## 📜 Informe para desarrolladores

> [!info] ¿Qué es?
>
> Docker OIDC connections para GitHub Actions son una herramienta que permite conectarse a GitHub Actions con OIDC (OpenID Connect) para autenticación y autorización de usuarios en entornos de Docker Orgs.

> [!tip] ¿En qué ayuda al desarrollo?
>
> Docker OIDC connections permiten a los desarrolladores de Docker Orgs automatizar la autenticación y autorización de usuarios en sus pipelines de CI/CD, lo que mejora la seguridad y la eficiencia de sus procesos.

### Relevancia por perfil ⚔️

| Perfil | Relevancia | Debes saber / actualizarte |
| --- | --- | --- |
| Ingeniero de Software | Alta | Docker OIDC connections permiten automatizar la autenticación y autorización de usuarios en GitHub Actions. · Docker Orgs permiten a los desarrolladores automatizar la autenticación y autorización de usuarios en sus pipelines de CI/CD. |
| DevOps / SRE | Baja | Docker OIDC connections permiten automatizar la autenticación y autorización de usuarios en GitHub Actions. · Docker Orgs permiten a los desarrolladores automatizar la autenticación y autorización de usuarios en sus pipelines de CI/CD. |
| Ciberseguridad | Alta | Docker OIDC connections permiten automatizar la autenticación y autorización de usuarios en GitHub Actions. · Docker Orgs permiten a los desarrolladores automatizar la autenticación y autorización de usuarios en sus pipelines de CI/CD. |
| Semi-Senior | Baja | Docker OIDC connections permiten automatizar la autenticación y autorización de usuarios en GitHub Actions. · Docker Orgs permiten a los desarrolladores automatizar la autenticación y autorización de usuarios en sus pipelines de CI/CD. |
| Junior | Alta | Docker OIDC connections permiten automatizar la autenticación y autorización de usuarios en GitHub Actions. · Docker Orgs permiten a los desarrolladores automatizar la autenticación y autorización de usuarios en sus pipelines de CI/CD. |
| Trainee | Alta | Docker OIDC connections permiten automatizar la autenticación y autorización de usuarios en GitHub Actions. · Docker Orgs permiten a los desarrolladores automatizar la autenticación y autorización de usuarios en sus pipelines de CI/CD. |


## Información técnica ⚒️

- **Versión:** 1.0
- **Fecha de lanzamiento:** 2023-03-09
- **Cambios incompatibles:** No hay cambios incompatibles

## Precio 🪙

> [!money] unknown
>
> $20/mes

## Alternativas 🔄

- **GitHub Actions OIDC connections** — confianza: high
- **OIDC connections para GitHub Actions** — confianza: medium

## Fuente original 📜

[https://www.docker.com/blog/docker-oidc-connections-for-github-actions-available-for-docker-orgs/](https://www.docker.com/blog/docker-oidc-connections-for-github-actions-available-for-docker-orgs/)

## Contenido original 📚

<details>
<summary>Ver contenido original (no traducido)</summary>

Eliminate Stored Credentials in Your CI/CD Pipelines TL;DR: Docker now supports OpenID Connect (OIDC) for GitHub Actions. Your workflows can authenticate with short-lived, per-run tokens instead of stored PATs or OATs. No secrets to rotate, no credentials to leak. GitHub OIDC connections are available to organizations with Docker Team, Docker Business, or Docker Hardened Images (DHI) subscriptions, as well as organizations enrolled in the Docker Sponsored Open Source Program (DSOS) . Table of contents The problem with stored credentials Who should use this How OIDC connections work Getting started What doesn’t change Learn more OIDC token exchange flow between GitHub Actions and Docker The problem with stored credentials Every GitHub Actions workflow that pushes or pulls images from Docker Hub authenticates with a personal access token (PAT) or organization access token (OAT) stored as a GitHub secret. These credentials are long-lived. Someone has to remember to rotate them. A leaked token grants access to your registry — pulling private images, pushing malicious ones — and that access persists until someone discovers and revokes it. Rotation is manual and does not scale. As pipelines multiply, so do the credentials that need tracking, and stale tokens are a common audit finding. Who should use this GitHub issues a signed identity token (a JWT) that encodes the repository, branch, environment, and other metadata about the workflow run. The workflow calls docker/ login -action , which presents this token to Docker. Docker verifies the token’s signature against GitHub’s public key registry and checks it against rulesets configured in the Admin Console. If the token matches a ruleset, Docker returns a short-lived access token scoped to the resources defined in that ruleset. docker/login-action uses this token to authenticate to Docker Hub. From there, docker pull, docker push, and docker build commands work as usual. The entire exchange happens without any stored secrets, API keys, or access tokens. The short-lived Docker access token expires in minutes and cannot be reused. This is the same pattern that AWS and GCP already use for cloud resource access ( AWS OIDC for GitHub Actions , GCP Workload Identity Federation ). Docker is applying it to container registry access. Getting started Setup is a one-time connection in Docker Home plus a small update to your workflow YAML. Step 1: Create a connection Sign in to Docker Home , select your organization, and navigate to OIDC connections. Select Create OIDC connection and configure the rulesets that control which repositories, branches, and workflows can access which Docker Hub resources. You can create up to five rulesets per connection. When a workflow triggers an OIDC exchange, Docker checks the token against every ruleset defined in your connection. If a ruleset’s conditions are satisfied, Docker grants access based on the parameters set by that ruleset. Rulesets use OIDC subject claims to match incoming tokens. You can pin to specific repos and branches as a recommended security best practice: repo:my-org/my-repo:ref:refs/heads/main — only the main branch of a specific repo repo:my-org/my-repo:ref:refs/heads/release-* — all release branches repo:my-org/my-repo:* – all branches of this repo repo:my-org/* — any repo in the organization (not recommended) Copy the connection ID when you are done. Note: GitHub repositories created after July 15, 2026 use immutable identifiers for default subject claims. For example: repo:octocat@123456/my-repo@456789:ref:refs/heads/main. See the GitHub changelog for more details. Step 2: Update your workflow Update your GitHub Actions workflow. Replace <YOUR_CONNECTION_ID> with the ID from the previous step and <YOUR_ORG_NAME> with your Docker organization name: permissions: contents: read id-token: write steps: - name: Docker login uses: docker/login-action@v4 # v4.5.0+ with: username: <YOUR_ORG_NAME> env: DOCKERHUB_OIDC_CONNECTIONID: <YOUR_CONNECTION_ID> The id-token : write permission lets the workflow request a GitHub OIDC token. The docker/login-action handles the token exchange and Docker login in a single step when DOCKERHUB_OIDC_CONNECTIONID is set. From there, docker pull, docker push , and docker build commands work as usual.details of the incoming claim sub value, which you can use to diagnose why the connection failed. Step 3: Verify the OIDC connection works Run your workflow and confirm it completes successfully. If you encounter an error, the Failures tab of the OIDC connection page will show the details of the incoming claim sub value, which you can use to diagnose why the connection failed. Step 4: Remove the stored credential After verifying your workflow runs successfully with OIDC, remove the old PAT or OAT from your GitHub repository secrets. You no longer need it. Migration Checklist Create a connection Update your workflow Verify the OIDC connection works Remove stored credentials What doesn’t change Existing PATs and OATs keep working. Organizations can migrate workflows to OIDC connections at their own pace. Images, registries, and build workflows are unchanged. OIDC connections only replace the authentication step; everything downstream is the same. Local development and non-GitHub CI still use PATs and OATs. OIDC connections are the recommended replacement for GitHub Actions specifically. Other CI providers will follow based on demand. Learn more Learn more about OpenID Connect Visit Docker Home to get started Read the documentation

</details>

