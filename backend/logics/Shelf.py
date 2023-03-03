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
        print(hash(item))
        if item not in self.container:
            food = sql.addFood(shelfId, userId, name, expiration)
            self.container.append(food);
        else:
            self.container[self.container.index(item)] = item.increment();
            food = sql.addFood(shelfId, userId, name, expiration);
            

    def removeFood(self, item ):
        if item in self.container:
            self.container[self.container.index(item)] = None;
            sql.removeFood(item, self.id)
            
    def useFood(self, item):
        if(item.quantity > 0):
            for e in self.__container:
                if(e == item):
                  updatedFood = item.decrement();
                  sql.useFood(updatedFood, self.id);
                  self.container[self.container.index(e)] = updatedFood;
        
    #check if the container have available space
    def empty(self):
        if ((len(self.container) < 3) or (None in self.__container)):
            return True;
        else:
            return False;
