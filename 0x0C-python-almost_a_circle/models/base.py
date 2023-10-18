#!/usr/bin/python3
"""
This module contains the Base class which serves as the
"base" for all other classes in this project. The main
purpose of the Base class is to manage the `id` attribute
for all derived classes.
"""


import turtle
import csv
import json


class Base:
    """Base class for the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int, optional): The id of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(cls.__name__ + ".json", 'w') as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation `json_string`.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: A list of dictionaries represented by `json_string`.
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set from the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise Exception("Unknown class")

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file.
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()

            list_of_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_of_dicts]

        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the objects' data to a CSV file specific to the class.

        Args:
            list_objs (list): A list of objects to be serialized to a CSV file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads objects' data from a CSV file specific to the class.

        Returns:
            list: A list of objects loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        objs = []

        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        objs.append(
                            cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[4]),
                                int(row[0])
                            )
                        )
                    elif cls.__name__ == "Square":
                        objs.append(
                            cls(
                                int(row[1]),
                                int(row[2]),
                                int(row[3]),
                                int(row[0])
                            )
                        )

            return objs
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Open a window to draw Rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): Rectangles to draw.
            list_squares (list): Squares to draw.
        """

        screen = turtle.Screen()
        screen.bgcolor("white")
        t = turtle.Turtle()
        t.speed(5)

        def draw_shape(rect):
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.color("blue")
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                if rect.__class__.__name__ == "Rectangle":
                    t.forward(rect.height)
                elif rect.__class__.__name__ == "Square":
                    t.forward(rect.size)
                t.left(90)

        for rect in list_rectangles:
            draw_shape(rect)

        for square in list_squares:
            draw_shape(square)

        turtle.mainloop()
