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
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(2, 2)
        self.assertTrue(hasattr(s2, 'id'))
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)

        s3 = Square(3, 1, 3)
        self.assertTrue(hasattr(s3, 'id'))
        self.assertEqual(s3.size, 3)
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

    def test_square_update_args(self):
        """
        Test updating Square attributes using *args.
        """
        s1 = Square(5)

        s1.update(89)
        self.assertEqual(s1.id, 89)
        
        s1.update(90, 2)
        self.assertEqual(s1.id, 90)
        self.assertEqual(s1.size, 2)
        
        s1.update(91, 3, 1)
        self.assertEqual(s1.id, 91)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)

        s1.update(92, 4, 2, 3)
        self.assertEqual(s1.id, 92)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_square_update_kwargs(self):
        """
        Test updating Square attributes using **kwargs.
        """
        s2 = Square(1)

        s2.update(id=100)
        self.assertEqual(s2.id, 100)
        
        s2.update(id=101, size=7)
        self.assertEqual(s2.id, 101)
        self.assertEqual(s2.size, 7)
        
        s2.update(x=5, y=6, id=102)
        self.assertEqual(s2.x, 5)
        self.assertEqual(s2.y, 6)
        self.assertEqual(s2.id, 102)

        s2.update(z=10)
        self.assertFalse(hasattr(s2, 'z'))

    def test_square_update_mixed(self):
        """
        Test updating Square attributes using both *args and **kwargs.
        *args should have precedence.
        """
        s3 = Square(8)

        s3.update(200, 10, x=9, y=10)
        self.assertEqual(s3.id, 200)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 0)
        self.assertEqual(s3.y, 0)

if __name__ == "__main__":
    unittest.main()
