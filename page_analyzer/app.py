# page_analyzer/app.py

import os
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import page_analyzer.models as models
from page_analyzer.urls import validate_url

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/urls', methods=['GET'])
def urls():
    all_urls = models.get_all_urls()
    return render_template('urls.html', urls=all_urls)


@app.route('/urls/<int:id>')
def url_detail(id):
    url = models.find_url_by_id(id)
    if not url:
        flash('Page not found', 'danger')
        return redirect(url_for('urls'))
    
    return render_template('url_detail.html', 
                         url_id=url[0], 
                         url_name=url[1], 
                         created_at=url[2])


@app.route('/urls', methods=['POST'])
def add_url():
    url = request.form.get('url', '').strip()
    
    errors = validate_url(url)
    if errors:
        for error in errors:
            flash(error, 'danger')
        return render_template('index.html', url=url), 422
    
    existing_url = models.find_url_by_name(url)
    if existing_url:
        flash('Page already exists', 'info')
        return redirect(url_for('url_detail', id=existing_url[0]))
    
    new_url_id = models.create_url(url)
    if new_url_id:
        flash('Page successfully added', 'success')
        return redirect(url_for('url_detail', id=new_url_id))
    else:
        flash('Error occurred while adding', 'danger')
        return render_template('index.html', url=url), 500

