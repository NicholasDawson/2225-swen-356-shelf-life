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
    sqlStatement = """INSERT INTO food(shelfId, name, expiration)
                    VALUES( '%s', '%s', '%s')""" %(shelfId, name, expiration);
    cursor.execute(sqlStatement);
    db.commit();


def getFood(shelfId, name) -> Food:
    sqlStatement = """SELECT foodId, expiration, quantity
                      FROM food
                      WHERE shelfId = '%s'
                      AND name = '%s' """ %(shelfId, name);
    cursor.execute(sqlStatement);
    food = cursor.fetchone();
    db.commit();
    return Food(food[0], shelfId, name, food[1], food[2])

def getFood(shelfId) -> Food:
    sqlStatement = """SELECT foodId, name, expiration, quantity
                      FROM food
                      WHERE shelfId = '%s'""" %(shelfId);
    cursor.execute(sqlStatement);
    food = cursor.fetchone();
    print(food)
    db.commit();
    
    # return Food(food[0][0], shelfId, food[0][1], food[0][2])
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
    return Shelf(shelfID);

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

