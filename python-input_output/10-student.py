#!/usr/bin/python3
"""Task 10"""


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

    def to_json(self, attrs=None):
        """
        Converts the student object to a JSON serializable dictionary.

        Args:
            attrs (list, optional): A list of attribute names to include
            in the dictionary.
            If None, all attributes are included. Defaults to None.

        Returns:
            dict: A dictionary representation of the student object.

        """
        if attrs == None:
            return self.__dict__
        dic = {}
        for i in attrs:
            if i in self.__dict__:
                dic[i] = self.__dict__[i]
        return dic
