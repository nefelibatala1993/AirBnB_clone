#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

my_model = BaseModel()
key = my_model.__class__.__name__ + "." + my_model.id
print(my_model)
print(storage.all())
storage.save()

del storage.all()[key]
storage.save()
