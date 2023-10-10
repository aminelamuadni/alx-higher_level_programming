#!/usr/bin/python3
"""
11-student.py
Module that defines a class called Student
"""


class Student:
    """
    Defines a Student with attributes and methods
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
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
            dict: Dictionary representation of the Student instance
        """
        if attrs is None:
            return vars(self)
        else:
            return {key: value for key, value in vars(self).items()
                    if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
            json (dict): Dictionary representation of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
