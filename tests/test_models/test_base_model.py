#!/usr/bin/python3
"""Unitest for the BaseModel class"""
import unittest
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

    def test_str(self) -> None:
        """Tests the string representation of an object"""
        test_str = f"[{self.testBase.__class__.__name__}] ({self.testBase.id}) {self.testBase.__dict__}"
        self.assertEqual(test_str, str(self.testBase))

    def test_to_dict(self) -> None:
        """Tests to_dict() method of BaseModel has all the attributes required"""
        self.assertIn('__class__', self.testBase.to_dict().keys())
