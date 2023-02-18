from logics.User import User
from logics.Shelf import Shelf
from logics.Food import Food

#food functionality
def addFood(cursor, shelfId, name, expiration):
    sqlStatement = """INSERT INTO food(shelfId, name, expiration)
                    VALUES( %d, '%s', '%s')""" %(shelfId, name, expiration);
    cursor.execute(sqlStatement);

def getFood(cursor, shelfId, name):
    sqlStatement = """SELECT foodId, expiration, quantity
                      FROM food
                      WHERE shelfId = '%s'
                      AND name = '%s' """ %(shelfId, name);
    cursor.execute(sqlStatement);
    food = cursor.fetchone();
    return Food(food[0], shelfId, name, food[1], food[2])
#shelves functionality
#-------------------------------------
def addShelf(cursor,userUID):
    sqlStatement = """
        INSERT INTO shelf()
        VALUES(get_random_uuid(), '%s')
    """ %(userUID);
    cursor.execute(sqlStatement)

def getShelf(cursor, userUID):
    sqlStatement = """
        SELECT shelfID
        FROM shelf
        WHERE userID = '%s'
    """%(userUID)
    cursor.execute(sqlStatement)
    shelfID = cursor.fetchone()
    return Shelf(shelfID, userUID);

#users functionality
#--------------------------------------
def addUser(cursor,usn,pwd):
    sqlStatement = """
        INSERT INTO users(username, password)
        VALUES('%s','%s');
    """%(usn,pwd)
    cursor.execute(sqlStatement);
    
def getUser(cursor,usn,pwd) -> User:
    cursor.execute("""SELECT userID 
                             FROM users
                             WHERE username = '%s'
                             AND password = '%s'
                             """%(usn,pwd));
    id = cursor.fetchone();
    return User(id[0],usn,pwd)

