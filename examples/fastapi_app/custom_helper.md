# Creating a Helper for a Custom Schema

This example demonstrates a FastAPI dependency that checks membership in a custom schema
(`Teams`) returned by `google-authz`.

Assumptions:
- `GOOGLE_WORKSPACE_EXTRA_SCHEMAS` includes `Teams`.
- The `Teams` schema includes `PrimaryTeam` (single) and `Team` (multi).

```python
from fastapi import Depends, HTTPException
from google_authz_client.client import AsyncGoogleAuthzClient
from google_authz_client.fastapi import effective_auth_payload


def team_member(team_name: str, authz_client: AsyncGoogleAuthzClient):
    async def _team_member(
        auth: dict = Depends(effective_auth_payload(authz_client)),
    ) -> None:
        if not auth:
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        teams_schema = auth.get("custom_schemas", {}).get("Teams", {})
        primary_team = teams_schema.get("PrimaryTeam", {}).get("values", [])
        additional_teams = teams_schema.get("Team", {}).get("values", [])
        
        # Normalize the values to lowercase
        team_name_normalized = team_name.lower()
        team_values = [value.lower() for value in (primary_team + additional_teams)]

        if team_name_normalized not in team_values:
            raise HTTPException(status_code=403, detail="Team not allowed")

    return _team_member
```

Usage:

```python
@router.get("/banking/chase/checks/open")
async def get_chase_bankrec(
    _=Depends(team_member("Operations", authz_client)),
):
    ...
```
