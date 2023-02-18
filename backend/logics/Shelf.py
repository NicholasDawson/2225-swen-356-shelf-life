from .Food import Food


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
    
    def addItem(self, item: Food):
        self.__container.append(item);
    
    def removeItem(self, item: Food):
        self.__container.remove(item);
