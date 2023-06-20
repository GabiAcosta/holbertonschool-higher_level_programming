#!/usr/bin/python3
"""Task 6"""


class BaseGeometry:
    """
    Base class for geometry-related operations.

    Attributes:
        None

    Methods:
        area(): Raises an exception indicating that the method is not
        implemented.

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
