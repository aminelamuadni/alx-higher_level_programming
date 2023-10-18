#!/usr/bin/python3
"""
This module contains the Rectangle class which inherits
from the Base class and represents a rectangle.
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.__attribute_validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.__attribute_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.__attribute_validation("x", value, False)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.__attribute_validation("y", value, False)
        self.__y = value

    def __attribute_validation(self, name, value, is_size=True):
        """Private method to validate attribute values."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if is_size and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif not is_size and value < 0:
            raise ValueError("{} must be >= 0".format(name))
