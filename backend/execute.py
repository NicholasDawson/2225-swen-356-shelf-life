from sqlMethods import *

#create user
setup()
addUser("test1","123")
sir = getUser("test1","123")

#create a new shelf
newShelf = sir.addShelf();

#add food to current existing shelf array
addFood(newShelf.id,"Tomato","2016-06-22 19:10:25-07")

#testing if an item can be used 
food = getFood("Tomato")
print(food)
printTables()
print(newShelf.container)
newShelf.addFood(food);
newShelf.useFood(food);
print(newShelf.container[0])

food = getFood("Tomato");
print(food);

newShelf.removeFood(food)

print(newShelf.container)
food = getFood("Tomato")
