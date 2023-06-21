#!/usr/bin/python3
"""Task 9"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(width, height): Initializes a rectangle with the given width
        and height.

    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Returns:
            None

        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a description of the reactangle.

        Returns:
            str: A string representation of the rectangle object in the format
            "[Rectangle] <width>/<height>".

        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
