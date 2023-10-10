#!/usr/bin/python3
"""
2-append_write.py
Module that defines a function called append_write
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8) and returns
    the number of characters added

    Args:
        filename (str): The name of the file
        text (str): The text string to append to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
