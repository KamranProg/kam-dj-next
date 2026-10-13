import uuid
from typing import ClassVar

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager["User"]):
    """Custom manager for the User model."""

    def create_user(
        self,
        email: str,
        password: str | None = None,
        **extra_fields: object,
    ) -> "User":
        """Create and return a user with the given email and password.

        Args:
        email: The user's email address.
        password: The user's password.
        extra_fields: Additional fields to include when creating the user.

        Raises:
        ValueError: If email is not provided.

        Returns:
        User: The newly created user instance.

        """
        if not email:
            msg = "Email must be provided"
            raise ValueError(msg)
        email = self.normalize_email(email)
        extra_fields.setdefault(
            "username",
            email,
        )  # Auto-fill username as email if not passed
        extra_fields.setdefault("is_active", True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        **extra_fields: object,
    ) -> "User":
        """Create and return a superuser with the given email and password.

        Args:
            email: The user's email address.
            password: The user's password.
            extra_fields: Additional fields to include when creating the superuser.

        Raises:
            ValueError: If is_staff or is_superuser is not set to True.

        Returns:
            User: The newly created superuser instance.

        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            value_error = "Superuser must have is_staff=True."
            raise ValueError(value_error)
        if not extra_fields.get("is_superuser"):
            value_error = "Superuser must have is_superuser=True."
            raise ValueError(value_error)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that uses email as the username field."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True)  # , null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: ClassVar[list[str]] = []

    def __str__(self) -> str:
        """Return the user's email address as string representation.

        Returns:
        str: The user's email.

        """
        return self.email


class UserProfile(models.Model):
    """Model to store additional user profile information."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="uploads/avatars/",
        default="uploads/avatars/default.png",
    )
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        """Return the string representation of the user profile.

        Returns:
            str: A formatted string with the user's email.

        """
        return f"Profile for {self.user.email}"
