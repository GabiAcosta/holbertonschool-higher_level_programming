#!/usr/bin/python3
"""Task 2"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the class, False otherwise.

    """
    if type(obj) is a_class:
        return True
    else:
        return False
