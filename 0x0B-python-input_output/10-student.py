#!/usr/bin/python3
"""
10-student.py
Module that defines a class called Student
"""


class Student:
    """
    A class that defines a Student with some basic attributes and methods
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): List of strings for attribute names to retrieve

        Returns:
            dict: A dictionary representation of the Student instance
        """
        if attrs is None:
            return vars(self)
        else:
            return {key: value for key, value in vars(self).items()
                    if key in attrs}
