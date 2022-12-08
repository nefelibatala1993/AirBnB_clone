#!/usr/bin/python3
"""unittest for the FileStorage class"""
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorge(unittest.TestCase):
    """Unittest for the FileStorage class"""
    def setUp(self) -> None:
        """SetUp for the tests"""
        pass

    def tearDown(self) -> None:
        """Cleans up after tests"""
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self) -> None:
        """Test the all method of the FileStorage class"""
        dict_s = storage.all()
        self.assertIsInstance(dict_s, dict)

    def test_save(self) -> None:
        """Tests the save method of the FileStorage class"""
        test_base = BaseModel()
        storage.save()
        self.assertTrue(FileStorage._FileStorage__file_path)

    def test_new(self):
        test_base = BaseModel()
        key = test_base.__class__.__name__ + "." +  test_base.id
        FileStorage._FileStorage__objects = {}
        storage.new(test_base)
        self.assertIn(key, FileStorage._FileStorage__objects.keys())



if __name__ == '__main__':
    unittest.main()
