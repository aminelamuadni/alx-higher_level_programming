#!/usr/bin/python3
"""
This module defines the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is instance of, or inherited from, a specified class.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or is an instance of a
              subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
