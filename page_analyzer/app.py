import os

import requests
import validators
from bs4 import BeautifulSoup
from flask import Flask, flash, redirect, render_template, request, url_for
from requests.exceptions import RequestException

from page_analyzer import models

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    """Main page"""
    return render_template("index.html")


@app.route("/urls", methods=["GET"])
def urls():
    """Show list of all URLs"""
    return render_template("urls.html", urls=models.get_all_urls())


@app.route("/urls", methods=["POST"])
def add_url():
    """Add new URL"""
    url = request.form.get("url")

    # Validate URL
    if not url or not validators.url(url):
        flash("Некорректный URL", "danger")
        return render_template("index.html", url=url), 422

    # Normalize URL
    normalized_url = models.normalize_url(url)

    # Check if URL already exists
    existing_url = models.find_url_by_name(normalized_url)
    if existing_url:
        flash("Страница уже существует", "info")
        return redirect(url_for("url_detail", id=existing_url[0]))

    # Add URL to database
    url_id = models.add_url(normalized_url)
    flash("Страница успешно добавлена", "success")
    return redirect(url_for("url_detail", id=url_id))


@app.route("/urls/<int:id>")
def url_detail(id):
    """Show URL details and checks"""
    url = models.get_url_by_id(id)
    if not url:
        flash("Сайт не найден", "danger")
        return redirect(url_for("urls"))

    checks = models.get_url_checks(id)
    return render_template("url_detail.html", url=url, checks=checks)


@app.route("/urls/<int:id>/checks", methods=["POST"])
def check_url(id):
    """Perform URL check with real HTTP request and SEO analysis"""
    url_record = models.get_url_by_id(id)
    if not url_record:
        flash("Сайт не найден", "danger")
        return redirect(url_for("urls"))

    site_url = url_record[1]  # URL from database

    try:
        # Make HTTP request with timeout and User-Agent
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(
            site_url, headers=headers, timeout=10, allow_redirects=True
        )
        status_code = response.status_code

        # Initialize SEO data with empty strings
        h1 = ""
        title = ""
        description = ""

        # Parse HTML only for successful responses
        if 200 <= status_code < 400:
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract h1
            h1_tag = soup.find("h1")
            if h1_tag:
                h1 = h1_tag.get_text().strip()[:255]  # Limit to 255 chars for DB

            # Extract title
            title_tag = soup.find("title")
            if title_tag:
                title = title_tag.get_text().strip()[:255]  # Limit to 255 chars

            # Extract description
            meta_desc = soup.find("meta", attrs={"name": "description"})
            if meta_desc and meta_desc.get("content"):
                description = meta_desc["content"].strip()

        # Check if it's a server error (5xx)
        if 500 <= status_code < 600:
            flash("Произошла ошибка при проверке", "danger")
        else:
            # Create check with status code and SEO data
            models.add_url_check(id, status_code, h1, title, description)

            if 200 <= status_code < 300:
                flash("Страница успешно проверена", "success")
            else:
                flash(f"Страница проверена, статус: {status_code}", "info")

    except RequestException:
        # All requests exceptions (connection error, timeout, etc.)
        flash("Произошла ошибка при проверке", "danger")

    return redirect(url_for("url_detail", id=id))
