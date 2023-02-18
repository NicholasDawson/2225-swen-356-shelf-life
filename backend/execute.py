from sqlMethods import *


setup()
addUser("test1","123")
sir = getUser("test1","123")
addShelf(sir.id)
shelf = getShelf(sir.id)

addFood(shelf.id[0],"Tomato","2016-06-22 19:10:25-07")
food = getFood(shelf.id[0])
print(shelf)
print(food)
printTables()

cursor.execute("SELECT * FROM food")
shelfOne = cursor.fetchall();
print(shelfOne)
