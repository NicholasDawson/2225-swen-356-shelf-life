from datetime import datetime
import os
import psycopg2

from dotenv import load_dotenv
from models.Food import Food
from models.Shelf import Shelf
from models.User import User
load_dotenv()
db = psycopg2.connect(os.getenv("DATABASE_URL"))
db.autocommit = True

cursor = db.cursor();

def execute_sql(filename):    
    executable = "";
    with open(filename) as f:
        executable += f.read()
    cursor.execute(executable);
    
def printTables():
  cursor.execute("""SELECT table_name FROM information_schema.tables
  WHERE table_schema = 'public'""");
  for table in cursor.fetchall():
      print(table)
    
def setup():
    execute_sql("database/create_user_table.sql");
    execute_sql('database/create_shelf_table.sql')
    execute_sql('database/create_food_table.sql');

#food functionality
def createFood(shelfId, name, expiration, quantity = 1) -> Food:

    cursor.execute("""SELECT * FROM food
                      WHERE foodName = '%s' 
                      AND expiration = '%s'"""%(name, expiration))
    found = cursor.fetchone();
    if found == None:
        sqlStatement = """INSERT INTO food(shelfId, foodName, expiration, dateAdded)
                        VALUES('%s','%s', '%s', CURRENT_DATE)""" %(shelfId, name, expiration);
        cursor.execute(sqlStatement);
        
    else:
        cursor.execute("""UPDATE food
                          SET quantity = quantity + 1
                          WHERE foodName = '%s'
                          AND expiration = '%s'
                          """ %(name,expiration))
    result = getFoodByName(name, expiration)
    return result; 


def updateFoodQuantity(foodId, quantity):
    cursor.execute("""UPDATE food
                          SET quantity = '%d'
                          WHERE foodId = '%s'
                          """ %(quantity,foodId))



def getFood(foodId) -> Food:
    sqlStatement = """SELECT shelfId, name, expiration
                      FROM food
                      WHERE foodId = '%s'""" %(foodId)
    cursor.execute(sqlStatement)
    food = cursor.fetchone()
    if(food):
        return Food(id=foodId,name=food[0],expiration=food[1],quantity=food[2])
    return None


def getFoodByName(foodName) -> Food:
    sqlStatement = """SELECT foodId, shelfId, expiration, quantity, dateadded
                      FROM food
                      WHERE foodName = '%s'
                      """ %(foodName);
    cursor.execute(sqlStatement);
    food = cursor.fetchone();
    if food is None:
        return food
    foodid, shelfid, foodname, expiration, dateadded, quantity = food
    return Food(foodid, shelfid, foodname, expiration, dateadded, quantity)


def getFood(id) -> Food:
    sqlStatement = """SELECT *
                      FROM food
                      WHERE foodId = '%s'
                      """ %(id);
    cursor.execute(sqlStatement);
    food  = cursor.fetchone();
    if food is None:
        return food
    foodid, shelfid, foodname, expiration, dateadded, quantity = food
    return Food(foodid, shelfid, foodname, expiration, dateadded, quantity)


#full update on the food item
def updateFood(food:Food):
    sqlStatement = """ Update Food
                        Set foodName = '%s',
                        expiration = '%s',
                        quantity = '%s',
                        dateadded = '%s'
                        WHERE foodId = '%s'
                   """%(food.name, food.expiration, food.quantity, food.dateAdded, food.id)
    cursor.execute(sqlStatement);
    return getFood(food.id)


def useFood(foodId):
    sqlStatement = """UPDATE food
                    SET quantity = quantity - 1 
                    WHERE foodId = '%s' AND quantity > 0"""%(foodId)
    cursor.execute(sqlStatement);

#Can be used with or without a shelf or user ID
def removeFood(foodId, userId):
    sqlStatement = """DELETE from food
                    WHERE foodId = '%s'
                   """%(foodId)
    cursor.execute(sqlStatement);
    
def removeFood(foodId):
    sqlStatement = """DELETE from food
                    WHERE foodId = '%s'
                   """%(foodId)
    cursor.execute(sqlStatement);

def updateFoodShelf(foodId, newShelfId):
    sqlStatement = """
        UPDATE food
        SET shelfId = '%s'
        WHERE foodID = '%s'
    """%(newShelfId,foodId)
    cursor.execute(sqlStatement) 
#shelves functionality
#-------------------------------------
def addShelf(userUID, shelfName = 1):
    if(shelfName):
        sqlStatement = """
            INSERT INTO shelf(userId)
            VALUES( '%s')
        """ %(userUID);
    else:
        sqlStatement = """
            INSERT INTO shelf(userId, shelfName)
            VALUES('%s','%s')
        """
    cursor.execute(sqlStatement)
    
#gets all the shelves a user has
def getShelves(userUID):
    sqlStatement = """
        SELECT shelfID
        FROM shelf
        WHERE userID = '%s'
    """%(userUID)
    cursor.execute(sqlStatement)
    shelveIds = cursor.fetchall()
    return shelveIds

def getShelfByUserId(userUID) -> Shelf:
    sqlStatement = """
        SELECT *
        FROM shelf
        WHERE userID = '%s'
    """%(userUID)
    cursor.execute(sqlStatement)
    shelf = cursor.fetchone()
    return Shelf(shelf[0], shelf[1], shelf[2]);

def getShelf(userUID, boolean) -> Shelf:
    sqlStatement = """
        SELECT *
        FROM shelf
        WHERE shelfId = '%s'
    """%(userUID)
    cursor.execute(sqlStatement)
    shelf = cursor.fetchone()
    if(shelf is None):
        return shelf;
    return Shelf(shelf[0],shelf[1],shelf[2]);

def removeShelf(shelfId):
    sqlStatement = """
        DELETE FROM food
        WHERE shelfId = '%s'
    """%(shelfId)
    cursor.execute(sqlStatement)
    sqlStatement = """
        DELETE FROM shelf
        WHERE shelfId = '%s'
    """%(shelfId)
    cursor.execute(sqlStatement)

def updateShelfName(shelfId, shelfName):
    sqlStatement = """
        UPDATE shelf
        SET shelfName = '%s'
        WHERE shelfId = '%s'
    """%(shelfName,shelfId)
    cursor.execute(sqlStatement)

#users functionality
#--------------------------------------
def addUser(usr: User):
    sqlStatement = """
        INSERT INTO users(username, email, google_id)
        VALUES('%s', '%s', '%s');
    """%(usr.name, usr.email, usr.google_id)
    cursor.execute(sqlStatement)
    
    
def getUser(usn) -> User:
    cursor.execute("""SELECT userID 
                             FROM users
                             WHERE username = '%s'
                             """%(usn));
    id = cursor.fetchone();
    if(id != None):
        return User(id[0],usn)
    else:
        return None

def getUserByGoogleID(google_id) -> User:
    cursor.execute("""SELECT  userId, username, email
                             FROM users
                             WHERE google_id = '%s'
                             """%(google_id))
    result = cursor.fetchone()
    if result is not None:
        userId, username, email = result
        return User(userId, username, email, google_id)
    else:
        return None
