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
        self.__container.append(item);
    
    #adding item to a specific spot
    # def addItem(self, item: Food, index):
    #     self.__container[index] = item;
    
    #removing item from a specific spot
    def removeItem(self, index : int):   
        if(self.___container[index] != None):
            self.__container[index] = None;

    def removeItem(self, item : Food):
        index = self.__container.index(item);
        if(self.__container[index] != None):
            self.__container[index] = None;
            
    def useFood(self, item : Food):
        if(item.quantity > 0):
            for e in self.__container:
                if(e == item):
                  updatedFood = item.decrement();
                  sqlMethods.useFood(updatedFood, self.id);
        
        
        
        
    #check if the container have available space
    def empty(self):
        if ((self.__container.length() > 3) and (None not in self.__container)):
            return True;
        else:
            return False;