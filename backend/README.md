# Backend

Django REST API for authentication and user management. See the
[root README](../README.md) for setup, environment variables and the
overall architecture.

Common tasks (run from this directory, or use `make` from the repository root):

```bash
uv sync                    # install dependencies into .venv
uv run rav run dev         # start the API at http://localhost:8000
uv run rav run check       # ruff + mypy + pytest
```

Interactive API docs are served at `/api/docs/` while the server is running.
