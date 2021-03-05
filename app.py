from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import os

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    title_text = 'Hi I’m Amie. I enjoy programming, creating, teaching, and giving back.'
    return render_template('index.html',
                                title_text=title_text,
                                title="Data Science for Community",
                                id="index")


@app.route('/about', methods=['POST', 'GET'])
def about():
    title_text = 'I took the Dental Admission Test, received a decent score, and with that I applied to a masters program in Computer Science...'
    return render_template('/about.html',
                            title_text=title_text,
                            title="About Me",
                            id="about")


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    title_text = 'Python (scikit-learn, NumPy, SciPy, Pandas, Keras, Gensim, Plotly), Java, SQL, HTML, CSS, Git, Unix, Flask, Data Extraction, Data Cleaning & Data Visualization'
    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="Project Portfolio",
                            id="portfolio")


@app.route('/orgs', methods=['POST', 'GET'])
def org():
    title_text = 'Promoting Diversity, Inclusion, Community, Leadership'
    return render_template('/orgs.html',
                            title_text=title_text,
                            title="Organizations",
                            id="orgs")
