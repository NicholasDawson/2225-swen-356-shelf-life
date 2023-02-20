from .Food import Food
import sqlMethods

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
    def addFood(self, item: Food):
        if item not in self.container:
            self.__container.append(item);
            sqlMethods.addFood(self.id, item.name, item.expiration)

    def removeFood(self, item : Food):
        if item in self.container:
            self.container[self.container.index(item)] = None;
            sqlMethods.removeFood(item, self.id)
            
    def useFood(self, item : Food):
        if(item.quantity > 0):
            for e in self.__container:
                if(e == item):
                  updatedFood = item.decrement();
                  sqlMethods.useFood(updatedFood, self.id);
                  self.container[self.container.index(item)] = updatedFood;
        
    #check if the container have available space
    def empty(self):
        if ((self.__container.length() > 3) and (None not in self.__container)):
            return True;
        else:
            return False;