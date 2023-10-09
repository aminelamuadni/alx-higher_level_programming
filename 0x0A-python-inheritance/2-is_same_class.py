#!/usr/bin/python3
"""
This module defines the is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
