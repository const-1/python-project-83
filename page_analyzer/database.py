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

    # Connect with SSL for Render
    return psycopg2.connect(db_url, sslmode="require")
