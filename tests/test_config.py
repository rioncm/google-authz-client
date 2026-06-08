from google_authz_client.config import GoogleAuthzSettings


def test_settings_builds_client_with_token_type():
    settings = GoogleAuthzSettings(base_url="https://authz.local", token_type="session_token")

    client = settings.build_client()

    assert client.token_type == "session_token"


def test_settings_builds_async_client_with_token_type():
    settings = GoogleAuthzSettings(base_url="https://authz.local", token_type="access_token")

    client = settings.build_async_client()

    assert client.token_type == "access_token"


def test_settings_builds_login_app_url():
    settings = GoogleAuthzSettings(base_url="https://authz.local/")

    url = settings.login_app_url("helpers", "https://helpers.k8.pminc.me/")

    assert url == (
        "https://authz.local/login/app?"
        "app=helpers&redirect_uri=https%3A%2F%2Fhelpers.k8.pminc.me%2F"
    )
