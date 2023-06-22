#!/usr/bin/python3
"""Task 3"""
import json


def to_json_string(my_obj):
    """
    Convert an object to a JSON-formatted string.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: A JSON-formatted string representing the object.

    """
    return json.dumps(my_obj)
