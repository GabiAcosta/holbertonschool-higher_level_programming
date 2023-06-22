#!/usr/bin/python3
"""Task 8"""
import json


def class_to_json(obj):
    """
    Converts a Python object to a JSON string representation.

    Args:
        obj: The object to be converted.

    Returns:
        str: A JSON string representation of the object.

    """
    return json.dumps(obj.__dict__)
