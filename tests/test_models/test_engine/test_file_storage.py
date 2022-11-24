#!/usr/bin/python3
"""Defines the TestFileStorage class"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Performs unittests for the FileStorage class"""
    def setUp(self) -> None:
        """Setup method for Initializing a new Instance Object"""
        self.test_obj = FileStorage()
        self.test_model = BaseModel()

    def tearDown(self) -> None:
        """Cleans up the files created"""
        if os.path.isfile(self.test_obj._FileStorage__file_path):
            os.remove(self.test_obj._FileStorage__file_path)

    def test_file_path_is_str(self) -> None:
        """Tests the id the file path of the JSON is string"""
        self.assertIsInstance(self.test_obj._FileStorage__file_path, str)

    def test_objects_stored_is_a_dict(self) -> None:
        """Tests the dictionary which stored the objects"""
        self.assertIsInstance(self.test_obj._FileStorage__objects, dict)

    def test_all_returns_the_objects_dict(self) -> None:
        """
        Tests the all method of the FileStorage class if it
        returns the objects dictionary that holds the dictionary
        of all the objects created
        """
        dicts = self.test_obj._FileStorage__objects
        self.assertEqual(self.test_obj.all(), dicts)


if __name__ == '__main__':
    unittest.main()
