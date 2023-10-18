#!/usr/bin/python3
"""
This module contains the Base class which serves as the
"base" for all other classes in this project. The main
purpose of the Base class is to manage the `id` attribute
for all derived classes.
"""


class Base:
    """Base class for the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int, optional): The id of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
