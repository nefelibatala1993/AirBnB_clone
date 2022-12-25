#!/usr/bin/python3
"""Unitest for the BaseModel class"""
import unittest
import json
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines unittests for the BaseModel class"""
    def setUp(self) -> None:
        self.testBase = BaseModel()

    def test_save(self) -> None:
        """Tests save method of BaseModel when an object is saved"""
        t = self.testBase.updated_at
        self.testBase.save()
        self.assertLess(t, self.testBase.updated_at)

        # Check whether the object is stored in storage (__objects)
        key = self.testBase.__class__.__name__ + "." + self.testBase.id
        self.assertIn(key, storage.all())

        # Check if the object stored has the same content
        with open(storage._FileStorage__file_path, 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], self.testBase.to_dict())

    def test_str(self) -> None:
        """Tests the string representation of an object"""
        test_str = f"[{self.testBase.__class__.__name__}] ({self.testBase.id}) {self.testBase.__dict__}"
        self.assertEqual(test_str, str(self.testBase))

    def test_to_dict(self) -> None:
        """Tests to_dict() method of BaseModel has all the attributes required"""
        self.assertIn('__class__', self.testBase.to_dict().keys())

    def test_from_dict_to_obj(self) -> None:
        """Tests for when an object is created from a dictionary"""
        dict_s = self.testBase.to_dict()
        new = BaseModel(**dict_s)
        dict_n = new.to_dict()
        self.assertDictEqual(dict_s, dict_n)


if __name__ == '__main__':
    unittest.main()
