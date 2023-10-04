#!/usr/bin/python3
"""
5-text_indentation.py

Function:
- text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Argument:
    - text (str): The text to be indented.

    Returns:
    None
    """

    # Check for valid text
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Indent the text
    start_idx = 0
    for idx, char in enumerate(text):
        if char in ".?:":
            print(text[start_idx:idx + 1].strip(), end="\n")
            start_idx = idx + 1
    if start_idx < len(text):
        print(text[start_idx:].strip(), end="")

