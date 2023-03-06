from sqlMethods import *
expiration = "2016-06-22";

#create user
setup()
addUser("test1","123")
sir = getUser("test1","123")


#add food to current existing shelf array

sir.addFood("Tomato",expiration)
sir.addFood("Tomato",expiration)
print((sir.shelves[0].container[0]))
print(getFood("Tomato", expiration), "databaes")
print("\n")
# #testing if an item can be used 
# printTables()
sir.useFood("Tomato", expiration)
sir.useFood("Tomato", expiration)
sir.useFood("Tomato", expiration)

print(sir.shelves[0].container[0], "array container")
sir.addFood("Tomato",expiration) 
sir.addFood("Tomato", expiration)
print("\n")
print(sir.shelves[0].container[0], "array container")
print(getFood("Tomato", expiration), "databaes")
sir.removeFood("Tomato", expiration)

print(getFood("Tomato", expiration), "databaes")


sir.addFood("pickle",expiration)
sir.addFood("egg",expiration)
sir.addFood("cheese",expiration)
sir.addFood("milk",expiration)

print(sir.shelves[0].container[0], "shelves1")
print(sir.shelves[0].container[1], "shelves2")
print(sir.shelves[0].container[2], "big shelf")
print(sir.shelves[1].container[0], "big shelf")


# n1 = Shelf(1)
# n1.addFood(Food(1,2,"Tomato","2022-12-16",5))
# n1.addFood(Food(1,2,"Tomato","2022-12-17",5))
# n1.addFood(Food(1,2,"Tomato","2022-12-18",5))