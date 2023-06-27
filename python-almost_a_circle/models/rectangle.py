#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from the Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: The x-coordinate of the rectangle's position.
            y: The y-coordinate of the rectangle's position.
            id (int): The ID of the rectangle. If not provided, the ID is
            automatically assigned based on the current number of instances.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If width or height is under or equals 0.
            ValueError: If x or y is under 0.

        Returns:
            None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate of the rectangle's position.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate of the rectangle's position.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints a visual representation of the rectangle.

        The rectangle is represented using '#' characters. The position of the
        rectangle is determined by the `x` and `y` attributes.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string representing the rectangle in the format:
        "[Rectangle] (<id>) <x>/<y> - <width>/<height>"
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: New values for the rectangle's attributes as positional
            arguments.
            **kwargs: New values for the rectangle's attributes as keyword
            arguments.
        """
        if args and len(args) != 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for arg, attr in zip(args, attrs):
                setattr(self, attr, arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.
        """
        return self.__dict__
