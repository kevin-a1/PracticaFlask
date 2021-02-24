from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Kevin'

posts = []
@app.route('/inicio')
@app.route('/inicio/<string:slug>/')
def index(slug = 'Usuario'):
    return render_template("index.html", num_posts = slug)
