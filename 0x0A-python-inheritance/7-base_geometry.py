#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class named BaseGeometry with two methods: area and integer_validator.
    """

    def area(self):
        """
        Method to compute the area, not yet implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to validate value:
        - <name> must be an integer.
        - <name> must be greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
