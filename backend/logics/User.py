
from .Shelf import Shelf


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
    
    def addShelf(self):
        #generate a new uuid from sql and then get from the table
        
        self.__shelves.append(Shelf());
    
    def __str__(self) -> str:
        return "ID - " + self.id + " | NAME - "+self.name