#!/usr/bin/python3
"""
Square class with attributes size and position.
"""


class Square:
    """
    A representation of a square.

    Attributes:
        __size (int): Size of the square.
        __position (tuple): Position of the square in 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square with optional size and position.

        Args:
            size (int): Size of the square. Default is 0.
            position (tuple): 2D coordinates of the square. Default is (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position.

        Args:
            value (tuple): 2D coordinates of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square considering its position.
        """
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
