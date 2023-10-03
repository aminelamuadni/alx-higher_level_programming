#!/usr/bin/python3
"""
4-print_square.py

Function:
- print_square
"""


def print_square(size):
    """
    Prints a square with the character #

    Argument:
    - size (int): The size length of the square.

    Returns:
    None
    """

    # Check for type of size
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print("#" * size)

