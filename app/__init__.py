from flask import Flask
from flask import render_template,request, redirect
import boto3
import uuid
import requests
import botocore

from botocore import UNSIGNED
from botocore.client import Config
from botocore.exceptions import ClientError

app = Flask(__name__)


bucket = 'examenllivichuzhcakevin'
s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
s3._request_signer.sign = (lambda *args, **kwargs: None)

@app.route('/' ,methods=["GET", "POST"])
def index():
    imagen = None
    if request.method == 'POST':
     imagen = request.files['imagen']
     s3.upload_fileobj(imagen,bucket,'img/image1.png', ExtraArgs={'ACL':'public-read'})

    return render_template("index.html",imag = imagen)
