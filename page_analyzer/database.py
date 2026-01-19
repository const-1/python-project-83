# database.py

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

def get_connection():
    import psycopg2
    return psycopg2.connect(DATABASE_URL)

