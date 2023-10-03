#!/usr/bin/python3

"""
Module for defining a rectangle.

This module provides functionalities related to a rectangle, including
properties like width, height, and methods to calculate area, perimeter, 
and its string representation.
"""


class Rectangle:
    """Class that defines a rectangle.

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with given width and height.

        Args:
            width (int, optional): width of the rectangle.
            height (int, optional): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return the official string representation of the rectangle."""
        return "{} whitespace before '{}'".format(self.__width, self.__height)
