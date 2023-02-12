#!/usr/bin/python3
"""BaseModel parent class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            # set instance attributes using kwargs dictionary
            for key, value in kwargs.items():
                if key == "__class__":  # skip `__class__` key
                    continue
                else:
                    # convert datetime string to datetime object
                    if key == "created_at" or key == "updated_at":
                        date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, date)
                    else:
                        setattr(self, key, value)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary of all key/values
        of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__  # adds class name to dict
        new_dict["created_at"] = datetime.isoformat(self.created_at)
        new_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return new_dict

    def __str__(self):
        """Runs when user prints instance eg. print(self)"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    @staticmethod
    def all():
        """returns all instances saved"""
        return storage.all()
