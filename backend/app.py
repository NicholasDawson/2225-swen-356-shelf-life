from flask import Flask, jsonify, make_response, redirect, request, url_for
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, unset_jwt_cookies
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
import os
import psycopg2


from dotenv import load_dotenv

from models.Food import Food 
from models import *
from sqlMethods import *


app = Flask(__name__)

# Configure JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')  # replace with your own secret key
jwt = JWTManager(app)

# Configure Google OAuth
oauth = OAuth(app)
oauth.init_app(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://www.googleapis.com/oauth2/v3/userinfo',
    jwks_uri='https://www.googleapis.com/oauth2/v3/certs',
    client_kwargs={'scope': 'openid email profile'},
)

# region Authentication Methods
   
# Define an endpoint for logging in with Google OAuth2
@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(
        redirect_uri=redirect_uri, 
        access_type='offline', 
        prompt='consent'
    )


# Define the callback for handling the OAuth2 response
@app.route('/authorize')
def authorize():
    try:
        token = google.authorize_access_token()
        resp = google.get('userinfo')
        resp.raise_for_status()
        userinfo = resp.json()
        email = userinfo["email"]
        name = userinfo["name"]
        google_id = userinfo["id"]

        print(userinfo)

        # ------------ Commenting this section out until DB changes are applied ----------------
        # # Check if the user already exists in the database
        user = getUserByGoogleID(google_id)

        if not user:
            # If the user doesn't exist, create a new user record in the database
            user = User(google_id=google_id, name=name)
            addUser(user)
            print("new user", user)
        # --------------------------------------------------------------------------------------

        # Generate an access token and redirect to the splash page with the token in the query string
        access_token = create_access_token(identity=email)
        # TODO: change the hardcoded url
        redirect_url = f'{os.getenv("FRONTEND_URL")}/splash?access_token={access_token}'
        return redirect(redirect_url)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Define a protected endpoint that requires authentication (For testing purposes)
@app.route('/protected')
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/logout')
@jwt_required()
def logout():
    response = jsonify({'logout': True})
    unset_jwt_cookies(response)
    return response, 200

# endregion

load_dotenv()
user = None;
conn = psycopg2.connect(os.getenv("DATABASE_URL"))
with conn.cursor() as cur:
    cur.execute("SELECT * FROM Food")
    res = cur.fetchall()
    conn.commit()
    print(res)
    
    cur.execute("SELECT * FROM users")
    res = cur.fetchall()
    conn.commit()
    print(res)
    
        
    cur.execute("SELECT * FROM shelf")
    res = cur.fetchall()
    conn.commit()
    print(res)

app.secret_key = os.getenv("APP_SECRET_KEY")
print([os.getenv("FRONTEND_URL")])
CORS(app, origins=[os.getenv("FRONTEND_URL")])

@app.route('/Food', methods=['GET'])
def get_all_Food():
    cur = conn.cursor()
    cur.execute("SELECT * FROM Food")
    rows = cur.fetchall()
    foods = []
    for row in rows:
        foods.append(Food(row[0], row[1], row[2], row[3]))
    return jsonify([my_object.__dict__ for my_object in foods])

@app.route('/food/<string:id>', methods=['GET'])
def get_Food(id):
    fode = getFood(id)
    if fode:
        return jsonify(fode.__dict__)
    return jsonify({'message': 'Food not found'}), 404
    
#used when food is being created and supports multiple creation of same food (increments the count)
@app.route('/food', methods=['POST'])
def create_food():
    data = request.json
    shelfId = data.get("shelfId")
    name = data.get('name')
    expiration_date = data.get('expiration_date')
    food = createFood( shelfId, name,expiration_date)
    return jsonify(food.__dict__)

#used when food is being eaten
@app.route('/food/use/<string:id>', methods=['PUT'])
def use_food(id):
    useFood(id)
    food = getFood(id)
    return jsonify(food.__dict__), 200

#used after food is created, just need id
@app.route('/food/add/<string:id>', methods=['PUT'])
def add_food(id):
    addFood(id)
    food = getFood(id)
    return jsonify(food.__dict__), 200

#TODO uncertain if this on is necessary could be helpful to change the expiration date
@app.route('/food/update/<string:id>', methods=['PUT'])
def update_food(id):
    data = request.get_json()
    cur = conn.cursor()
    cur.execute("UPDATE Food SET name = %s, expiration = %s, quantity = %s WHERE id = %s", (data['name'], data['expiration'], data['quantity'], id))
    conn.commit()
    cur.execute("SELECT * FROM my_objects WHERE id = %s", (id,))
    row = cur.fetchone()
    my_object = Food(row[0], row[1], row[2], row[3])
    return jsonify(my_object.__dict__), 200

#used when food is not wanted
@app.route('/food/<string:id>', methods=['DELETE'])
def delete_food(id):
    if(getFood(id) != None):
        removeFood(id)
        response = jsonify({'message': 'Food removed successfully'})
        return response, 204
    else:
        response = jsonify({"message": "Food does not exist in the database"})
        return response, 404


#used when moving a food to another shelf
@app.route('/food/move', methods=['PUT'])
def update_food_shelf():
    data = request.json
    shelfId = data.get("shelfId")
    foodId = data.get("foodId") 
    if(getFood(foodId) and getShelf(shelfId)):
        updateFoodShelf(foodId, shelfId)
        response = jsonify({'message': 'Food moved successfully'})
        return response, 204
    else:
        response = jsonify({"message": "Food or Shelf does not exist in the database"})
        return response, 404

#used when there is no shelf
@app.route('/shelf', methods=['POST'])
def create_shelf():
    data = request.json
    userId = data.get('userId')
    addShelf(userId)
    response = jsonify({'message': 'Successfully created a shelf'})
    return response, 204


@app.route('/shelf', methods=['DELETE'])
def delete_shelf():
    data = request.json
    shelfId = data.get('shelfId')
    if(getShelf(shelfId, True) != None):
        removeShelf(shelfId)
        response = jsonify({'message': 'Successfully created a shelf'})
        return response, 204
    else:
        response = jsonify({"message":"Shelf was not found"})
        return response, 404



if __name__ == '__main__':
    app.run(debug=True)