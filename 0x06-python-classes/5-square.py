#!/usr/bin/python3
"""
Square class with controlled access to the private attribute 'size'.
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
        self.size = size

    @property
    def size(self):
        """
        Getter for size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size.

        Args:
            value (int): Size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the # character.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
