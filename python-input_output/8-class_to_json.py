#!/usr/bin/python3
"""Task 8"""


def class_to_json(obj):
    """
    Converts a Python object to a JSON serializable dictionary.

    Args:
        obj: The object to be converted.

    Returns:
        dict: A dictionary representation of the object that can be
        serialized to JSON.

    """
    return obj.__dict__
