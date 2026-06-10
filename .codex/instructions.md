# Project Instructions

## Primary Guidance
- Follow the programming [style guide](style_guide.md)

## Project Specific 

Use this repo as the client-library side of the shared AuthZ system. Verify server-facing assumptions against `../google-authz` when endpoint behavior, payload shape, or auth semantics matter.

## Working Style

- Keep changes backwards-compatible for existing API callers unless the user explicitly asks for a breaking change.
- Preserve the distinction between `id_token`, `session_token`, and `access_token`.
- Prefer framework-native helpers over ad hoc auth code inside examples.
- When changing core client behavior, update or add tests for sync and async paths where both are affected.
- When changing docs/examples, keep browser login and access-token API examples separate.

## Client-Specific Guardrails

- Do not hard-code browser cookies as the only credential source; header bearer tokens remain important.
- Do not make Apps Script/access-token users go through `/login/app`.
- Do not require consumers to decode the session cookie locally. The server owns session validation and RBAC lookup.
- Keep `_effective_auth_from_payload()` tolerant of both nested and older top-level response payloads unless a versioned breaking change is planned.
- Keep `GoogleAuthzSettings` env names under the `GOOGLE_AUTHZ_` prefix.
- Keep `login_app_url()` URL-encoding both `app` and `redirect_uri`.
- Permission helpers should continue calling `/authz/check` for enforcement rather than trusting only locally cached permissions.

## Common Files

- `src/google_authz_client/client.py`: sync/async HTTP clients and response normalization.
- `src/google_authz_client/config.py`: settings, env loading, client builders, login URL helper.
- `src/google_authz_client/token.py`: bearer/cookie token discovery.
- `src/google_authz_client/fastapi.py`: FastAPI dependencies for current user and permissions.
- `src/google_authz_client/flask.py`: Flask middleware/decorators.
- `src/google_authz_client/django.py`: Django middleware/decorators.
- `src/google_authz_client/models.py`: `EffectiveAuth` and permission check models.
- `tests/`: regression coverage for client/config/framework behavior.

## Verification

- Preferred full verification: `pytest`.
- If dependencies are missing, install dev extras with `pip install -e .[fastapi,flask,django,dev]` when appropriate.
- For token-type changes, cover `id_token`, `session_token`, and `access_token`.
- For browser-login helper changes, cover `GoogleAuthzSettings.login_app_url()`.
- For framework helper changes, cover missing credentials, allowed permission, and denied permission cases.
- For server contract changes, verify matching behavior in `../google-authz` before finalizing.
