# google-authz-client Context

This repo is the Python client/integration library for the sibling `../google-authz` service. It provides sync and async HTTP clients plus framework helpers for FastAPI, Flask, and Django.

## Current Shape

- Package source: `src/google_authz_client/`.
- Core sync/async clients: `src/google_authz_client/client.py`.
- Typed settings and env loading: `src/google_authz_client/config.py`.
- Shared response models: `src/google_authz_client/models.py`.
- Token discovery helpers: `src/google_authz_client/token.py`.
- Framework integrations:
  - FastAPI: `src/google_authz_client/fastapi.py`.
  - Flask: `src/google_authz_client/flask.py`.
  - Django: `src/google_authz_client/django.py`.
- Tests: `tests/`.
- Packaging: `pyproject.toml`.
- Examples: `examples/fastapi_app/`.

The Graphify knowledge graph lives in `graphify-out/`. The latest report at `graphify-out/GRAPH_REPORT.md` identifies the main hubs as `EffectiveAuth`, `AsyncGoogleAuthzClient`, `GoogleAuthzSettings`, `_BaseClient`, `PermissionCheckResult`, and framework helper modules. Treat inferred graph edges as search hints, not validated facts.

## Relationship To Server Repo

The sibling `../google-authz` repo owns the HTTP endpoint behavior. This library must stay compatible with server contracts for:

- `/authz`
- `/authz/check`
- `GET /login/app`
- token payload field names
- EffectiveAuth response shape
- permission check response shape

Known server contract: `/authz` and `/authz/check` accept exactly one token field: `id_token`, `session_token`, or `access_token`.

The library currently supports:

- `token_type="id_token"` by default.
- `token_type="session_token"` for browser app sessions.
- `token_type="access_token"` for Apps Script/local API workflows.
- Nested `/authz` response payloads under `effective_auth`.
- Older/top-level permission payloads for backwards compatibility.

Preserve these compatibility points unless a breaking change is intentional, versioned, and documented.

## Auth Flows To Preserve

1. Browser app login:
   - A browser app builds a login URL with `GoogleAuthzSettings.login_app_url(app, redirect_uri)`.
   - The user enters the server through `/login/app`.
   - The server sets a session cookie such as `ga_session`.
   - Consuming FastAPI/Flask/Django apps configure this library with `token_type="session_token"`.
   - Framework helpers discover the cookie and call `/authz` or `/authz/check`.

2. Existing API/access-token flow:
   - Apps Script obtains a Google OAuth access token using `ScriptApp.getOAuthToken()`.
   - The local API receives `Authorization: Bearer <token>`.
   - The local API configures this library with `token_type="access_token"`.
   - This flow does not use `/login/app` or browser cookies.

Do not make browser session behavior replace access-token behavior.

## Important Contracts

- `_BaseClient._token_payload()` must emit exactly one of `id_token`, `session_token`, or `access_token`.
- `_BaseClient._effective_auth_from_payload()` intentionally handles both nested `effective_auth` and older top-level payloads.
- `GoogleAuthzSettings` reads env vars with the `GOOGLE_AUTHZ_` prefix.
- `GoogleAuthzSettings.login_app_url()` builds `/login/app?app=...&redirect_uri=...`.
- FastAPI helpers use `discover_token()` against headers and cookies, then call the async client.
- Permission strings passed to helpers are expected to look like `module:action`.
- `shared_secret` is optional; the main server relies on network ACLs unless a deployment adds an extra enforcement layer.

## Verification Notes

- Install dev extras locally with `pip install -e .[fastapi,flask,django,dev]` when needed.
- Standard test command: `pytest`.
- Focused tests exist for clients, config, FastAPI dependencies, Flask helpers, and token discovery.
- When changing token handling, run or update `tests/test_client.py`, `tests/test_config.py`, and framework helper tests as relevant.
