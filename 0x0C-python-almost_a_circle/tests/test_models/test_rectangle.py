#!/usr/bin/python3
"""
This module contains the unit tests for the Rectangle class.
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Defines the test cases for the Rectangle class.
    """

    def test_attribute_assignment(self):
        """Tests the attributes assignment of the Rectangle class."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Rectangle(2, 10, 1, 2, 12)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 12)

    def test_id_inheritance(self):
        """Tests the ID inheritance from the Base class."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id + 1, r2.id)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

if __name__ == "__main__":
    unittest.main()
