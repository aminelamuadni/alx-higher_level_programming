#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_sorted(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_sorted_descending(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_identical(self):
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_single_item(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mix_negatives_and_positives(self):
        self.assertEqual(max_integer([-1, -2, 3, 4]), 4)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()

