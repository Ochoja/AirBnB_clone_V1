#!/usr/bin/python3
import uuid, datetime

class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, id, created_at, updated_at):
        """Constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary of all key/values
        of __dict__ of the instance"""
        dict_values = self.__dict__
        dict_values["__class__"] = type(self).__name__

    def __str__(self):
        """Runs when user prints instance eg. print(self)"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
