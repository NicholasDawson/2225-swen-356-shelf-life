from flask import Flask, jsonify, request, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
import json
import os
import psycopg2


from dotenv import load_dotenv

from logics.Food import Food 
from logics import *
from sqlMethods import *

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
@app.route('/Food', methods=['GET'])
def get_all_Food():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Food")
    rows = cur.fetchall()
    foods = []
    for row in rows:
        foods.append(Food(row[0], row[1], row[2], row[3], row[4]))
    return jsonify([my_object.__dict__ for my_object in foods])

@app.route('/food/<string:id>', methods=['GET'])
def get_Food(id):
    fode = getFood(id)
    if fode:
        return jsonify(fode.__dict__)
    return jsonify({'message': 'Food not found'}), 404
    

@app.route('/food', methods=['POST'])
def create_food():
    data = request.json
    name = data.get('name')
    expiration_date = data.get('expiration_date')
    food = addFood(None, None, name, expiration_date)
    return jsonify(food.__dict__)

@app.route('/food/<string:id>', methods=['PUT'])
def update_my_object(id):
    data = request.get_json()
    cur = conn.cursor()
    cur.execute("UPDATE Food SET name = %s, expiration = %s, quantity = %s WHERE id = %s", (data['name'], data['expiration'], data['quantity'], id))
    conn.commit()
    cur.execute("SELECT * FROM my_objects WHERE id = %s", (id,))
    row = cur.fetchone()
    my_object = Food(row[0], row[1], row[2], row[3])
    return jsonify(my_object.__dict__)

@app.route('/food/<string:id>', methods=['DELETE'])
def delete_my_object(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM food WHERE id = %s", (id,))
    conn.commit()
    return '', 204

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

# @app.route('/add/<>')
# def addFood():
#     return

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