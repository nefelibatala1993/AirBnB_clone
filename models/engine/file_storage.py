#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """This class serializes instances to a JSON file and
        deserializes JSON file to instance
    Attributes:
        __file_path (str): path to te JSON file
        __objects (dict): initially it is an empty dictionary,
            but will store all objects by <class name>.<id>
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of __objects"""
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json_dict = {}
            for k, v in self.__objects.items():
                json_dict[k] = v.to_dict()
            json.dump(json_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        if path.isfile(self.__file_path):
            dict_s = {}
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                dict_s = json.load(f)

            for k, v in dict_s.items():
                instance = eval(v['__class__'])(**v)
                self.__objects[k] = instance
