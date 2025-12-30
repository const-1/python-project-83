import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create a Flask application instance
app = Flask(__name__)

# Get secret key from environment variable (important for security!)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-fallback-key')

# Create first route (handler) for home page
@app.route('/')
def index():
    return 'Hello, World! This is Page Analyzer.'
