#!/usr/bin/python3
"""Defines the TestFileStorage class"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittest for the FileStorage class"""
    def setUp(self) -> None:
        """Sets up for all the tests"""
        FileStorage._FileStorage__objects = {}

    def tearDown(self) -> None:
        """Cleans up after all tests have been carried out"""
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self) -> None:
        """Tests the all method of the FileStorage class"""
        testBase = BaseModel()
        self.assertDictEqual(FileStorage._FileStorage__objects, storage.all())


if __name__ == '__main__':
    unittest.main()
