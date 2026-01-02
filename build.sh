#!/bin/sh
set -e
echo "Installing dependencies..."

# Установка uv, если не установлен
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

# Установка зависимостей из pyproject.toml
uv sync --quiet
echo "✅ Dependencies installed!"

