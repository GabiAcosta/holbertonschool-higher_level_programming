#!/usr/bin/python3
"""Task 9"""


class Student:
    """
    Class representing a student.

    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        Returns:
            None.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Converts the student object to a JSON serializable dictionary.

        Returns:
            dict: A dictionary representation of the student object.

        """
        return self.__dict__
