#!/usr/bin/python3
"""
9-rectangle module
Contains the Rectangle class that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        """Initialize the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
