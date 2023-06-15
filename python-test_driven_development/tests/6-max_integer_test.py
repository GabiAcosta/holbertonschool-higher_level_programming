#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([10, 8, 15, 12, 6]), 15)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-100, -200, -50, -300]), -50)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 8, -15, 12, -6]), 12)
        self.assertEqual(max_integer([100, -200, 50, -300]), 100)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([10, 8, 15, 15, 6]), 15)
        self.assertEqual(max_integer([100, 200, 50, 200]), 200)

if __name__ == '__main__':
    unittest.main()
