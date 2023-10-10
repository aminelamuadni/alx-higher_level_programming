#!/usr/bin/python3
"""
This module contains a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The new string to insert after the search string.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)
            i += 1  # Skip the next line since we just added it
        i += 1

    with open(filename, 'w') as f:
        f.writelines(lines)
