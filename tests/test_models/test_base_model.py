#!/usr/bin/python3
"""Unitest for the BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines unittests for the BaseModel class"""
    def setUp(self) -> None:
        self.testBase = BaseModel()

    def test_str(self) -> None:
        """Tests the string representation of an object"""
        test_str = f"[{self.testBase.__class__.__name__}] ({self.id}) {self.__dict__}"
