#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self) -> None:
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj) -> None:
        """Sets in __objects the obj with key <obj class name>.id"""
        key = str(type(obj)) + "." + obj.id
        self.__objects[key] = obj

    def save(self) -> None:
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(json_dict, f)

    def reload(self) -> None:
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                obj = eval(value['__class__'])(**value)
                self.__objects[key] = obj
