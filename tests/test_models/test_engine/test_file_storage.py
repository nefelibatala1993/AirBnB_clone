#!/usr/bin/python3
"""Defines the TestFileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Performs unittests for the FileStorage class"""
    def setUp(self) -> None:
        """Setup method for Initializing a new Instance Object"""
        with open("test.json", "w", encoding="utf-8"):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}
        self.test_file = FileStorage()
        self.test_base = BaseModel()

    def tearDown(self) -> None:
        """Cleans up the files created"""
        FileStorage.__FileStorage__file_path = "file.json"
        if os.path.isfile("test.json"):
            os.remove("test.json")

    def test_all(self) -> None:
        """Test all method from FileStorage"""
        self.assertIsInstance(self.test_file.all(), dict)

    def test_storage(self) -> None:
        """Tests storage object"""
        self.assertIsInstance(storage, FileStorage)


if __name__ == '__main__':
    unittest.main()
