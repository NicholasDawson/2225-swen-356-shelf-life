from datetime import date, datetime


SUCCESS = "Success Operation";
UNSUCCESS = "Unsuccess Operation";

class Food:
    def __init__(self, id, name, expiration, quantity):
        self.__id = id;
        self.__name = name;
        self.__expiration = expiration;
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
    def quantity(self):
        return self.__quantity;
    
    @property 
    def shelfId(self):
        return self.__shelfId;
    
    @name.setter
    def name(self, name: str) -> str:
        if self.__name != name:
            self.__name = name 
            return SUCCESS;
        else:
            return UNSUCCESS;
                
    @quantity.setter
    def quantity(self, num: int):
        self.__quantity = num;
        
    @shelfId.setter
    def shelfId(self, id:int):
        self.__shelfId = id;
    
    def increment(self):
        self.__quantity += 1;
        return self;
    
    def decrement(self):
        self.__quantity -= 1;
        return self;
    
    def __str__(self) -> str:
        return self.id + " " + self.name + " " + str(self.expiration) + " " + str(self.quantity);
    
    def __eq__(self, __o: object) -> bool:
        return self.__hash__() == __o.__hash__();
    
    
    
    def __hash__(self) -> int:
        return hash(self.id + self.name + str(hash(self.expiration.__str__())) + str(self.quantity))