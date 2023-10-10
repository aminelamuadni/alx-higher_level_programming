#!/usr/bin/python3
"""
1-write_file.py
Module that defines a function called write_file
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8) and returns the number
    of characters written

    Args:
        filename (str): The name of the file
        text (str): The text string to write to the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
