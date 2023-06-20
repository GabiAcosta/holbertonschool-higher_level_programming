#!/usr/bin/python3
"""Task 7"""


class BaseGeometry:
    """
    Base class for geometry-related operations.

    Attributes:
        None

    Methods:
        area(): Raises an exception indicating that the method is not
        implemented.
        integer_validator(name, value): Validates that a value is an integer
        and greater than 0.

    """
    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Indicates that the method is not implemented.

        Returns:
            None

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            None

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
