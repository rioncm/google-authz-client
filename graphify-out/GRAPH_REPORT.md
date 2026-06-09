# Graph Report - /Users/rion/VSCode/pminc/google-authz-client  (2026-06-09)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 139 nodes · 271 edges · 20 communities (12 shown, 8 thin omitted)
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 70 edges (avg confidence: 0.52)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_FastAPI Auth Dependencies|FastAPI Auth Dependencies]]
- [[_COMMUNITY_Flask Auth Utilities|Flask Auth Utilities]]
- [[_COMMUNITY_GoogleAuthz Configuration|GoogleAuthz Configuration]]
- [[_COMMUNITY_FastAPI Example App|FastAPI Example App]]
- [[_COMMUNITY_Django Auth Integration|Django Auth Integration]]
- [[_COMMUNITY_HTTP Client and Models|HTTP Client and Models]]
- [[_COMMUNITY_Auth Missing Credentials Error|Auth Missing Credentials Error]]
- [[_COMMUNITY_Auth Permission Exceptions|Auth Permission Exceptions]]
- [[_COMMUNITY_AuthZ Response Models|AuthZ Response Models]]
- [[_COMMUNITY_AuthZ FastAPI Client|AuthZ FastAPI Client]]
- [[_COMMUNITY_Base Client Exceptions|Base Client Exceptions]]
- [[_COMMUNITY_FastAPI Auth Payload Helpers|FastAPI Auth Payload Helpers]]
- [[_COMMUNITY_Async HTTP Client|Async HTTP Client]]
- [[_COMMUNITY_Permission Check Helpers|Permission Check Helpers]]
- [[_COMMUNITY_Django AuthZ Client|Django AuthZ Client]]
- [[_COMMUNITY_Django AuthZ Middleware|Django AuthZ Middleware]]
- [[_COMMUNITY_Flask AuthZ Client|Flask AuthZ Client]]
- [[_COMMUNITY_Flask Current User Middleware|Flask Current User Middleware]]
- [[_COMMUNITY_Async AuthZ Client|Async AuthZ Client]]
- [[_COMMUNITY_AuthZ Settings Class|AuthZ Settings Class]]

## God Nodes (most connected - your core abstractions)
1. `EffectiveAuth` - 25 edges
2. `google-authz-client library` - 22 edges
3. `GoogleAuthzError` - 21 edges
4. `AsyncGoogleAuthzClient` - 19 edges
5. `PermissionCheckResult` - 17 edges
6. `MissingCredentialsError` - 16 edges
7. `GoogleAuthzSettings` - 14 edges
8. `_BaseClient` - 12 edges
9. `Request` - 10 edges
10. `EffectiveAuth` - 10 edges

## Surprising Connections (you probably didn't know these)
- `google-authz-client library` --inherits--> `_BaseClient`  [EXTRACTED]
  README.md → src/google_authz_client/client.py
- `Synchronous, long-lived httpx client.` --rationale_for--> `google-authz-client library`  [EXTRACTED]
  src/google_authz_client/client.py → README.md
- `effective_auth_payload from google_authz_client.fastapi` --semantically_similar_to--> `FastAPI effective_auth_payload dependency`  [INFERRED] [semantically similar]
  README.md → CHANGELOG.md
- `FastAPI` --uses--> `AsyncGoogleAuthzClient`  [INFERRED]
  tests/test_fastapi_dependencies.py → src/google_authz_client/client.py
- `test_settings_builds_client_with_token_type()` --calls--> `GoogleAuthzSettings`  [EXTRACTED]
  tests/test_config.py → src/google_authz_client/config.py

## Import Cycles
- 1-file cycle: `src/google_authz_client/flask.py -> src/google_authz_client/flask.py`
- 2-file cycle: `src/google_authz_client/fastapi.py -> tests/test_fastapi_dependencies.py -> src/google_authz_client/fastapi.py`

## Communities (20 total, 8 thin omitted)

### Community 0 - "FastAPI Auth Dependencies"
Cohesion: 0.25
Nodes (15): AsyncGoogleAuthzClient, all_of(), any_of(), current_user(), effective_auth_payload(), _get_cache(), FastAPI dependency helpers for google-authz., Dependency that allows the request if any permission passes. (+7 more)

### Community 1 - "Flask Auth Utilities"
Cohesion: 0.18
Nodes (11): Flask, _get_cache(), Flask utilities for enforcing google-authz permissions., Attach `g.current_user` with EffectiveAuth when a token exists., Decorator enforcing a permission on a Flask view., register_current_user_middleware(), require_permission(), EffectiveAuth (+3 more)

### Community 2 - "GoogleAuthz Configuration"
Cohesion: 0.16
Nodes (7): BaseModel, _env_key(), GoogleAuthzSettings, Settings helpers for configuring the google-authz client., Typed configuration object that can source values from env vars., test_settings_builds_client_with_token_type(), test_settings_builds_login_app_url()

### Community 3 - "FastAPI Example App"
Cohesion: 0.21
Nodes (7): FastAPI, Example FastAPI app using google-authz-client for authorization.  This file demo, _build_mock_async_client(), create_test_app(), test_fastapi_dependency_allows_authorized_call(), test_fastapi_dependency_blocks_invalid_permission(), test_fastapi_dependency_requires_token()

### Community 4 - "Django Auth Integration"
Cohesion: 0.19
Nodes (9): Synchronous, long-lived httpx client., GoogleAuthzMiddleware, _import_django(), Django integration helpers., Attach EffectiveAuth information onto incoming Django requests., Decorator enforcing permissions for Django view functions., require_permission(), google-authz-client library (+1 more)

### Community 5 - "HTTP Client and Models"
Cohesion: 0.18
Nodes (3): HTTP clients for communicating with the google-authz service., google-authz client helpers for Python frameworks., Data models shared across clients and framework integrations.

### Community 6 - "Auth Missing Credentials Error"
Cohesion: 0.31
Nodes (6): Any, EffectiveAuthCache, MissingCredentialsError, Raised when the inbound request does not include a recognizable token., PermissionCheckResult, EffectiveAuth

### Community 7 - "Auth Permission Exceptions"
Cohesion: 0.25
Nodes (6): PermissionDeniedError, Custom exceptions used throughout the google-authz client package., Raised when the service rejects a permission check., PermissionCheckResult, Represents the `/authz/check` response., Raise when the action is not permitted.

### Community 8 - "AuthZ Response Models"
Cohesion: 0.33
Nodes (5): AsyncClient, Client, EffectiveAuth, Represents the `/authz` response for a caller., Return the actions granted for the supplied module.

### Community 9 - "AuthZ FastAPI Client"
Cohesion: 0.29
Nodes (7): AuthZ client singleton, current_user FastAPI dependency, require_permission FastAPI dependency, AsyncGoogleAuthzClient class, current_user FastAPI dependency, current_user from google_authz_client.fastapi, require_permission FastAPI dependency

### Community 10 - "Base Client Exceptions"
Cohesion: 0.47
Nodes (5): Exception, _BaseClient, GoogleAuthzError, Base exception for client failures., Response

### Community 11 - "FastAPI Auth Payload Helpers"
Cohesion: 0.67
Nodes (3): FastAPI effective_auth_payload dependency, team_member FastAPI dependency helper, effective_auth_payload from google_authz_client.fastapi

## Knowledge Gaps
- **12 isolated node(s):** `FastAPI effective_auth_payload dependency`, `GoogleAuthzSettings config class`, `AsyncGoogleAuthzClient in google_authz_client.client`, `current_user from google_authz_client.fastapi`, `GoogleAuthzClient class for Flask` (+7 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `google-authz-client library` connect `Django Auth Integration` to `Flask Auth Utilities`, `GoogleAuthz Configuration`, `HTTP Client and Models`, `Auth Missing Credentials Error`, `Auth Permission Exceptions`, `AuthZ Response Models`, `AuthZ FastAPI Client`, `Base Client Exceptions`?**
  _High betweenness centrality (0.263) - this node is a cross-community bridge._
- **Why does `EffectiveAuth` connect `AuthZ Response Models` to `FastAPI Auth Dependencies`, `Flask Auth Utilities`, `Django Auth Integration`, `HTTP Client and Models`, `Auth Missing Credentials Error`, `Auth Permission Exceptions`, `Base Client Exceptions`, `Async HTTP Client`, `Permission Check Helpers`?**
  _High betweenness centrality (0.153) - this node is a cross-community bridge._
- **Why does `GoogleAuthzSettings` connect `GoogleAuthz Configuration` to `HTTP Client and Models`, `Async HTTP Client`, `Django Auth Integration`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Are the 17 inferred relationships involving `EffectiveAuth` (e.g. with `Any` and `AsyncClient`) actually correct?**
  _`EffectiveAuth` has 17 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `google-authz-client library` (e.g. with `Flask` and `GoogleAuthzSettings`) actually correct?**
  _`google-authz-client library` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `GoogleAuthzError` (e.g. with `Any` and `AsyncClient`) actually correct?**
  _`GoogleAuthzError` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `AsyncGoogleAuthzClient` (e.g. with `AsyncGoogleAuthzClient` and `FastAPI`) actually correct?**
  _`AsyncGoogleAuthzClient` has 9 INFERRED edges - model-reasoned connections that need verification._