#!/usr/bin/python3
"""Defines a Base model class"""


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
