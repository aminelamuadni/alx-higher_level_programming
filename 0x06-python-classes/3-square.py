#!/usr/bin/python3
"""
Definition of the class 'Square' with a private attribute 'size' and a method
to compute its area.
"""


class Square:
    """
    A representation of a square.

    Attributes:
        __size (int): Size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize the Square with an optional size.

        Args:
            size (int): Size of the square. Default is 0.
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
