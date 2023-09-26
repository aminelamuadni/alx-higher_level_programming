#!/usr/bin/python3
"""
This module contains the definition of the class 'Square'.

The Square class has a private attribute 'size' and a method to compute its area.
"""


class Square:
    """
    A representation of a square.

    Attributes:
        __size (int): Size of the square, it's a private attribute.
    """

    def __init__(self, size=0):
        """
        Initialize the Square instance with size value.

        Args:
            size (int): Size of the square, default is 0.
        """
        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Check if size is a non-negative integer
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size
