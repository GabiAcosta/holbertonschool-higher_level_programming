#!/usr/bin/python3
"""Task 4"""


def inherits_from(obj, a_class):
    """
    Checks if an object is a subclass of a specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is a subclass of the class, False otherwise.

    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
