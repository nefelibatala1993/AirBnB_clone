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

    def tearDown(self) -> None:
        """Cleans up after all tests"""
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self) -> None:
        """Tests the all method of an object
        """
        self.assertIsInstance(storage.all(), dict)
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self) -> None:
        """Tests the new method of when an object is created"""
        test_base = BaseModel()
        key = type(test_base).__name__ + "." + test_base.id
        FileStorage._FileStorage__objects = {}
        storage.new(test_base)
        dict_s = storage.all()
        self.assertIn(key, dict_s.keys())


if __name__ == '__main__':
    unittest.main()
