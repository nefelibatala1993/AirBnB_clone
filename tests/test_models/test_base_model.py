#!/usr/bin/python3
"""Defines the Unittests for the BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittests for the BaseModel class"""
    def setUp(self) -> None:
        self.testBase = BaseModel()

    def test_instantiation(self) -> None:
        """Tests public instance attributes of a newly instantiated object"""
        self.assertTrue(hasattr(self.testBase, "id"))
        self.assertTrue(hasattr(self.testBase, "id"))
        self.assertTrue(hasattr(self.testBase, "id"))

    def test_id_is_string(self) -> None:
        """Tests if the id of an instance is a string"""
        self.assertIsInstance(self.testBase.id, str)

    def test_created_at(self) -> None:
        """Tests the created_at public instance attribute"""
        self.assertIsInstance(self.testBase.created_at, datetime)

    def test_updated_at(self) -> None:
        """Tests updated_at public instance attribute"""
        self.assertIsInstance(self.testBase.updated_at, datetime)

    def test_save(self) -> None:
        """Tests the save method of the BaseModel class"""
        t1 = self.testBase.updated_at
        self.testBase.save()
        t2 = self.testBase.updated_at
        self.assertLess(t1, t2)

    def test_str(self) -> None:
        """Tests the string representaion of an object"""
        str_rep = f"[{self.testBase.__class__.__name__}] "\
            f"({self.testBase.id}) {self.testBase.__dict__}"
        self.assertEqual(str(self.testBase), str_rep)

    def test_to_dict(self) -> None:
        """Tests the to_dict() method of the BaseModel class"""
        dict_s = self.testBase.__dict__
        dict_s['__class__'] = self.testBase.__class__.__name__
        for key, value in self.testBase.to_dict().items():
            if key == 'updated_at' or key == 'created_at':
                self.assertEqual(dict_s[key].isoformat(), value)
            else:
                self.assertEqual(dict_s[key], value)


if __name__ == '__main__':
    unittest.main()
