#!/usr/bin/python3
"""Defines the TestFileStorage class"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittest for the FileStorage class"""
    def setUp(self) -> None:
        """Sets up for all the tests"""
        pass

    def test_all(self) -> None:
        """Tests the all method of the FileStorage class"""
        self.assertDictEqual(FileStorage._FileStorage__objects, storage.all())


if __name__ == '__main__':
    unittest.main()
