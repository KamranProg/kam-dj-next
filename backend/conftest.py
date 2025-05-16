# backend/conftest.py
def pytest_itemcollected(item):
    """Override test display name with docstring (if present)"""
    doc = item.obj.__doc__
    if doc:
        item._nodeid = f"{item.parent.name}::" + doc.strip()
