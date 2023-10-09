#!/usr/bin/python3
"""
10-square module
Contains the Square class that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size):
        """Initialize the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
