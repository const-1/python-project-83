# Page Analyzer

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-16-purple.svg)](https://www.postgresql.org/)
[![Ruff](https://img.shields.io/badge/code%20style-ruff-ff69b4.svg)](https://github.com/astral-sh/ruff)
[![Render](https://img.shields.io/badge/deployed%20on-render-46a2f1.svg)](https://render.com)

### Hexlet tests and linter status:

[![Actions Status](https://github.com/const-1/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/const-1/python-project-83/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=const-1_python-project-83&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=const-1_python-project-83)

A professional web application for website monitoring and SEO analysis. Page Analyzer allows you to check website availability, extract SEO metadata, and track website status changes over time.

## Features

- Website Monitoring: Track multiple websites with regular checks
- SEO Analysis: Extract h1, title, and description metadata
- Status Tracking: Monitor HTTP response codes and website availability
- URL Validation: Robust URL validation and normalization
- Responsive Design: Mobile-friendly interface using Bootstrap 5

## Quick Start

### Prerequisites

- Python 3.12+
- PostgreSQL 14+
- uv (recommended) or pip

### Installation

- 1.Clone and setup:
- git clone https://github.com/const-1/python-project-83.git
- cd python-project-83
- make install

- 2.Configure environment:
- cp .env.example .env

- 3.Setup database:
- createdb page_analyzer
- psql -d page_analyzer -f database.sql

- 4.Run the application:
- make dev

- 5.Open http://localhost:5000 in your browser.

## Usage

- 1.Add a URL - Enter any website URL on the homepage
- 2.Run checks - Click "Check" to analyze the website
- 3.View results - See HTTP status, SEO metadata, and check history
- 4.Monitor changes - Track website status over time

## Project Commands

- make install      # Install dependencies
- make dev          # Run development server
- make start        # Run production server
- make lint         # Check code quality
- make format       # Format code
- make quality      # Lint and format code
- make clean        # Clean temporary files

## Deployment

### Render (Recommended)

- 1.Connect GitHub repository to Render
- 2.Set Build Command: ./build.sh
- 3.Set Start Command: make render-start
- 4.Add PostgreSQL database
- 5.Configure environment variables

### Environment Variables

- .env
- DATABASE_URL=postgresql://user:password@localhost:5432/page_analyzer
- SECRET_KEY=<your-secret-key-here>

## Technology Stack

- Backend: Python 3.12, Flask 3.0, PostgreSQL
- Frontend: HTML5, Jinja2, Bootstrap 5
- Tools: Ruff (linting), BeautifulSoup4 (HTML parsing), Requests (HTTP)
- Infrastructure: Render (hosting), GitHub Actions (CI/CD)

## Code Quality
- This project uses modern Python development practices:
- Ruff for linting and formatting
- GitHub Actions for continuous integration
- PostgreSQL for data persistence
- Environment variables for configuration

## Project Structure

- .
- ├── page_analyzer/             # Main application package
- │   ├── __init__.py            # Package initialization
- │   ├── app.py                 # Flask application and routes
- │   ├── database.py            # PostgreSQL database connection
- │   ├── models.py              # Data models and SQL queries
- │   ├── urls.py                # URL validation logic
- │   ├── static/                # Static assets
- │   │   └── css/               # CSS stylesheets
- │   └── templates/             # HTML templates
- │       ├── base.html          # Base template with layout
- │       ├── index.html         # Homepage with URL input form
- │       ├── urls.html          # List of all monitored URLs
- │       └── url_detail.html    # URL details and check history
- ├── .github/workflows/         # GitHub Actions workflows
- │   ├── lint.yml               # Code quality checks
- │   └── test.yml               # Test automation
- ├── database.sql               # Database schema and setup
- ├── pyproject.toml             # Python dependencies and configuration
- ├── ruff.toml                  # Ruff linter and formatter configuration
- ├── Makefile                   # Project commands and automation
- ├── build.sh                   # Build script for deployment
- ├── uv.lock                    # Dependency version locking
- └── README.md                  # Project documentation

- .github/workflows/  # CI/CD pipelines
- ├── lint.yml        # Code quality checks
- └── test.yml        # Test automation

## License

- This project is part of the Hexlet curriculum.
