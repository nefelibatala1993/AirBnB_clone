#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime

import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs) -> None:
        """Instantiation Method(Default Constructor)"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(val,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, val)

    def __str__(self) -> str:
        """Returns the string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates an object"""
        self.updated_at = datetime.now()
        models.storage.save()

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
