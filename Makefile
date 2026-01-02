# Install dependencies using uv (modern alternative to pip)
install:
	uv sync

# Run in development mode with automatic reloading
dev:
	uv run flask --debug --app page_analyzer:app run

# Start production server locally with Gunicorn
PORT ?= 8000
start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

# Command for building on Render.com
build:
	./build.sh

# Command for running on Render.com (dependencies are already installed globally)
render-start:
	.venv/bin/python -m gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app
