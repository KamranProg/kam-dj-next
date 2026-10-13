from http import HTTPStatus

import pytest
from rest_framework.test import APIClient

from accounts.models import User

PASSWORD = "Str0ngPass!234"  # ruff: ignore[hardcoded-password-string]


@pytest.fixture
def client() -> APIClient:
    """Return an unauthenticated API client."""
    return APIClient()


@pytest.fixture
def user() -> User:
    """Return a persisted user."""
    return User.objects.create_user(email="member@example.com", password=PASSWORD)


@pytest.mark.django_db
class TestAuthApi:
    """Tests for the cookie-session authentication endpoints."""

    def test_register_creates_user_and_session(self, client: APIClient) -> None:
        """Registers a user, starts a session and returns no API token."""
        response = client.post(
            "/api/auth/registration/",
            {"email": "new@example.com", "password1": PASSWORD, "password2": PASSWORD},
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert "sessionid" in response.cookies
        assert User.objects.filter(email="new@example.com").exists()

    def test_register_rejects_mismatched_passwords(self, client: APIClient) -> None:
        """Rejects registration when the two passwords differ."""
        response = client.post(
            "/api/auth/registration/",
            {"email": "new@example.com", "password1": PASSWORD, "password2": "other"},
            format="json",
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_login_sets_session_cookie_without_token(
        self,
        client: APIClient,
        user: User,
    ) -> None:
        """Logs in with a session cookie and returns no API token."""
        response = client.post(
            "/api/auth/login/",
            {"email": user.email, "password": PASSWORD},
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert not response.content
        assert "sessionid" in response.cookies

    def test_login_rejects_wrong_password(self, client: APIClient, user: User) -> None:
        """Rejects a login with the wrong password."""
        response = client.post(
            "/api/auth/login/",
            {"email": user.email, "password": "wrong"},
            format="json",
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert "sessionid" not in response.cookies

    def test_user_endpoint_requires_authentication(self, client: APIClient) -> None:
        """Denies the current-user endpoint to anonymous clients."""
        assert client.get("/api/auth/user/").status_code in {
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
        }

    def test_user_endpoint_returns_current_user(
        self,
        client: APIClient,
        user: User,
    ) -> None:
        """Returns the signed-in user's details."""
        client.force_login(user)
        response = client.get("/api/auth/user/")
        assert response.status_code == HTTPStatus.OK
        assert response.json()["email"] == user.email

    def test_logout_ends_the_session(self, client: APIClient, user: User) -> None:
        """Logs out and denies the user endpoint afterwards."""
        client.force_login(user)
        assert client.post("/api/auth/logout/").status_code == HTTPStatus.OK
        assert client.get("/api/auth/user/").status_code in {
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
        }
