#!/usr/bin/python3
"""
3-say_my_name.py module

Functions:
- say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'

    Arguments:
    - first_name (str): the first name to print
    - last_name (str, optional): the last name to print

    Returns:
    None
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
