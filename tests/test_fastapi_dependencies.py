import httpx
import pytest

fastapi = pytest.importorskip("fastapi")
testclient_module = pytest.importorskip("fastapi.testclient")

Depends = fastapi.Depends
FastAPI = fastapi.FastAPI
TestClient = testclient_module.TestClient

from google_authz_client.client import AsyncGoogleAuthzClient
from google_authz_client.fastapi import current_user, require_permission


def _build_mock_async_client():
    def handler(request: httpx.Request) -> httpx.Response:
        token = request.headers.get("Authorization", "")
        token = token.split("Bearer ")[-1] if "Bearer" in token else token
        if request.url.path == "/authz":
            return httpx.Response(
                200,
                json={
                    "subject": token or "anon",
                    "permissions": {"inventory": ["read"]},
                },
            )
        if request.url.path == "/authz/check":
            allowed = token == "good-token"
            payload = {"allowed": allowed, "permitted_actions": ["read"] if allowed else []}
            return httpx.Response(200, json=payload)
        raise AssertionError("Unexpected path")

    transport = httpx.MockTransport(handler)
    return httpx.AsyncClient(transport=transport, base_url="https://authz.local")


def create_test_app() -> FastAPI:
    async_client = _build_mock_async_client()
    authz_client = AsyncGoogleAuthzClient(client=async_client, base_url="https://authz.local")

    app = FastAPI()

    @app.get("/inventory")
    async def read_inventory(
        auth=Depends(current_user(authz_client)),
        _=Depends(require_permission("inventory:read", client=authz_client)),
    ):
        return {"subject": auth.subject}

    return app


def test_fastapi_dependency_allows_authorized_call():
    app = create_test_app()
    client = TestClient(app)
    response = client.get("/inventory", headers={"Authorization": "Bearer good-token"})
    assert response.status_code == 200
    assert response.json()["subject"] == "good-token"


def test_fastapi_dependency_blocks_invalid_permission():
    app = create_test_app()
    client = TestClient(app)
    response = client.get("/inventory", headers={"Authorization": "Bearer bad-token"})
    assert response.status_code == 403


def test_fastapi_dependency_requires_token():
    app = create_test_app()
    client = TestClient(app)
    response = client.get("/inventory")
    assert response.status_code == 401
