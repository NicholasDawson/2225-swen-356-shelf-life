class Shelf:
    def __init__(self, id, uid):
        self.__id = id;
        self.__userId = uid;
  
    @property
    def id(self):
        return self.__id;

    @property
    def uid(self):
        return self.__userId;
    
