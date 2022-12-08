#!/usr/bin/python3
"""unittest for the FileStorage class"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorge(unittest.TestCase):
    """Unittest for the FileStorage class"""
    def setUp(self) -> None:
        """SetUp for the tests"""
        self.test = FileStorage()

    def tearDown(self) -> None:
        """Cleans up after tests"""
        pass

    def test_all(self) -> None:
        """Test the all method of the FileStorage class"""
        self.assertDictEqual(storage.all(), FileStorage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
