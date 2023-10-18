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

    def test_size_getter(self):
        """
        Test cases for the size getter.
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        
        s2 = Square(3, 2)
        self.assertEqual(s2.size, 3)

    def test_size_setter(self):
        """
        Test cases for the size setter.
        """
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_square_creation(self):
        """
        Test cases for the creation of squares and
        their string representations.
        """
        s1 = Square(5)
        self.assertTrue(hasattr(s1, 'id'))
        self.assertEqual(s1.size, 5)

        s2 = Square(2, 2)
        self.assertTrue(hasattr(s2, 'id'))
        self.assertEqual(s2.size, 2)

        s3 = Square(3, 1, 3)
        self.assertTrue(hasattr(s3, 'id'))
        self.assertEqual(s3.size, 3)

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
