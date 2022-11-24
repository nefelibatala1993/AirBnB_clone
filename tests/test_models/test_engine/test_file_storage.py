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
        self.test_model = BaseModel()

    def tearDown(self) -> None:
        """Cleans up the files created"""
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_file_path_is_str(self) -> None:
        """Tests the id the file path of the JSON is string"""
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_objects_stores_the_created_objects(self) -> None:
        """Tests objects stores the created objects in the dictionary"""
        key = self.test_model.__class__.__name__ + "." + self.test_model.id
        self.assertIn(key, storage._FileStorage__objects.keys())

    def test_all_returns_the_objects_dict(self) -> None:
        """
        Tests the all method of the FileStorage class if it
        returns the objects dictionary that holds the dictionary
        of all the objects created
        """
        self.assertDictEqual(storage.all(),
                             storage._FileStorage__objects)

    def test_save_when_an_object_is_created(self) -> None:
        """Tests the save method when an object is created"""
        test_base = BaseModel()
        storage.save()
        self.assertIn(test_base.__class__.__name__ + "." +
                      test_base.id, storage.all().keys())

    def test_reload_to_retrieve_objects_from_json_file(self) -> None:
        """Tests the reload method in the file storage class"""
        test_base = BaseModel()
        storage.save()
        storage.reload()
        self.assertIn(test_base.__class__.__name__ +
                      "." + test_base.id, storage.all().keys())

    def test_save(self) -> None:
        """Tests the save method with args supplied"""
        with self.assertRaises(TypeError):
            storage.save(self.test_model)

    def test_new_to_store_a_new_object(self) -> None:
        """Tests the new method of an object"""
        test_base = BaseModel()
        storage.save()
        storage.reload()
        self.assertIn(test_base.__class__.__name__ + "." + test_base.id,
                      storage.all().keys())


if __name__ == '__main__':
    unittest.main()
