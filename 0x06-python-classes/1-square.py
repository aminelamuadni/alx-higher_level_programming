#!/usr/bin/python3
"""
This module contains the definition of the class 'Square'.

The Square class has a private attribute 'size'.
"""


class Square:
    """
    A representation of a square.

    Attributes:
        __size (int): Size of the square, it's a private attribute.
    """

    def __init__(self, size):
        """
        Initialize the Square instance with size value.

        Args:
            size (int): Size of the square.
        """
        self.__size = size
