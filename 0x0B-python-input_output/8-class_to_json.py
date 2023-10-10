#!/usr/bin/python3
"""
8-class_to_json.py
Module that defines a function called class_to_json
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object

    Args:
        obj: instance of a Class
    """
    return vars(obj)
