# Install dependencies using uv
install:
	uv sync

# Development server with auto-reload
dev:
	uv run flask --debug --app page_analyzer:app run

# Production server locally
PORT ?= 8000
start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

# Build for Render
build:
	./build.sh

# Run on Render
render-start:
	.venv/bin/python -m gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

# === Code Quality Commands ===
# Lint code
lint:
	uv run ruff check .

# Auto-fix lint errors
lint-fix:
	uv run ruff check --fix .

# Format code
format:
	uv run ruff format .

# Combined: lint and format
quality:
	uv run ruff check . && uv run ruff format .

# Clean up Python cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
