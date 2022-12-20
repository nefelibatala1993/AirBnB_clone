#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self) -> None:
        """Instantiation Method(Default Constructor)"""
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """Returns the string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates an object"""
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Returns the dictionary representation of an object"""
        dict_s = {}
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                dict_s[key] = val.isoformat()
            else:
                dict_s[key] = val
            dict_s['__class__'] = self.__class__.__name__
        return dict_s
