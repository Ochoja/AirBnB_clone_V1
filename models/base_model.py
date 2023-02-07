#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self):
        """Constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of all key/values
        of __dict__ of the instance"""
        dict_values = self.__dict__
        dict_values["__class__"] = type(self).__name__ # adds class name to dict
        dict_values["created_at"] = datetime.isoformat(self.created_at)
        dict_values["updated_at"] = datetime.isoformat(self.updated_at)
        return dict_values

    def __str__(self):
        """Runs when user prints instance eg. print(self)"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

a = BaseModel()
print(a.to_dict())
