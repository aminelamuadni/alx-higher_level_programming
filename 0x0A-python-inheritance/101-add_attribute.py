#!/usr/bin/python3
"""
101-add_attribute module
Contains the add_attribute function that adds a new attribute to an object
if possible
"""


def add_attribute(obj, attr_name, value):
    """Adds a new attribute to an object if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, value)
