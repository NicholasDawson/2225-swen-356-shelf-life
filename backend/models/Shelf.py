class Shelf:
    def __init__(self, id, shelfName, uid):
        self.__id = id;
        self.__shelfName = shelfName;
        self.__userId = uid;
  
    @property
    def id(self):
        return self.__id;

    @property
    def shelfName(self):
        return self.__shelfName;

    @property
    def uid(self):
        return self.__userId;
    
