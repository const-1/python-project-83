#!/usr/bin/env python3
"""Initialize database tables for Page Analyzer"""

import os
import sys

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from page_analyzer.database import get_connection


def init_database():
    """Initialize database tables from database.sql"""
    try:
        print("Initializing database...")
        
        conn = get_connection()
        cur = conn.cursor()
        
        # Read SQL file
        with open('database.sql', 'r') as f:
            sql_commands = f.read()
        
        # Execute SQL commands
        cur.execute(sql_commands)
        conn.commit()
        
        cur.close()
        conn.close()
        
        print("Database initialized successfully!")
        return True
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        print("This might be normal if tables already exist.")
        return False


if __name__ == "__main__":
    success = init_database()
    sys.exit(0 if success else 1)

