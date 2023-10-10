#!/usr/bin/python3
"""
3-to_json_string.py
Module that defines a function called to_json_string
"""


import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)

    Args:
        my_obj: The object to convert
    """
    return json.dumps(my_obj)
