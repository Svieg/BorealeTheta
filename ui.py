from flask import Flask, render_template, request
import pickle, os
import requests
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
  return render_template('main.html')

@app.route('/code', methods=['GET'])
def code():
    if request.method == 'GET':
        return 'gANjYnVpbHRpbnMKc3RyCnEAWBkAAAA8aDI+IHlvdXIgY29kZSBoZXJlIDwvaDI+cQGFcQJScQMu'

@app.route('/rpc', methods=['GET'])
def rpc():
    if request.method == 'GET':
      url = request.args.get('url')
      print(f"[*] URL: {url}")
      response = requests.get(url).content
      print(f"[*] RESPONSE: {response}")
      pickled_code = base64.b64decode(response)
      print(f"[*] PICKLE: {pickled_code}")
      return pickle.loads(pickled_code)
