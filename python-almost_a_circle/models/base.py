#!/usr/bin/python3
"""Defines a Base model class"""
import json


class Base:
    """
    Base model class.

    Attributes:
        __nb_objects (int): Counter for the number of instances of Base.

    Methods:
        __init__(self, id=None): Initializes a Base object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int): The ID of the object. If not provided, the ID is
            automatically assigned based on the current number of instances.

        Returns:
            None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: A JSON string representing the list of dictionaries. If the
                input list is None or empty, it returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved.

        Returns:
            None.
        """
        filename = "{}.json".format(cls.__name__)
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string to be converted.

        Returns:
            list: A list of dictionaries representing the JSON data. If the
                input string is None, it returns an empty list.
        """
        if json_string is None:
            return []
        return json.loads(json_string)
