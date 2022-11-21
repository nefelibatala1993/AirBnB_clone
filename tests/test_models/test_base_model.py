#!/usr/bin/python3
"""Defines ``TestBaseModel`` class

``TestBaseModel`` has unittests for the BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Defines unittests for the BaseModel class"""
    def setUp(self) -> None:
        """SetUp method for initializing my new Instance Object"""
        self.test_obj = BaseModel()

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


if __name__ == '__main__':
    unittest.main()