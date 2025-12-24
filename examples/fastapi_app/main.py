"""Example FastAPI app using google-authz-client for authorization.

This file demonstrates:
- Creating a shared AsyncGoogleAuthzClient.
- Pulling the current user into a route with dependency injection.
- Enforcing permissions per-route (single permission and any-of).
- Combining multiple dependencies on a single route.
"""

from fastapi import Depends, FastAPI

from google_authz_client.client import AsyncGoogleAuthzClient
from google_authz_client.fastapi import any_of, current_user, require_permission

# Create a single client instance for the app lifecycle.
authz_client = AsyncGoogleAuthzClient()
# Basic FastAPI app setup with a human-readable title.
app = FastAPI(title="google-authz-client example")


@app.get("/inventory")
async def list_inventory(
    # Resolve the current user from the incoming request (e.g., Authorization header).
    auth=Depends(current_user(authz_client)),
    # Enforce that the user has the required permission for this route.
    _=Depends(require_permission("inventory:read", client=authz_client)),
):
    # Return the authenticated subject and their permissions for demo purposes.
    return {"subject": auth.subject, "permissions": auth.permissions}


@app.post("/inventory")
async def create_inventory_item(
    # Only users with "inventory:create" may access this endpoint.
    _=Depends(require_permission("inventory:create", client=authz_client)),
):
    # In a real app, create the inventory item here.
    return {"status": "created"}


@app.delete("/inventory/{item_id}")
async def delete_inventory_item(
    # Path parameter provided by FastAPI routing.
    item_id: str,
    # Allow access if the user has either "inventory:delete" or "inventory:admin".
    _=Depends(any_of(["inventory:delete", "inventory:admin"], client=authz_client)),
):
    # In a real app, delete the item from storage here.
    return {"status": "deleted", "item": item_id}

# Example showing multiple dependencies configured at the decorator level.
@app.get(
    "/bankrec/chase",
    status_code=200,
    dependencies=[
        Depends(current_user(authz_client)),
        Depends(require_permission("inventory:read", client=authz_client)),
    ],
)
async def get_chase_bankrec():
    # This route will only run if both dependencies succeed.
    return {"message": "Chase bank reconciliation data"}
