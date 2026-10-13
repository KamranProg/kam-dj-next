import pytest
from accounts.models import User
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import override_settings


@pytest.mark.django_db
class TestSeedDemo:
    """Test cases for the seed_demo management command."""

    @override_settings(DEBUG=True)
    def test_creates_demo_user(self) -> None:
        """Creates a demo user that can sign in."""
        call_command("seed_demo")
        user = User.objects.get(email="demo@example.com")
        assert user.check_password("DemoPass123!")

    @override_settings(DEBUG=True)
    def test_is_idempotent(self) -> None:
        """Does not fail or duplicate the user when run twice."""
        call_command("seed_demo")
        call_command("seed_demo")
        assert User.objects.filter(email="demo@example.com").count() == 1

    @override_settings(DEBUG=False)
    def test_refuses_outside_debug(self) -> None:
        """Refuses to create a known-password user when DEBUG is off."""
        with pytest.raises(CommandError, match="DEBUG"):
            call_command("seed_demo")
        assert not User.objects.filter(email="demo@example.com").exists()
