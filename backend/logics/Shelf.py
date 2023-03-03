import sqlMethods as sql

class Shelf:
    def __init__(self, id):
        self.__id = id;
        self.__container = [];
  
    @property
    def id(self):
        return self.__id;

    @property
    def container(self):
        return self.__container;
    
    #adding item to the back
    def addFood(self, userId, shelfId, name, expiration):
        item = sql.getFood(name,expiration)
        count = 0;
        if item not in self.container:
            food = sql.addFood(shelfId, userId, name, expiration)
            self.container.append(food);
        else:
            for food in self.container:
                if food == item:
                    self.container[count] = food.increment();
                    sql.addFood(shelfId, userId, item.name, food.expiration, food.quantity);
                else:
                    count+=1
            

    def removeFood(self, food, userId):
        if food in self.container:
            self.container[self.container.index(food)] = None;
            sql.removeFood(food, self.id, userId)
            
            
    def useFood(self, item):
        if(item.quantity > 0):
            for e in self.__container:
                if(e == item):
                  updatedFood = item.decrement();
                  sql.useFood(updatedFood);
                  self.container[self.container.index(e)] = updatedFood;
        else:
            print("there is no more")
        
    #check if the container have available space
    def empty(self):
        if ((len(self.container) < 3) or (None in self.__container)):
            return True;
        else:
            return False;
