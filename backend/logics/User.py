class User:
    def __init__(self, id, name):
        self.__id = id;
        self.__name = name;
        
    @property
    def id(self):
        return self.__id;
    
    @property
    def name(self):
        return self.__name;

