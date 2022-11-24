#!/usr/bin/python3
"""Defines the BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes
    Attributes:
        id (str): unique ID for an instance object
        created_at (datetime): datetime when an object is created
        updated_at (datetime): datetime when an object is updated
    """
    def __init__(self, *args, **kwargs):
        """Instantiation Method / Default Constructor"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, k, v)

    def __str__(self) -> None:
        """Returns the string representation of an object"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self) -> None:
        """Updates an Object when an object has been changes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """Returns the dictionary representation of an object"""
        dict_s = {}
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dict_s[k] = v.isoformat()
            else:
                dict_s[k] = v
        dict_s['__class__'] = type(self).__name__
        return dict_s
