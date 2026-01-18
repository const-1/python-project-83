#!/bin/sh
set -e
echo "Installing dependencies..."

if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

source $HOME/.local/bin/env 2>/dev/null || true

uv sync --quiet
echo "Dependencies installed!"

if [ -n "$DATABASE_URL" ]; then
    echo "Applying database migrations..."
    if command -v psql &> /dev/null; then
        psql -a -d "$DATABASE_URL" -f database.sql
        echo "Database migrations applied!"
    else
        echo "PostgreSQL client not found. Skipping database setup."
    fi
else
    echo "DATABASE_URL not set. Skipping database setup."
fi

