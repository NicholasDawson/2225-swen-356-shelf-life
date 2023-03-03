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
    def addFood(self, userId, shelfId, name, expiration, index = -1):
        item = sql.getFood(name,expiration)
        count = 0;
        if item is None:
            food = sql.addFood(shelfId, userId, name, expiration)
            if None in self.container:
                self.container[self.container.index(None)] = food
            else:
                self.container.append(food);
        else:
            if(index != -1):
                self.container[index-1] = item.increment();
                sql.addFood(shelfId, userId, item.name, item.expiration, item.quantity);
            

    def removeFood(self, food, userId, index):
        self.container[index] = None;
        sql.removeFood(food, self.id, userId)
            
            
    def useFood(self, item, index):
        if(item.quantity > 0):
            updatedFood = item.decrement();
            sql.useFood(updatedFood);
            self.container[index] = updatedFood;
        else:
            print("there is no more")
        
    
    #check if the container have available space
    def empty(self):
        if ((len(self.container) < 3) or (None in self.container)):
            return True;
        else :
            return False;
