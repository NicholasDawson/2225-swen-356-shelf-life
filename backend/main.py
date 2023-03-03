from sqlMethods import *
expiration = "2016-06-22";

#create user
setup()
addUser("test1","123")
sir = getUser("test1","123")

# #create a new shelf
newShelf = sir.addShelf();

#add food to current existing shelf array

sir.addFood("Tomato",expiration)
sir.addFood("Tomato",expiration)
print((sir.shelves[0].container))
# print(sir.shelves[0].container)
# #testing if an item can be used 
# printTables()
# sir.useFood("Tomato", expiration)
# # sir.removeFood("Tomato", expiration)
# print( getFood("Tomato",expiration) , " this is after remove and use")

# print(newShelf.container)

# sir.addFood("Tomato",expiration)
# sir.addFood("Tomato", expiration)
# print(getFood("Tomato",expiration))


# n1 = Shelf(1)
# n1.addFood(Food(1,2,"Tomato","2022-12-16",5))
# n1.addFood(Food(1,2,"Tomato","2022-12-17",5))
# n1.addFood(Food(1,2,"Tomato","2022-12-18",5))