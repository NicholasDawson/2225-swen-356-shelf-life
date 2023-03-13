class User:
    def __init__(self, id, name, email, googleId):
        self.__id = id;
        self.__name = name;
        self.__email = email;
        self.__googleId = googleId;
        
    @property
    def id(self):
        return self.__id;
    
    @property
    def name(self):
        return self.__name;

    @property
    def email(self):
        return self.__email;

    @property
    def googleId(self):
        return self.__googleId;

