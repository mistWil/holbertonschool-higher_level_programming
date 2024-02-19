import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_init_without_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_multiple_instances(self):
        obj2 = Base()
        obj3 = Base()
        obj4 = Base()
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)
        self.assertEqual(obj4.id, 4)

if __name__ == '__main__':
    unittest.main()