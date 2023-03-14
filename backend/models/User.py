import uuid


class User:
    def __init__(self,   name, email, google_id, id=None ):
        self.__id = id or uuid.uuid4()
        self.__name = name;
        self.__email = email;
        self.__google_id = google_id;
        
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
    def google_id(self):
        return self.__google_id;

