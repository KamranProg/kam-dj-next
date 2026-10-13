BACKEND_ENV := backend/backend/.env
COMPOSE := docker compose --env-file $(BACKEND_ENV)

.DEFAULT_GOAL := help
.PHONY: help setup deps db migrate seed dev backend frontend test check lint down reset-db

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  %-10s %s\n", $$1, $$2}'

setup: $(BACKEND_ENV) deps ## Create the backend .env and install both apps' dependencies

$(BACKEND_ENV):
	cp backend/backend/.env.example $@
	sed -i.bak "s|^SECRET_KEY=.*|SECRET_KEY=$$(python3 -c 'import secrets; print(secrets.token_urlsafe(50))')|" $@ && rm -f $@.bak
	@echo "Created $@ with a fresh SECRET_KEY"

deps:
	cd backend && uv sync
	cd frontend && pnpm install --frozen-lockfile

db: ## Start PostgreSQL in Docker and wait until it is ready
	$(COMPOSE) up -d --wait db

migrate: ## Apply database migrations
	cd backend && uv run python backend/manage.py migrate

seed: ## Create the demo user (demo@example.com), development only
	cd backend && uv run python backend/manage.py seed_demo

dev: db migrate seed ## Run everything: database, API on :8000, web app on :3000
	$(MAKE) -j2 backend frontend

backend: ## Run only the Django API on :8000
	cd backend && uv run python backend/manage.py runserver

frontend: ## Run only the Next.js app on :3000
	cd frontend && pnpm dev

test: db ## Run the backend tests
	cd backend && uv run pytest backend --ds=config.settings -q

lint: ## Lint and type-check both apps
	cd backend && uv run ruff check backend --no-fix && uv run ruff format backend --check && uv run mypy backend
	cd frontend && pnpm lint && pnpm exec prettier --check . && pnpm type-check

check: lint test ## Everything CI runs, plus the backend tests

down: ## Stop the database container (data is kept)
	$(COMPOSE) down

reset-db: ## Delete the database volume and start a fresh database
	$(COMPOSE) down -v
	$(MAKE) db
