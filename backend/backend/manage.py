#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line


def main() -> None:
    """Run administrative tasks.

    Raises:
        ImportError: If Django is not installed or the virtual environment
                     is not activated.

    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        msg = (
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
        raise ImportError(msg) from exc


if __name__ == "__main__":
    main()
