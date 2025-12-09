from fastapi import Depends, FastAPI

from google_authz_client.client import AsyncGoogleAuthzClient
from google_authz_client.fastapi import any_of, current_user, require_permission

authz_client = AsyncGoogleAuthzClient()
app = FastAPI(title="google-authz-client example")


@app.get("/inventory")
async def list_inventory(
    auth=Depends(current_user(authz_client)),
    _=Depends(require_permission("inventory:read", client=authz_client)),
):
    return {"subject": auth.subject, "permissions": auth.permissions}


@app.post("/inventory")
async def create_inventory_item(
    _=Depends(require_permission("inventory:create", client=authz_client)),
):
    return {"status": "created"}


@app.delete("/inventory/{item_id}")
async def delete_inventory_item(
    item_id: str,
    _=Depends(any_of(["inventory:delete", "inventory:admin"], client=authz_client)),
):
    return {"status": "deleted", "item": item_id}
