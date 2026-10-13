import pytest

from accounts.models import User
from accounts.services import activate_user, create_user


@pytest.mark.django_db
class TestUserServices:
    """Tests for the accounts service layer."""

    def test_create_user_persists_user(self) -> None:
        """Creates and saves a user through the service layer."""
        user = create_user(email="service@example.com", password="testpass")
        assert User.objects.filter(pk=user.pk).exists()
        assert user.check_password("testpass")

    def test_activate_user_sets_is_active(self) -> None:
        """Activates an inactive user."""
        user = User.objects.create_user(email="inactive@example.com", password="pass")
        user.is_active = False
        user.save(update_fields=["is_active"])

        activate_user(user)

        user.refresh_from_db()
        assert user.is_active
