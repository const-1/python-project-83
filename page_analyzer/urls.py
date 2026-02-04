# page_analyzer/urls.py

import validators


def validate_url(url):
    errors = []

    if not url:
        errors.append("URL is required")
    elif len(url) > 255:
        errors.append("URL exceeds 255 characters")
    elif not validators.url(url):
        errors.append("Invalid URL")

    return errors
