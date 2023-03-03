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
        
    def addFood(self, name, expiration):
        food = sql.getFood(name,expiration)
        print(food);
        if(len(self.shelves) == 0):
            newShelf = self.addShelf();
            newShelf.addFood(self.id, newShelf.id, name, expiration); 
            return;
        else:
            
            for shelf in self.shelves:
                if food in shelf.container:
                    shelf.addFood(self.id, shelf.id, name, expiration)
                    break;
                else:
                    if shelf.empty():
                        shelf.addFood(self.id, shelf.id, name, expiration);
                        break;
        
                
    def useFood(self, name, expiration):
        for s in self.shelves:
            food = sql.getFood(name, expiration);
            if food in s.container:
                s.useFood(food);
            
    def removeFood(self, name, expiration):
        for s in self.shelves:
            food = sql.getFood(name, expiration);
            if food in s.container:
                s.remove(food);
    
    def __str__(self) -> str:
        return "ID - " + self.id + " | NAME - "+self.name
    
    
    #technical debt, manage the workload, peak traffic, balanced the load, architecture
    #business model, text stack, work-life balanced
    #change something about your work, what do you think
    #fav, improve?