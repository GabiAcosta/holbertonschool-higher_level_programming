#!/usr/bin/python3
"""Task 3"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance or a subclass of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance or subclass of the class,
        False otherwise.

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
