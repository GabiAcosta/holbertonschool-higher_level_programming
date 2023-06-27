#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The ID of the square. If not provided, the ID is
            automatically assigned based on the current number of instances.

        Returns:
            None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representing the square in the format:
        "[Square] (<id>) <x>/<y> - <size>"
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args: New values for the square's attributes as positional
            arguments.
            **kwargs: New values for the square's attributes as keyword
            arguments.
        """
        if args and len(args) != 0:
            attrs = ['id', 'size', 'x', 'y']
            for arg, attr in zip(args, attrs):
                setattr(self, attr, arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.height,
            "y": self.y
        }
