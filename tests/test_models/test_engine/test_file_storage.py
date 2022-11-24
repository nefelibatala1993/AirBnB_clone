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

    def test_save(self) -> None:
        """Tests save method from FileStorage"""
        self.test_file.new(self.test_base)
        dict_s = self.test_file.all()
        self.test_file.save()
        self.test_file.reload()
        dict_t = self.test_file.all()
        self.assertDictEqual(dict_s, dict_t)

    def test_reload_empty(self) -> None:
        """Tests an empty reload from non-existent JSON file"""
        self.test_file.new(self.test_base)
        self.test_file.save()
        dict_s = self.test_file.all()
        os.remove("test.json")
        self.test_file.reload()
        dict_t = self.test_file.all()
        self.assertEqual(dict_s, dict_t)

    def test_all_if_no_object_is_retrieved(self) -> None:
        """Tests when an empty JSON file is used to retrieve objects from storage"""
        FileStorage._FileStorage__objects = {}
        dict_s = self.test_file.all()
        self.assertEqual(dict_s, {})


if __name__ == '__main__':
    unittest.main()
