#!/usr/bin/python3
"""Defines the FileStorage class"""
import json


class FileStorage:
    """FileStorage manages the file storage engine for AirBnB Clone"""
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj) -> None:
        """Sets in obj to __objects. Key will be the class
        name and its id --> <class name>.<obj id>"""
        self.__objects.update({
            obj.__class__.__name__ + "." + obj.id: obj
        })

    def save(self) -> None:
        """Saves the dict __objects to a JSON file (__file_path)"""
        json_dict = {
            k: v.to_dict() for k, v in self.__objects.items()
            }
        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self) -> None:
        """Reloads all the objects stored in the __file_path"""
        from models.base_model import BaseModel

        classes = {
            "BaseModel": BaseModel
        }

        try:
            with open(self.__file_path, 'r') as f:
                json_dict = json.load(f)

            dict_s = {
                k: classes[v['__class__']](**v) for k, v in json_dict.items()
            }
            self.__objects.update(dict_s)
        except FileNotFoundError:
            pass
