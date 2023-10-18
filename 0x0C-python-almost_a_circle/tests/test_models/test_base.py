#!/usr/bin/python3
"""
This module contains the unit tests for the Base class.
"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Defines the test cases for the Base class.
    """

    def setUp(self):
        """
        Resets the Base class private counter before each test.
        """
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Tests the ID assignment of the Base class."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_id_data_type(self):
        """Tests non-integer IDs."""
        b = Base("string_id")
        self.assertEqual(b.id, "string_id")

        b = Base(1.5)
        self.assertEqual(b.id, 1.5)

        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
