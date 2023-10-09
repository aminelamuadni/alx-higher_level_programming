#!/usr/bin/python3
"""
This module defines the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class; otherwise False.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or is an instance of a 
              subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
