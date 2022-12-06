#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all the common attributes/methods for the other classes"""
    def __init__(self) -> None:
        """Instantiaion Method / Default Constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> None:
        """Prints the string representation of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Returns a dictionary containing all keys/values of __dict__
        of the instance. A key '__class__' is added with the name of
        the class of the object"""
        dict_s = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_s[key] = value.isoformat()
            else:
                dict_s[key] = value
        dict_s['__class__'] = self.__class__.__name__
        return dict_s
