#!/usr/bin/python3
"""
100-my_int module
Contains the MyInt class that inherits from int
"""


class MyInt(int):
    """A class that inverts == and != operators"""

    def __eq__(self, other):
        """Override the equality operator to return not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the not equal operator to return equal"""
        return super().__eq__(other)
