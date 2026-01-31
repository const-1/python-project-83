from page_analyzer.database import get_connection


def add_url(name):
    """Add new URL to database"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO urls (name) VALUES (%s) RETURNING id",
        (name,)
    )
    url_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return url_id


def get_all_urls():
    """Get all URLs with their last check date and status code"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            u.id,
            u.name,
            MAX(uc.created_at) as last_check_date,
            (
                SELECT uc2.status_code
                FROM url_checks uc2
                WHERE uc2.url_id = u.id
                ORDER BY uc2.created_at DESC
                LIMIT 1
            ) as last_check_status_code
        FROM urls u
        LEFT JOIN url_checks uc ON u.id = uc.url_id
        GROUP BY u.id
        ORDER BY u.created_at DESC
    """)
    urls = cur.fetchall()
    cur.close()
    conn.close()
    return urls


def find_url_by_name(name):
    """Find URL by name"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM urls WHERE name = %s", (name,))
    url = cur.fetchone()
    cur.close()
    conn.close()
    return url


def get_url_by_id(id):
    """Get URL by id"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM urls WHERE id = %s", (id,))
    url = cur.fetchone()
    cur.close()
    conn.close()
    return url

def add_url_check(url_id, status_code=None, h1=None, title=None, description=None):
    """Add URL check to database with SEO data"""
    conn = get_connection()
    cur = conn.cursor()

    if status_code is not None:
        cur.execute(
            "INSERT INTO url_checks (url_id, status_code, h1, title, description) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (url_id, status_code, h1, title, description)
        )
    else:
        # This case probably won't be used now, but keep for compatibility
        cur.execute(
            "INSERT INTO url_checks (url_id) VALUES (%s) RETURNING id",
            (url_id,)
        )

    check_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return check_id


def get_url_checks(url_id):
    """Get all checks for specific URL"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM url_checks
        WHERE url_id = %s
        ORDER BY created_at DESC
    """, (url_id,))
    checks = cur.fetchall()
    cur.close()
    conn.close()
    return checks
