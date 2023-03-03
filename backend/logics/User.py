from logics import Food
import sqlMethods as sql;

class User:
    def __init__(self, id, name, pwd):
        self.__id = id;
        self.__name = name;
        self.__pwd = pwd;
        self.__shelves = [];
        
    @property
    def id(self):
        return self.__id;
    
    @property
    def name(self):
        return self.__name;
    
    @property
    def pwd(self):
        return self.__pwd;
    
    @property
    def shelves(self):
        return self.__shelves;
    
    def addShelf(self):
        #generate a new uuid from sql and then get from the table
        #init a new shelf for the user
        sql.addShelf(self.id);
        newShelf = sql.getShelf(self.id);
        self.shelves.append(newShelf);
        return newShelf;
    
    def deleteShelf(self, shelf):
        #delete a shelf
        self.shelves.remove(shelf);
        sql.removeShelf(shelf.id);
        
    def newItemAdd(self, name, expiration):
        newShelf = self.addShelf();
        newShelf.addFood(self.id, newShelf.id, name, expiration); 
        
    def addFood(self, name, expiration):
        endOfArray = len(self.shelves)
        counter = 1;
        if(len(self.shelves) == 0 ):
            self.newItemAdd(name,expiration)
            return;
        else:
            for shelf in self.shelves:
                if shelf.empty():
                    shelf.addFood(self.id, shelf.id, name, expiration);
                    return;
                elif counter == endOfArray:
                    self.newItemAdd(name,expiration)
                    return;
                else:
                    counter+=1
                    
            # elif endOfArray == 0:
            #     print(name)
            #     newShelf = self.addShelf();
            #     newShelf.addFood(self.id, newShelf.id, name, expiration); 
            #     return;
            # else:
            #     endOfArray -=1
                    
        
                
    def useFood(self, name, expiration):
        index = 0
        food = sql.getFood(name, expiration);
        for s in self.shelves:
            if food in s.container:
                s.useFood(food, index);
                return;
            else:
                index += 1
            
                    
    # def useFood(self, foodId):
    #     index = 0
    #     food = sql.getFood(foodId);
    #     for s in self.shelves:
    #         if food in s.container:
    #             s.useFood(food, index);
    #             return;
    #         else:
    #             index +=1
            
    def removeFood(self, name, expiration):
        index = 0;
        food = sql.getFood(name, expiration);
        for shelf in self.shelves:
            if food in shelf.container:
                shelf.removeFood(food, self.id, index);
            else:
                index += 1
                
    # def removeFood(self, foodId):
    #     food = sql.getFood(foodId);
    #     for shelf in self.shelves:
    #         if food in shelf.container:
    #             shelf.removeFood(food, self.id);
    def __str__(self) -> str:
        return "ID - " + self.id + " | NAME - "+self.name
    
