from flask import Flask, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
import json
import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(os.getenv("DATABASE_URL"))
with conn.cursor() as cur:
    cur.execute("SELECT * FROM Food")
    res = cur.fetchall()
    conn.commit()
    print(res)

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

# oauth config
oauth = OAuth(app)
# TODO: make the client ID and the secret env variables
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    jwks_uri='https://www.googleapis.com/oauth2/v3/certs',
    client_kwargs={'scope': 'openid email profile'},
)



@app.route('/')
def home():
    if 'profile' in session:
        name = dict(session)['profile']['given_name']
        return f'hello, {name}'
    else:
        return 'please, login'
    
@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    # Get information about the authenticated user
    resp = google.get('userinfo')
    # raise an exception if the response from the server is not successful 
    resp.raise_for_status()
    userinfo = resp.json()
    # do something with the token and profile
    print(json.dumps(userinfo, indent=4))
    session['profile'] = userinfo

    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)