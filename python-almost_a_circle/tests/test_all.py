import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """Unit tests for the Base class."""

    def test_auto_assign_id(self):
        """Test automatic assignment of ID."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_auto_assign_id_increment(self):
        """Test automatic assignment of ID incrementing."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_assigned_id(self):
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

class TestRectangle(unittest.TestCase):
    """Unit tests for the Rectangle class."""

    def test_rectangle_exists(self):
        """Test if Rectangle class exists."""
        self.assertTrue(hasattr(Rectangle, "__init__"))

    # Ajoutez d'autres tests pour les autres cas demandés...

class TestSquare(unittest.TestCase):
    """Unit tests for the Square class."""

    def test_square_exists(self):
        """Test if Square class exists."""
        self.assertTrue(hasattr(Square, "__init__"))

    # Ajoutez d'autres tests pour les autres cas demandés...

if __name__ == '__main__':
    unittest.main()
