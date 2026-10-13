# backend/conftest.py

from typing import Any


def pytest_itemcollected(item: Any) -> None:
    """Override test display name with docstring."""
    doc = getattr(item.obj, "__doc__", None)
    if doc:
        item._nodeid = f"{item.parent.name}::{doc.strip()}"
