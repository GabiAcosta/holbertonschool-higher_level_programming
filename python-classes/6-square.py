#!/usr/bin/python3
""" Task 6 """


class Square:
    """ Class that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Returns:
            None.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value (tuple): The position value to be set.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.

        Returns:
            None.
        """
        if not check_positive_tuple(value) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        if self.position[1] > 0:
            for _ in range(self.position[1]):
                print()
        for _ in range(self.size):
            for _ in range(self.position[0]):
                print(" ", end="")
            for _ in range(self.size):
                print("#", end="")
            print()


def check_positive_tuple(value):
    """
    Checks if a tuple contains positive integers.

    Args:
        value (tuple): The tuple to be checked.

    Returns:
        bool: True if the tuple contains positive integers, False otherwise.
    """
    if not isinstance(value, tuple):
        return False
    for elem in value:
        if not isinstance(elem, int) or elem < 0:
            return False
    return True
