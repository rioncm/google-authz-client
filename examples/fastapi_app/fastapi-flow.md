# Example Authorization Flows

This document covers two distinct paths:
1. Full OAuth flow handled by `google-authz` (login to session).
2. OAuth already completed elsewhere; `google-authz` validates an ID token and returns authorizations.

Important: the `google-authz` service validates **OpenID ID tokens** (or its own session token),
not OAuth access tokens. The client library simply forwards whatever token is provided in the
`Authorization: Bearer <token>` header (or a `session` cookie). If you pass an access token, the
current service will reject it unless it is extended to verify access tokens.

# Google Sheets Extension (External OAuth Completed)

## Activation
The user activates an extension function which makes a call to the central API at
`https://api.pminc.me` (which can differ from the authz host, e.g. `https://auth.pminc.me`).

1. The code grabs the current user OAuth access token.

``` javascript
function getHeaders() {
   const token = getAuthToken();
   const headers =  {
    method: 'get',
    headers: { Authorization: `Bearer ${token}` },
    muteHttpExceptions: true, 
  };
  return headers;
}
function getAuthToken() {
  return ScriptApp.getOAuthToken(); // OAuth access token.
}

function isUserAuthorized() {
  const token = getAuthToken();
  // Simple check: token exists and is non-empty
  return token && token.length > 0;
}
```

2. Builds and executes the request.
``` javascript
function getApData() {
  const url = BASE_URL + '/ap/aging'; // Replace with your API URL
  const options = getHeaders()
  Logger.log(`url: ${url}`);
  

  try {
    const data = getAPIData(url, options);
    return data;
  } catch (e) {
    Logger.log('Error: %s', e.message);
  }
}
```
3. The API receives the request, forwards the access token to `google-authz`, and validates
   the user + authorizations.

# lib/authz.py
``` python
from google_authz_client.client import AsyncGoogleAuthzClient
from google_authz_client.fastapi import current_user, require_permission

class AuthZ:
    def __init__(self):
        self.authz_client = AsyncGoogleAuthzClient(
            base_url="https://auth.pminc.me",
            verify_tls=True
        )

# The functions below are helpers to allow a singleton pattern for the AuthZ client.
authz_client = AuthZ().authz_client
current_user = current_user
require_permission = require_permission 
```
# /routers_ap_data.py
``` python
#other imports...
from lib.authz import authz_client, current_user, require_permission

@router.get(
    "/banking/rec/chase",
    status_code=200,
    dependencies=[
        Depends(require_permission("bankrec:read", client=authz_client)),
    ],
)
async def get_chase_bankrec(account: str, start_date: str, end_date: str): 
    """
    Returns Chase Bank Reconciliation data from OSAS for use in Google Sheets.
    """

    # Load the base SQL query
    query = ute.get_sql("get_chase_bankrec")
    
    try:
        # Execute the query with parameters
        result = await odb.get_data(query)
        return {"records": result}
    except Exception as e:
        log.error(f"Error fetching Chase bank reconciliation data: {e}")
        return Response(content="Internal Server Error", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
```
4. API endpoint processes and returns an appropriate response.

Success
{records: DATA}

Not Authorized
{401} (missing or invalid token)
{403} (permission denied)

Error
{500}

# Flow 1: Full OAuth Handled by google-authz

This path is for web apps that delegate Google login to the `google-authz` service.
The service completes OAuth, verifies the ID token, and returns its own session token.
Subsequent calls use the session token (cookie or header).

1. Client hits `GET /login` on `google-authz`.
2. User completes Google OAuth consent.
3. `google-authz` exchanges the code and validates the ID token.
4. `google-authz` issues a session cookie (or `session_token`) for future `/authz` calls.
5. Your API uses `google-authz-client` to authorize requests using that session token.

# Flow 2: OAuth Completed Elsewhere (ID Token Validation)

This path is for clients that already have a Google OAuth access token (Apps Script, backend
service, or another OAuth-enabled app). The client sends the access token to your API, and the
API forwards it to `google-authz` for validation and authorization.

1. Client obtains an **access token** externally.
2. Client calls your API with `Authorization: Bearer <access_token>`.
3. Your API uses `google-authz-client` which forwards the token to `/authz` or `/authz/check`.
4. `google-authz` verifies the access token and returns the EffectiveAuth payload.

If you need to support ID tokens instead, configure `google-authz` with the correct audience
and send an OpenID ID token. The client library forwards whatever token it receives.
