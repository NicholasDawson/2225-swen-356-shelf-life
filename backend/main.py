from sqlMethods import *

#create user
setup()
addUser("test1","123")
sir = getUser("test1","123")

# #create a new shelf
# newShelf = sir.addShelf();

#add food to current existing shelf array
sir.addFood("Tomato","2016-06-22")

print(sir.shelves[0].container)
#testing if an item can be used 
printTables()
# print(newShelf.container)
# sir.useFood("Tomato", "2016-06-22")

# sir.removeFood("Tomato", "2016-06-22")

# print(newShelf.container)


# n1 = Shelf(1)
# n1.addFood(Food(1,2,"Tomato","2022-12-16",5))
# n1.addFood(Food(1,2,"Tomato","2022-12-17",5))
# n1.addFood(Food(1,2,"Tomato","2022-12-18",5))