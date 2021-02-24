from flask import Flask
from flask import render_template,request, redirect

app = Flask(__name__)

@app.route('/' ,methods=["GET", "POST"])
def index():
    if request.method == 'POST':
     imagen = request.form['imagen']
     print(imagen)
    return render_template("index.html")
