#!/usr/bin/python3
"""Task 0"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result as an integer.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default value is 98.

    Raises:
        TypeError: If either a or b is not an integer or float.
        OverflowError: If a is positive or negative infinity.

    Returns:
        int: The sum of a and b as an integer.
    """
    if a == float('inf') or a == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer.")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
