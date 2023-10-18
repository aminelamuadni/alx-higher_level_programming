#!/usr/bin/python3
"""
This module contains the unit tests for the Base class.
"""


import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string(self):
        """Tests the to_json_string method of the Base class."""

        self.assertEqual(Base.to_json_string([]), "[]")

        self.assertEqual(Base.to_json_string(None), "[]")

        list_dicts = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(json_str), list_dicts)

        self.assertIsInstance(json_str, str)

    def test_save_to_file(self):
        """Tests the save_to_file method of the Base class."""

        class MockClass(Base):
            def to_dictionary(self):
                return {"id": self.id}

        obj1 = MockClass()
        obj2 = MockClass()

        MockClass.save_to_file([obj1, obj2])

        self.assertTrue(os.path.isfile("MockClass.json"))

        with open("MockClass.json", "r") as file:
            content = json.load(file)
            expected = [{"id": 1}, {"id": 2}]
            self.assertEqual(content, expected)

        os.remove("MockClass.json")

    def test_from_json_string(self):
        """Tests the from_json_string method of the Base class."""

        self.assertEqual(Base.from_json_string('[]'), [])
        
        json_str = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}])

        self.assertEqual(Base.from_json_string(None), [])

        self.assertEqual(Base.from_json_string(""), [])

    def test_create(self):
        """Tests the create method of the Base class."""
        rect_dict = {"id": 1, "width": 4, "height": 5, "x": 0, "y": 0}
        r = Rectangle.create(**rect_dict)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)

        square_dict = {"id": 2, "size": 6}
        s = Square.create(**square_dict)
        self.assertEqual(s.size, 6)

    def test_load_from_file(self):
        """Tests the load_from_file method of the Base class."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.load_from_file(), [])

        r1 = Rectangle(4, 5, 0, 0, 1)
        r2 = Rectangle(6, 7, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)
        self.assertEqual(rectangles[0].width, 4)
        self.assertEqual(rectangles[0].height, 5)
        self.assertEqual(rectangles[1].width, 6)
        self.assertEqual(rectangles[1].height, 7)

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

if __name__ == "__main__":
    unittest.main()
