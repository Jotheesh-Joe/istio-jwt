from flask import Flask, jsonify, render_template, redirect, request, url_for, session
import requests
from urllib import parse
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app)
app.secret_key = '34ad45ty'


client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
url = os.environ["URL"]
tenant_id = os.environ["TENANT_ID"]
api_url = os.environ["API_URL"]
authorization_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/authorize"
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"

redirect_uri = url + '/callback'

#api_url = os.environ["URL"]


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html", bearer_token=session.get('id_token'), api_url=api_url)


@app.route("/login")
def login():
    # Redirect the user to the Azure AD login page to get an authorization code
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "response_mode": "query",
        "scope": "openid profile email User.Read",  # Add the required scopes
    }
    authorization_url_with_params = f"{authorization_url}?{parse.urlencode(params)}"
    return redirect(authorization_url_with_params)


@app.route("/callback")
def callback():
    # Step 2: Extract the authorization code from the query parameters of the redirected URL.
    authorization_code = request.args.get("code")

    token_data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "code": authorization_code,
        "redirect_uri": redirect_uri,
        "client_secret": client_secret,
    }

    token_response = requests.post(token_url, data=token_data)

    # Parse the token response to get the access token and its expiration time
    token_info = token_response.json()
    print(token_info)
    session['id_token'] = "Bearer " + token_info.get("id_token")
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
