#!/usr/bin/python3
"""
This module contains the unit tests for the Square class.
"""


import os
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

    def test_square_to_dictionary(self):
        """
        Test the to_dictionary method of the Square class.
        """
        s1 = Square(5, 1, 2, 100)

        s1_dict = s1.to_dictionary()
        expected_dict = {'id': 100, 'size': 5, 'x': 1, 'y': 2}
        
        self.assertEqual(s1_dict, expected_dict)
        self.assertIsInstance(s1_dict, dict)

    def test_invalid_constructor_args(self):
        """
        Test invalid arguments provided to the Square constructor.
        """
        with self.assertRaises(TypeError):
            Square(1, "2")
        
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        
        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

        with self.assertRaises(ValueError):
            Square(0)

    def test_str_representation(self):
        """
        Test the __str__ method for the Square class.
        """
        s = Square(5, 1, 2, 99)
        self.assertEqual(str(s), "[Square] (99) 1/2 - 5")

    def test_to_dictionary_method(self):
        """
        Test the to_dictionary method of the Square class.
        """
        s = Square(5, 1, 2, 100)
        self.assertDictEqual(s.to_dictionary(), {'id': 100, 'size': 5, 'x': 1, 'y': 2})

    def test_save_to_file_with_empty_list(self):
        """
        Test the save_to_file class method when an empty list is provided.
        """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_valid_square(self):
        """
        Test the save_to_file class method with a valid Square instance.
        """
        s = Square(1)
        Square.save_to_file([s])

    def test_load_from_file_when_file_missing(self):
        """
        Test the load_from_file class method when the file doesn't exist.
        """
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        squares = Square.load_from_file()
        print(squares)
        self.assertEqual(squares, [])

    def test_load_from_file_when_file_exists(self):
        """
        Test the load_from_file class method when the file exists.
        """
        s = Square(1)
        Square.save_to_file([s])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)

if __name__ == "__main__":
    unittest.main()
