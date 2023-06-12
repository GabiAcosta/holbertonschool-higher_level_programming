#!/usr/bin/python3
""" Task 4 """


class Square:
    """ Class that defines a square """

    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.

        Returns:
            None.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The size value to be set.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.

        Returns:
            None.
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            Returns the current square area.

        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a square pattern using the '#' character.

        Returns:
            None.
        """
        if self.size == 0:
            print("")
        for _ in range(self.size):
            for _ in range(self.size):
                print("#", end="")
            print()
