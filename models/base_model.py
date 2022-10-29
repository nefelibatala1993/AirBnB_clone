#!/usr/bin/python3
"""Defines the BaseModel class"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """BaseModel that defines the common attributes/methods for
        other classes

    Attributes:
          id (str): unique id of an instance
          created_at (str): time when the instance is created at
          updated_at (str): time when the instance has been updated/modified
    """

    def __init__(self, *args, **kwargs):
        """Instantiation Method"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)

            self.created_at = datetime.strptime(self.created_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at,
                                                '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """Returns string representation of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute when the instance is
            updated/modified"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an object"""
        dict_s = {}
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dict_s[k] = v.isoformat()
            else:
                dict_s[k] = v
        dict_s["__class__"] = self.__class__.__name__
        return dict_s
