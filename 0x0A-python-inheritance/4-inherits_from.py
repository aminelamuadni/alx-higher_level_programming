#!/usr/bin/python3
"""
This module contains the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class inherited from a_class.

    Args:
    obj (Any): The object to check.
    a_class (type): The reference class.

    Returns:
    bool: True if obj is an instance of a class that inherited from a_class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
