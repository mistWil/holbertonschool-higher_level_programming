#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_integer(self):
        self.assertEqual(max_integer([8]), 8)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([8, 4, 1]), 8)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([2, 9, 22, 7, 6]), 22)

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 4, 8]), 8)
        self.assertEqual(max_integer([2, 9, 6, 7, 22]), 22)
        self.assertEqual(max_integer([-1, -5, -4]), -1)

    def test_string_list(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')


if __name__ == '__main__':
    unittest.main()