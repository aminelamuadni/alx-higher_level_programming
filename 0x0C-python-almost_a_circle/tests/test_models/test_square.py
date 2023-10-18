#!/usr/bin/python3
"""
This module contains the unit tests for the Square class.
"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Defines the test cases for the Square class.
    """

    def test_square_creation(self):
        """
        Test cases for the creation of squares and
        their string representations.
        """
        s1 = Square(5)
        self.assertTrue(hasattr(s1, 'id'))
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(2, 2)
        self.assertTrue(hasattr(s2, 'id'))
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)

        s3 = Square(3, 1, 3)
        self.assertTrue(hasattr(s3, 'id'))
        self.assertEqual(s3.width, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)

    def test_square_area(self):
        """
        Test cases for the computation of the area of squares.
        """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

if __name__ == "__main__":
    unittest.main()
