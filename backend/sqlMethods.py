import os
import psycopg2

db = psycopg2.connect(os.getenv("DATABASE_URL"))

cursor = db.cursor();

from logics.User import User
from logics.Shelf import Shelf
from logics.Food import Food

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
    execute_sql('../database/create_shelf_table.sql')
    execute_sql("../database/create_user_table.sql");
    execute_sql('../database/create_food_table.sql');

#food functionality
def addFood(shelfId, userId, name, expiration):

    cursor.execute("""SELECT * FROM food
                      WHERE name = '%s' 
                      AND expiration = '%s'"""%(name, expiration))
    if cursor.fetchone() == None:
        # sqlStatement = """UPDATE INTO shelf(shelfId, userId)
        #                   VALUES('%s', '%s')"""%(shelfId,userId)
        # cursor.execute(sqlStatement);
        sqlStatement = """INSERT INTO food(name, expiration, dateAdded)
                        VALUES('%s', '%s', CURRENT_DATE)""" %(name, expiration);
        cursor.execute(sqlStatement)
        cursor.execute("""SELECT * FROM food
                      WHERE name = '%s' 
                      AND expiration = '%s'"""%(name, expiration))
        db.commit()
        return cursor.fetchone()[0]
    return None



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


def getFoodWithExpiration(foodName,expiration) -> Food:
    print(foodName + " " + expiration)
    sqlStatement = """SELECT foodId, quantity
                      FROM food
                      WHERE name = '%s'
                      AND expiration = '%s'""" %(foodName,expiration);
    cursor.execute(sqlStatement);
    food = cursor.fetchone();
    db.commit();
    if food is None:
        return food
    return Food(food[0],foodName,expiration,food[1])

def useFood(food : Food):
    sqlStatement = """UPDATE food
                    SET quantity = %d
                    WHERE foodId = '%s'"""%(food.quantity, food.id)
    cursor.execute(sqlStatement);
    db.commit();

def removeFood(food: Food, shelfId):
    sqlStatement = """DELETE from food
                    WHERE foodId = '%s'
                    AND shelfId = '%s'"""%(food.id, shelfId)
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
def addUser(usn,pwd):
    sqlStatement = """
        INSERT INTO users(username, password)
        VALUES('%s','%s');
    """%(usn,pwd)
    cursor.execute(sqlStatement);
    db.commit();
    
def getUser(usn,pwd) -> User:
    cursor.execute("""SELECT userID 
                             FROM users
                             WHERE username = '%s'
                             AND password = '%s'
                             """%(usn,pwd));
    id = cursor.fetchone();
    db.commit();
    return User(id[0],usn,pwd)



