# google-authz-client

High-level helpers for calling the `google-authz` service from Python APIs.  
Version 0.5 ships framework integrations for FastAPI, Flask, and Django along with a shared HTTP client powered by `httpx`.

## Installation

Pick the source that matches how you ship code. All of the examples show the `fastapi` extra, but feel free to swap in `flask`, `django`, or omit extras entirely.

### From PyPI

```bash
pip install "google-authz-client[fastapi]"
```

This installs the latest published release and is the easiest option for production deployments.

### From Git

```bash
pip install "google-authz-client[fastapi] @ git+https://github.com/example/google-authz-client.git@main"
```

Pin to a tag (for example `@v0.5.0`) when you want a reproducible build while still consuming code directly from Git.

### Local Editable Install

```bash
pip install -e .[fastapi,flask,django,dev]
```

Use this when you are hacking on the library itself so your changes are reloaded without reinstalling. The extra groups are optional – install only what your framework needs.

## Quick Start (FastAPI)

```python
from fastapi import Depends, FastAPI
from google_authz_client.client import AsyncGoogleAuthzClient
from google_authz_client.fastapi import current_user, require_permission

client = AsyncGoogleAuthzClient()
app = FastAPI()

@app.get("/inventory")
async def read_inventory(
    authz=Depends(current_user(client)),
    _=Depends(require_permission("inventory:read", client=client)),
):
    return {"subject": authz.subject, "perms": authz.permissions}
```

`current_user` discovers a token via cookies or the `Authorization` header, fetches the caller’s effective authorization, and raises HTTP 401/403 when missing or denied.

## Flask Example

```python
from flask import Flask
from google_authz_client.client import GoogleAuthzClient
from google_authz_client.flask import register_current_user_middleware, require_permission

app = Flask(__name__)
client = GoogleAuthzClient()
register_current_user_middleware(app, client)

@app.post("/inventory")
@require_permission("inventory:create", client=client)
def create_item():
    return {"subject": flask.g.current_user.subject}
```

## Django Middleware

```python
# settings.py
from google_authz_client.client import GoogleAuthzClient

GOOGLE_AUTHZ_CLIENT = GoogleAuthzClient()
MIDDLEWARE.append("google_authz_client.django.GoogleAuthzMiddleware")
```

## Configuration

Use `GoogleAuthzSettings` to load sensible defaults from environment variables:

```python
from google_authz_client.config import GoogleAuthzSettings

settings = GoogleAuthzSettings()
client = settings.build_async_client()
```

Key settings include `base_url`, `timeout_seconds`, `verify_tls`, and `shared_secret`.

## Development

Run linters and tests with:

```bash
pip install -e .[dev,fastapi,flask,django]
pytest
```

The FastAPI sample app lives under `examples/fastapi_app`.

## Release Process

See [`RELEASING.md`](RELEASING.md) for version-bump instructions, changelog expectations, and details on how the GitHub Actions workflow publishes to PyPI.
