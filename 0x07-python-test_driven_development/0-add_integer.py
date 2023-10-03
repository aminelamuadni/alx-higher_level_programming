#!/usr/bin/python3
"""
This module provides a function to add two numbers.

The function can accept integers or floats but will
return the result as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
    a (int/float): the first number.
    b (int/float, optional): the second number. Defaults to 98.

    Returns:
    int: The sum of a and b, casted to an integer.

    Raises:
    TypeError: If a or b are not int or float.
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

