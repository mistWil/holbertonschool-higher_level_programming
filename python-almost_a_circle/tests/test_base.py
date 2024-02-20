#!/usr/bin/python3


import unittest
import os
from models.base import Base

class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_readme_exists_and_not_empty(self):
        """Test if README.md exists and is not empty."""
        self.assertTrue(os.path.isfile("README.md") and os.path.getsize("README.md") > 0)

    def test_assign_auto_id(self):
        """Test automatic assignment of ID."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_assign_auto_id_increment(self):
        """Test automatic assignment of ID incrementing."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_assign_specific_id(self):
        """Test assignment of specific ID."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_empty_list(self):
        """Test to_json_string with empty list."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with list of dictionaries."""
        json_str = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_str, '[{"id": 12}]')

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        lst = Base.from_json_string(None)
        self.assertEqual(lst, [])

    def test_from_json_string_empty_string(self):
        """Test from_json_string with empty string."""
        lst = Base.from_json_string("[]")
        self.assertEqual(lst, [])

    def test_from_json_string_list(self):
        """Test from_json_string with JSON string."""
        lst = Base.from_json_string('[{"id": 89 }]')
        self.assertEqual(lst, [{"id": 89}])

if __name__ == '__main__':
    unittest.main()
