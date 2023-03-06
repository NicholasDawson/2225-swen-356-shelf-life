from datetime import datetime
import os
import psycopg2

from dotenv import load_dotenv
from logics.Food import Food
from logics.Shelf import Shelf
from logics.User import User
load_dotenv()
db = psycopg2.connect(os.getenv("DATABASE_URL"))

cursor = db.cursor();

def execute_sql(filename):    
    executable = "";
    with open(filename) as f:
        executable += f.read()
    cursor.execute(executable);
    db.commit();
    
def printTables():
  cursor.execute("""SELECT table_name FROM information_schema.tables
  WHERE table_schema = 'public'""");
  for table in cursor.fetchall():
      print(table)
    
def setup():
    execute_sql('database/create_shelf_table.sql')
    execute_sql("database/create_user_table.sql");
    execute_sql('database/create_food_table.sql');

#food functionality
def addFood(shelfId, userId, name, expiration, quantity = 1):

    cursor.execute("""SELECT * FROM food
                      WHERE name = '%s' 
                      AND expiration = '%s'"""%(name, expiration))
    found = cursor.fetchone();
    if found == None:
        
        sqlStatement = """INSERT INTO food(name, expiration, dateAdded)
                        VALUES('%s', '%s', CURRENT_DATE)""" %(name, expiration);
        cursor.execute(sqlStatement);
        cursor.execute("""SELECT foodId,name,expiration,quantity FROM food
                      WHERE name = '%s' 
                      AND expiration = '%s'"""%(name, expiration))
        db.commit();
        result = cursor.fetchone();
        sqlStatement = """UPDATE shelf
                          SET foodId = '%s'
                          WHERE shelfId = '%s'
                          AND userId = '%s'"""%(result[0],shelfId,userId)
        cursor.execute(sqlStatement);
        return Food(result[0],result[1],result[2],result[3]);
    else:
        cursor.execute("""UPDATE food
                          SET quantity = %d
                          WHERE name = '%s'
                          AND expiration = '%s'""" %(quantity, name, expiration))
        cursor.execute("""SELECT foodId,name,expiration,quantity FROM food
                      WHERE name = '%s' 
                      AND expiration = '%s'"""%(name, expiration))
        result = cursor.fetchone()
        return Food(result[0],result[1],result[2],result[3]);        



def getFood(foodId) -> Food:
    sqlStatement = """SELECT shelfId, name, expiration
                      FROM food
                      WHERE foodId = '%s'""" %(foodId)
    cursor.execute(sqlStatement)
    food = cursor.fetchone()
    if(food):
        db.commit()
        return Food(id=foodId,name=food[0],expiration=food[1],quantity=food[2])
    return None


def getFood(foodName,expiration) -> Food:
    format = '%Y-%m-%d'
    sqlStatement = """SELECT foodId, quantity
                      FROM food
                      WHERE name = '%s'
                      AND expiration = '%s'""" %(foodName,datetime.strptime(expiration, format));
    cursor.execute(sqlStatement);
    food = cursor.fetchone();
    db.commit();
    if food is None:
        return food
    return Food(food[0],foodName,expiration,food[1])



def getFoodById(id) -> Food:
    sqlStatement = """SELECT *
                      FROM food
                      WHERE id = '%s'
                      """ %(id);
    cursor.execute(sqlStatement);
    food = cursor.fetchone();
    db.commit();
    if food is None:
        return food
    return Food(food[0],food[1],food[2],food[3])

def useFood(food : Food):
    sqlStatement = """UPDATE food
                    SET quantity = %d
                    WHERE foodId = '%s'"""%(food.quantity, food.id)
    cursor.execute(sqlStatement);
    db.commit();

def useFood(food : Food):
    sqlStatement = """UPDATE food
                    SET quantity = %d
                    WHERE foodId = '%s'"""%(food.quantity, food.id)
    cursor.execute(sqlStatement);
    db.commit();

#Can be used with or without a shelf or user ID
def removeFood(foodId, shelfId, userId):
    sqlStatement = """DELETE from food
                    WHERE foodId = '%s'
                   """%(foodId)
    cursor.execute(sqlStatement);
    db.commit();
    
#shelves functionality
#-------------------------------------
def addShelf(userUID):
    sqlStatement = """
        INSERT INTO shelf(userId)
        VALUES( '%s')
    """ %(userUID);
    cursor.execute(sqlStatement)
    db.commit();
    

def getShelf(userUID) -> Shelf:
    sqlStatement = """
        SELECT shelfID
        FROM shelf
        WHERE userID = '%s'
    """%(userUID)
    cursor.execute(sqlStatement)
    shelfID = cursor.fetchone()
    db.commit();
    return Shelf(shelfID[0]);

#users functionality
#--------------------------------------
def addUser(usn):
    sqlStatement = """
        INSERT INTO users(username)
        VALUES('%s');
    """%(usn)
    cursor.execute(sqlStatement);
    db.commit();
    
    
def getUser(usn) -> User:
    cursor.execute("""SELECT userID 
                             FROM users
                             WHERE username = '%s'
                             """%(usn));
    id = cursor.fetchone();
    db.commit();
    return User(id[0],usn)



