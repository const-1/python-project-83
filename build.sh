#!/bin/sh
set -e
echo "Installing dependencies..."

pip install -e .

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
