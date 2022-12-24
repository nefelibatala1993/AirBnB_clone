#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """`FileStorage` serializes instances to a JSON file and
    deserializes JSON file to instances. This is one of the
    storage engines that will power the AirBnB clone website"""
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns the dictionary `__objects` that contains all
        the objects created"""
        return self.__objects

    def new(self, obj) -> None:
        """Sets in `__objects` the new object (obj) with the key
        `<obj class name>.<obj id>`"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self) -> None:
        """Serializes __objects to JSON file (__file_path). This means
        that the objects now will be stored in a file, to be recovered
        later"""
        json_dict = {key: val.to_dict() for key, val in self.__objects.items()}

        # Save the objects to a JSON file
        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self) -> None:
        """Deserializes JSON file (__file_path) to __objects. This wil reload
        the objects from storage, hence retrieving objects from storage"""

        try:
            # Get the objects from the file
            with open(self.__file_path, 'r') as f:
                json_data = json.load(f)

            # Set in __objects the objects retrieved appropriately
            self.__objects = {
                key: eval(val['__class__'])(**val)
                for key, val in json_data.items()
            }
        except FileNotFoundError:
            pass
