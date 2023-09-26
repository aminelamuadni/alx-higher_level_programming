#!/usr/bin/python3
"""
Square class with attributes size, position and a print method.
"""


class Square:
    """
    A representation of a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square instance.
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
        """
        if (not isinstance(value, tuple) or len(value) != 2 or 
            not isinstance(value[0], int) or not isinstance(value[1], int) or 
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """
        Return the area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square.
        """
        print(self.__str__())

    def __str__(self):
        """
        Return string representation of the square for print().
        """
        if self.__size == 0:
            return ""

        result = "\n" * self.__position[1]
        for i in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            if i < self.__size - 1:
                result += "\n"
        return result
