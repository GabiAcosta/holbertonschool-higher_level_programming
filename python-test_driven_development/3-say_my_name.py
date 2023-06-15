#!/usr/bin/python3
"""Task 3"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name with the provided first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))