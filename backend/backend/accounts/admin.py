from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):  # type: ignore[type-arg]
    """Admin configuration for the custom User model."""

    ordering = ["email"]  # noqa: RUF012

    list_display = ["email", "username", "is_staff", "is_active"]  # noqa: RUF012
    search_fields = ["email", "username"]  # noqa: RUF012

    # Django expects these as instance attributes
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
