#!/usr/bin/python3
"""Defines ``TestBaseModel`` class
``TestBaseModel`` has unittests for the BaseModel class
"""
import unittest
import json
from os import path
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Defines unittests for the BaseModel class"""
    def setUp(self) -> None:
        """SetUp method for initializing my new Instance Object"""
        self.test_obj = BaseModel()
        self.test_obj.name = "My Test Model"
        self.test_obj.number = 89

    def test_initialized_instance(self):
        """Tests for BaseModel initialization"""
        self.assertIsInstance(self.test_obj.id, str)
        self.assertEqual(self.test_obj.name, "My Test Model")
        self.assertEqual(self.test_obj.number, 89)
        self.assertEqual(str(type(self.test_obj)),
                         "<class 'models.base_model.BaseModel'>")

    def test_id_is_str(self) -> None:
        """Tests whether the new ID of an object is a string
        not a UUID object"""
        self.assertIsInstance(self.test_obj.id, str)

    def test_datetime_created_and_updated_at(self) -> None:
        """Test whether the new objects created_at and updated_at
        attributes are datetime objects."""
        self.assertIsInstance(self.test_obj.created_at, datetime)
        self.assertIsInstance(self.test_obj.updated_at, datetime)

    def test_string_representation(self) -> None:
        """Test the string representation of an object by calling
        the __str__ method
        and also implicitly calling the method using print()"""
        str_repr = "[{}] ({}) {}".format(self.test_obj.__class__.__name__,
                                         self.test_obj.id,
                                         self.test_obj.__dict__)
        self.assertEqual(self.test_obj.__str__(), str_repr)

    def test_to_dict_saves_dates_in_iso_format(self) -> None:
        """Tests the to_dict method of an instance object"""
        dict_s = self.test_obj.to_dict()
        for k, v in self.test_obj.__dict__.items():
            if isinstance(self.test_obj.__dict__[k], datetime):
                self.assertEqual(datetime.fromisoformat(dict_s[k]), v)

    def test_created_at(self) -> None:
        """Tests the time for which an object is created at"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_updated_at(self) -> None:
        """Tests the updated_at attribute of an object"""
        t1 = self.test_obj.updated_at
        self.test_obj.save()
        t2 = self.test_obj.updated_at
        self.assertLess(t1, t2)

    def test_from_dict_to_instance(self) -> None:
        """Tests for an object created from a dictionary of keys that
        correspond to its attributes"""
        dict_s = self.test_obj.to_dict()
        my_model = BaseModel(dict_s)
        my_model_dict_s = my_model.to_dict()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertNotEqual(self.test_obj, my_model)
        self.assertNotEqual(dict_s, my_model_dict_s)


if __name__ == '__main__':
    unittest.main()
