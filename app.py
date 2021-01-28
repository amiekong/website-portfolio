from flask import Flask, render_template

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    greeting = 'Data Science for the Community'

    return render_template('/index.html',
                            greeting=greeting)
