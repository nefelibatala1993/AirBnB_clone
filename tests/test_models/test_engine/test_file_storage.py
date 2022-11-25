#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Unittest for the FileStorage class"""
    def setUp(self) -> None:
        """SetUp initialization for test cases"""
        self.test_obj = BaseModel()

    def test_all(self) -> None:
        """Tests the all method of an object
        """
        self.assertIsInstance(storage.all(), dict)
        with self.assertRaises(TypeError):
            storage.all(None)


if __name__ == '__main__':
    unittest.main()
