#!/usr/bin/pyhton3
"""Defines the ``BaseModel`` class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methoods for other classes
    Attributes:
          id (str): unique ID of a new instance
          created_at (datetime): current datetime when an instance is created
          updated_at (datetime): current datetime when an instance is created,
            and it will be updated everytime an object changes
    """
    def __init__(self):
        """Instantiation Method/ Default Constructor"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the ``updated_at`` datetime object"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of an object"""
        dict_s = {}
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dict_s[k] = v.isoformat()
            else:
                dict_s[k] = v
        return dict_s
