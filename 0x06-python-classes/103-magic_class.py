#!/usr/bin/python3
"""
This module defines the MagicClass which calculates the area and
circumference based on a given radius.
"""

import math


class MagicClass:
    """
    Represents a MagicClass which calculates area and circumference
    for a given radius.
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass instance.

        Args:
            radius (int or float): The radius of the MagicClass. Default is 0.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the MagicClass.

        Returns:
            The area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the MagicClass.

        Returns:
            The circumference.
        """
        return 2 * math.pi * self.__radius
