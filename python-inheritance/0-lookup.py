#!/usr/bin/python3
"""Task 0"""


def lookup(obj):
    """
    Returns a list of attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings representing the attributes and
        methods of the object.

    """
    return list(dir(obj))
