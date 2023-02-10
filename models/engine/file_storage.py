#!/usr/bin/python3
"""Module used for storing files"""
import json


class FileStorage:
    """Serializes instances to JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"  # path to JSON file
    __objects = {}  # Stores all objects/instances

    def all(self):
        """returns the dictionary `__objects`"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in `__objects` the `obj` with key
        <obj class name>.id (eg. BaseModel instance
        with id=123654 will have a key `BaseModel.123654`)
        """
        key = type(obj).__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize `__objects` to the JSON file `__file_path`
        """
        new_dict = {}

        # convert values in `__objects` to dictionary and save in new_dict
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        """
        Deserialize JSON file saved in `__file_path` to `__objects`
        """
        temp_dict = {}

        try:
            with open(FileStorage.__file_path, 'r') as json_file:
                temp_dict = json.load(json_file)
        except FileNotFoundError:
            pass  # Do nothing if file does not exist
        else:
            # create objects from temp_dict values and save in `__objects`
            for key, value in temp_dict.items():
                # key.__class__ = Class Name (eg.'BaseModel' <type: str>)
                # convert dict to obj and add to `__objects`
                class_name = key.__class__
                exec(f"obj = {class_name}({value})")
                FileStorage.__objects[key] = obj
