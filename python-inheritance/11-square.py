#!/usr/bin/python3
"""Task 11"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(size): Initializes a square with the given size.
        area(): Calculates the area of the square.

    """
    def __init__(self, size):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of the square.

        Returns:
            None

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a description of the square.

        Returns:
            str: A string representation of the square object in the format
            "[Square] <width>/<height>".

        """
        return "[Square] {}/{}".format(self.__size, self.__size)
