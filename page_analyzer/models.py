# page_analyzer/models.py

from datetime import datetime
from urllib.parse import urlparse
from page_analyzer.database import get_connection


def normalize_url(url):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"


def create_url(url):
    normalized_url = normalize_url(url)
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO urls (name, created_at) VALUES (%s, %s) RETURNING id",
            (normalized_url, datetime.now())
        )
        result = cursor.fetchone()
        conn.commit()
        return result[0] if result else None
    except psycopg2.IntegrityError:
        conn.rollback()
        cursor.execute("SELECT id FROM urls WHERE name = %s", (normalized_url,))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        cursor.close()
        conn.close()


def find_url_by_name(url):
    normalized_url = normalize_url(url)
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM urls WHERE name = %s", (normalized_url,))
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()
        conn.close()


def find_url_by_id(url_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM urls WHERE id = %s", (url_id,))
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()
        conn.close()


def get_all_urls():
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, name, created_at FROM urls ORDER BY created_at DESC")
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()
        conn.close()

