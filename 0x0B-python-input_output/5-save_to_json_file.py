#!/usr/bin/python3
"""
5-save_to_json_file.py
Module that defines a function called save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to write to the file
        filename (str): The name of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
