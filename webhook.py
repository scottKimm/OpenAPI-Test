from flask import Flask, request
from urllib import parse
import requests
app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():

    print(request.form)
    return {
        "text": "ok"
    }

