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

        user = User(google_id=google_id, name=name, email=email)
        userinfo["userId"] = addUser(user)

        # Generate an access token and redirect to the splash page with the token in the query string
        print(userinfo)
        access_token = create_access_token(identity=userinfo)
        # TODO: change the hardcoded url
        redirect_url = f'{os.getenv("FRONTEND_URL")}/2225-swen-356-shelf-life/?access_token={access_token}'
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
        foods.append(Food( id=row[0], shelfId=row[1], name=row[2], expiration=row[3],dateAdded=row[4], quantity=row[5]))
    return jsonify([my_object.__dict__ for my_object in foods]), 200

@app.route('/food/<string:id>', methods=['GET'])
def get_Food(id):
    fode = getFood(id)
    if fode:
        return jsonify(fode.__dict__), 200
    return jsonify({'message': 'Food not found'}), 404
    
#used when food is being created and supports multiple creation of same food (increments the count)
@app.route('/food', methods=['POST'])
def create_food():
    data = request.json
    shelfId = data.get("shelfId")
    name = data.get('name')
    expiration_date = data.get('expiration_date')
    quantity = data.get('quantity')
    food = newCreateFood( shelfId, name,expiration_date, quantity)
    return jsonify(food), 201

@app.route('/deletefood', methods=['POST'])
def delete_food_new():
    data = request.json
    foodId = data.get("foodId")
    food = newDeleteFood( foodId)
    return jsonify(food), 201

#used when food is being updated or used or changed
@app.route('/food/updateQuantity/<string:id>', methods=['PUT'])
def update_food_quantity(id):
    data = request.json
    quantity = data.get("quantity")
    if( quantity ):
        updateFoodQuantity(id,quantity)
        food = getFood(id)
        return jsonify(food.__dict__), 200
    else:
        return jsonify({"message": "can not change a quantity to not a number"})

#TODO uncertain if this on is necessary could be helpful to change the expiration date
@app.route('/food/update/<string:id>', methods=['PUT'])
def update_food(id):
    data = request.get_json()
    food = Food(**data)
    updated_food = updateFood(food)
    return jsonify(updated_food.__dict__), 200

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


#used when moving a food to another shelf maybe elimate this because a user has one shelf
@app.route('/food/move', methods=['PUT'])
def update_food_shelf():
    data = request.json
    shelfId = data.get("shelfId")
    foodId = data.get("foodId") 
    if(getFood(foodId) and getShelf(shelfId)):
        updateFoodShelf(foodId, shelfId)
        response = jsonify({'message': 'Food moved successfully'})
        return response, 201
    else:
        response = jsonify({"message": "Food or Shelf does not exist in the database"})
        return response, 404

#used to create a shelf with a given name
@app.route('/shelf', methods=['POST'])
@jwt_required()
def create_shelf():
    data = request.json
    print("hello luke", data)
    shelfName = data.get('shelfName')

    userId = get_jwt_identity()['userId']

    addShelf(userId,shelfName)
    response = jsonify({'message': 'Successfully created a shelf'})
    return response, 201

#user can update the name of shelf using this method
@app.route('/shelf', methods=['PUT'])
def update_shelf():
    data = request.json
    shelfId = data.get('shelfId')
    newShelfName = data.get('shelfName')
    updateShelfName(shelfId, newShelfName)
    response = jsonify({'message': 'Successfully updated the shelf'})
    return response, 201


@app.route('/deleteshelf', methods=['POST'])
def delete_shelf():
    data = request.json
    shelfId = data.get('shelfId')
    if(getShelf(shelfId, True) != None):
        removeShelf(shelfId)
        response = jsonify({'message': 'Successfully deleted a shelf'})
        return response, 204
    else:
        response = jsonify({"message":"Shelf was not found"})
        return response, 404

#gets a shelf by a user Id #TODO this assumes that a user only has one shelf. For the demo this will be true but if this 
#was real application it would be more
@app.route('/shelf', methods= ['GET'])
@jwt_required()
def get_shelf():
    userId = get_jwt_identity()['userId']
    print("GET SHELF USERID", userId)
    shelf = getShelfByUserId(userUID=userId)

    newShelf = [[s, getFoodByShelfId(s[0])] for s in shelf]

    return jsonify(newShelf), 200


if __name__ == '__main__':
    app.run(debug=True)