#!/usr/bin/python3
"""Defines the TestFileStorage class"""
import unittest
import os
import json
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

    def test_instantiation(self) -> None:
        """Tests for an instantiation of a FileStorage object"""
        testFileStorage = FileStorage()
        self.assertIsInstance(testFileStorage, FileStorage)
        self.assertTrue(hasattr(testFileStorage, "all"))
        self.assertTrue(hasattr(testFileStorage, "save"))
        self.assertTrue(hasattr(testFileStorage, "reload"))
        self.assertTrue(hasattr(testFileStorage, "new"))


    def test_all(self) -> None:
        """Tests the all method of the FileStorage class"""
        testBase = BaseModel()
        self.assertDictEqual(FileStorage._FileStorage__objects, storage.all())

    def test_save(self) -> None:
        """Tests the save method of the FileStorage class"""
        testBase = BaseModel()
        key = testBase.__class__.__name__ + "." + testBase.id
        json_dict = {}
        testBase.save()

        # TODO: Check whether the file has been created and if so if it
        #       contains the new object that has been created.
        if os.path.isfile(FileStorage._FileStorage__file_path):
            with open(FileStorage._FileStorage__file_path, 'r') as f:
                json_dict = json.load(f)
        self.assertIn(key, json_dict)

    def test_new(self) -> None:
        """Tests the new method of the FileStorage class"""
        testBase = BaseModel()
        key = testBase.__class__.__name__ + "." + testBase.id

        # TODO: Clean the __objects attribute because it will store the
        #       object once the object is created (the new method is called
        #       by a new instance when it is created), and check whether the
        #       __object is empty
        FileStorage._FileStorage__objects = {}
        self.assertDictEqual(FileStorage._FileStorage__objects, {})

        # TODO: Store the object by calling the new method on the storage
        #       object, to check whether the object is stored in the dict
        #       __objects
        storage.new(testBase)
        self.assertIn(key, FileStorage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
