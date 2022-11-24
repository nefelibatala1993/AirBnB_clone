#!/usr/bin/python3
"""Defines the ``FileStorage`` class"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instance
    Attributes:
        __file_path (str): path to the JSON file
        __objects (dict): dictionary of objects. Initially
        empty, but it will store all objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self) -> dict:
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj) -> None:
        """Sets obj in __objects with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self) -> None:
        """Serializes __objects to JSON file"""
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_dict, f)

    def reload(self) -> None:
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
            for k, v in json_dict.items():
                obj = eval(v['__class__'])(**v)
                self.__objects[k] = obj
