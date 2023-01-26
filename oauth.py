from flask import Flask, request, redirect
from urllib import parse
import requests
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

asdfasdfsadfasdasfdasdf
@app.route("/auth", methods=['GET'])
def auth_swit():
    auth_url = "https://openapi.swit.io/oauth/authorize"
    params = {
        "scope": "user:read workspace:read channel:read message:write",
        "client_id": "",
        "redirect_uri": "http://localhost:5000/auth/callback",
        "response_type": "code"
    }

    return redirect(f"{auth_url}?{parse.urlencode(params)}")

@app.route("/auth/callback", methods=['GET'])
def auth_callback():

    code = request.args.get("code")
    token_url = "https://openapi.swit.io/oauth/token"
    
    headers_obj = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }

    data_obj = {
        "grant_type": "authorization_code",
        "client_id": "",
        "client_secret": "",
        "redirect_uri": "http://localhost:5000/auth/callback",
        "code": code
    }

    resp = requests.post(token_url,data=data_obj, headers=headers_obj)
    return resp.json()

@app.route("/test")
def test():
    headers = {
        "Authorization": "Bearer token...."
    }
    res = requests.get(url="https://openapi.swit.io/v1/api/user.info", headers=headers)
    return res.json()
