class Food:
    def __init__(self, id, shelfId, name, expiration, dateAdded, quantity):
        self.__id = id;
        self.__shelfId = shelfId;
        self.__name = name;
        self.__expiration = expiration;
        self.__dateAdded = dateAdded;
        self.__quantity = quantity;

    @property
    def id(self):
        return self.__id;
    
    @property
    def name(self):
        return self.__name;
    
    @property
    def expiration(self):
        return self.__expiration;
        
    @property
    def dateAdded(self):
        return self.__dateAdded;
    @property
    def quantity(self):
        return self.__quantity;
    
    @property 
    def shelfId(self):
        return self.__shelfId;
    
   