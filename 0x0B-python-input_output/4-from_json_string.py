#!/usr/bin/python3
"""
4-from_json_string.py
Module that defines a function called from_json_string
"""


import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure) represented by a
    JSON string

    Args:
        my_str: The JSON string to convert
    """
    return json.loads(my_str)
