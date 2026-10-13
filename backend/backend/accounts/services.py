from .models import User


def create_user(email: str, password: str) -> User:
    """Create a new user with the given details.

    Returns:
        User: The created user instance.

    """
    return User.objects.create_user(email=email, password=password)


# Can be useful when I introduce email verification scenarios
def activate_user(user: User) -> None:
    """Activate a user by setting their is_active field to True."""
    user.is_active = True
    user.save(update_fields=["is_active"])
