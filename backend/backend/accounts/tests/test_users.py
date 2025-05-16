import pytest
from accounts.models import User


@pytest.mark.django_db
class TestUserModel:
    def test_create_user_with_email_successful(self):
        """Creates a user with email and password successfully"""
        user = User.objects.create_user(email="test@example.com", password="testpass")
        assert user.email == "test@example.com"
        assert user.check_password("testpass")

    def test_new_user_email_normalized(self):
        """Normalizes the email of new users"""
        user = User.objects.create_user(email="USER@EXAMPLE.COM", password="pass")
        assert user.email == "USER@example.com"

    def test_new_user_without_email_raises_error(self):
        """Raises ValueError when creating user without email"""
        with pytest.raises(ValueError):
            User.objects.create_user(email=None, password="pass")

    def test_create_superuser(self):
        """Creates a superuser with correct flags"""
        user = User.objects.create_superuser(email="admin@example.com", password="adminpass")
        assert user.is_superuser
        assert user.is_staff
