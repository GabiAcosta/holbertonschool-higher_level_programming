#!/usr/bin/python3
"""Task 7"""


class Rectangle:
    """
    Class that defines a rectangle.

    Attributes:
        number_of_instances (int): The number of instances of the
        Rectangle class.
        print_symbol (str): The symbol used for printing the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Returns:
            None.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.

        Returns:
            None.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle, where by default '#'
            represents the rectangle's width and height. If print_symbol is
            changed, the new symbol will represent the rectangle.

            If the width or height is 0, an empty string is returned.

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for height in range(self.__height):
            for _ in range(self.__width):
                rectangle += str(self.print_symbol)
            if height != self.__height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """
        Returns a string representation of the rectangle object.

        Returns:
            str: A string representation of the rectangle object in the format
            "Rectangle(width, height)".

        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a farewell message when the rectangle object is deleted.

        Returns:
            None.

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
