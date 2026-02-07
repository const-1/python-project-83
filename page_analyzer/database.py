import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    """Get database connection"""
    # Fix for Render's PostgreSQL URL format
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        db_url = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    else:
        db_url = DATABASE_URL

    # Configure SSL for the database connection
    # SSL is disabled in CI/CD (test env)
    # SSL is enabled in production (Render)
    # "onrender.com" in DATABASE_URL means we are in production

    if "onrender.com" in (db_url or ""):
        # Production requires SSL
        return psycopg2.connect(db_url, sslmode="require")
    else:
        # Dev/test does not require SSL
        return psycopg2.connect(db_url)
