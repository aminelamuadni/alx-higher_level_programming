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

    def test_type_validation(self):
        """Tests the type validation of the attributes."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}

    def test_value_validation(self):
        """Tests the value validation of the attributes."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(10, 0)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(10, 2, -1, 0)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Tests the area method of the Rectangle class."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

        r2 = Rectangle(3, 5)
        self.assertEqual(r2.area(), 15)

        r3 = Rectangle(8, 7)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Tests the display method of the Rectangle class."""
        r1 = Rectangle(4, 6)
        r2 = Rectangle(2, 2)

        expected_output1 = "####\n" * 6
        expected_output2 = "##\n" * 2

        temp_stdout = StringIO()
        sys.stdout = temp_stdout
        r1.display()
        output = temp_stdout.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, expected_output1)

        temp_stdout = StringIO()
        sys.stdout = temp_stdout
        r2.display()
        output = temp_stdout.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, expected_output2)

    def test_str(self):
        """Tests the __str__ method of the Rectangle class."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)

        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

if __name__ == "__main__":
    unittest.main()
