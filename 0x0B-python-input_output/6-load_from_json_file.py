#!/usr/bin/python3
"""
6-load_from_json_file.py
Module that defines a function called load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”

    Args:
        filename (str): The name of the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
