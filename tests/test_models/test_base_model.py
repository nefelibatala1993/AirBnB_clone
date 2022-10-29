#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.my_model = BaseModel()

    def test_id_is_a_string(self):
        """`id` class attribute must be stored in a string format"""
        self.assertIsInstance(self.my_model.id, str)

    def test_created_at_updated_at(self):
        """`created_at` and `updated_at` class attributes must be of
            type datetime.
        """
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.created_at, datetime)

    def test_to_dict_formats_dates_with_iso_format(self):
        """to_dict should store dates in ISO format"""

        temp_dict = self.my_model.to_dict()
        for k, v in self.my_model.__dict__.items():
            if isinstance(self.my_model.__dict__[k], datetime):
                self.assertEqual(datetime.fromisoformat(temp_dict[k]), v)


if __name__ == '__main__':
    unittest.main()
