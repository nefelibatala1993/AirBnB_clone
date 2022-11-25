#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import json
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
        dict_s = FileStorage._FileStorage__objects
        self.assertIsInstance(storage.all(), dict)
        self.assertDictEqual(dict_s, storage.all())
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self) -> None:
        """Tests the new method of when an object is created"""
        key = type(self.test_obj).__name__ + "." + self.test_obj.id
        FileStorage._FileStorage__objects = {}
        storage.new(self.test_obj)
        dict_s = storage.all()
        self.assertIn(key, dict_s.keys())
        with self.assertRaises(AttributeError):
            storage.new(98)
            storage.new(None)

    def test_save(self) -> None:
        """Tests the save method when the object are stored in JSON file"""
        key = type(self.test_obj).__name__ + "." + self.test_obj.id
        storage.save()
        with open(FileStorage._FileStorage__file_path, "r") as f:
            dict_t = json.load(f)
        self.assertIn(key, dict_t.keys())

    def test_reload(self) -> None:
        """Tests the reload method to retrieve object from storage"""
        key = type(self.test_obj).__name__ + "." + self.test_obj.id
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        dict_s = storage.all()
        self.assertIn(key, dict_s.keys())

    def test_reload_if_no_file_present(self) -> None:
        """Tests reload when no file is present"""
        empty_dict = {}
        storage.save()
        FileStorage._FileStorage__objects = {}
        os.remove(FileStorage._FileStorage__file_path)
        storage.reload()
        dict_s = storage.all()
        self.assertEqual(dict_s, empty_dict)


if __name__ == '__main__':
    unittest.main()
