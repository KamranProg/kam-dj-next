import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestAdminUserManagement:
    def setup_method(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="adminpass"
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="userpass",
            username="user@example.com"
        )

    def test_users_list(self):
        """displays all users on the Django admin changelist"""
        url = reverse("admin:accounts_user_changelist")
        res = self.client.get(url)
        assert res.status_code == 200
        assert self.user.email in res.content.decode()

    def test_edit_user_page(self):
        """renders the Django admin edit form for a user"""
        url = reverse("admin:accounts_user_change", args=[self.user.id])
        res = self.client.get(url)
        assert res.status_code == 200
