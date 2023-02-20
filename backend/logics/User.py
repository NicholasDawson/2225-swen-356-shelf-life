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
    
    def addShelf(self):
        #generate a new uuid from sql and then get from the table
        #init a new shelf for the user
        sql.addShelf(self.__id);
        Shelf = sql.getShelf(self.__id);
        self.__shelves.append(Shelf);
        return Shelf;
    
    def __str__(self) -> str:
        return "ID - " + self.id + " | NAME - "+self.name