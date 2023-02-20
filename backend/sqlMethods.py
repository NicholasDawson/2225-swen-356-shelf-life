import psycopg2
from sqlMethods import *

db = psycopg2.connect(
  database = "shelflife",
  user = "shelflife",
  password = "12345",
  host = "localhost",
  port = '5432'
)
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
    execute_sql("database\create_user_table.sql");
    execute_sql('database\create_shelf_table.sql')
    execute_sql('database\create_food_table.sql');



#food functionality
def addFood(shelfId, name, expiration):

    cursor.execute("""SELECT * FROM food
                      WHERE name = '%s'"""%(name))
    if cursor.fetchone() == None:
        sqlStatement = """INSERT INTO food(shelfId, name, expiration, dateAdded)
                        VALUES( '%s', '%s', '%s', CURRENT_DATE)""" %(shelfId, name, expiration);
        cursor.execute(sqlStatement);
        db.commit();
    else:
        return


def getFood(foodId) -> Food:
    sqlStatement = """SELECT shelfId, name, expiration, quantity
                      FROM food
                      WHERE foodId = '%s'""" %(foodId);
    cursor.execute(sqlStatement);
    food = cursor.fetchone();
    db.commit();
    return Food(foodId,food[0],food[1],food[2],food[3]);


def getFood(foodName) -> Food:
    sqlStatement = """SELECT foodId, shelfId, expiration, quantity
                      FROM food
                      WHERE name = '%s'""" %(foodName);
    cursor.execute(sqlStatement);
    food = cursor.fetchone();
    db.commit();
    if food is None:
        return food;
    return Food(food[0],food[1],foodName,food[2],food[3]);

def useFood(food : Food, shelfId):
    sqlStatement = """UPDATE food
                    SET quantity = %d
                    WHERE foodId = '%s'
                    AND shelfId = '%s'"""%(food.quantity, food.id, shelfId)
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



