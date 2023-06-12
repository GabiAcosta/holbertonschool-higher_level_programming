#!/usr/bin/python3
""" Task 3 """


class Square:
    """ Class that defines a square """

    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.

        Returns:
            None.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        
    def area(self):
        """
        Calculates the area of the square.

        Returns:
            Returns the current square area.

        """
        return self.__size * self.__size
