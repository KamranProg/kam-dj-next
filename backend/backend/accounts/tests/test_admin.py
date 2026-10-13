import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestAdminUserManagement:
    """Tests for the Django admin user management interface."""

    def setup_method(self) -> None:
        """Set up the test client and create a superuser and a regular user."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="adminpass",
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="userpass",
            username="user@example.com",
        )

    def test_users_list(self) -> None:
        """Displays all users on the Django admin changelist."""
        url = reverse("admin:accounts_user_changelist")
        res = self.client.get(url)
        status_code = 200
        assert res.status_code == status_code
        assert self.user.email in res.content.decode()

    def test_edit_user_page(self) -> None:
        """Renders the Django admin edit form for a user."""
        url = reverse("admin:accounts_user_change", args=[self.user.id])
        res = self.client.get(url)
        status_code = 200
        assert res.status_code == status_code
