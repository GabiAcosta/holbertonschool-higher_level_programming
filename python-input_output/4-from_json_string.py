#!/usr/bin/python3
"""Task 4"""
import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string to an object.

    Args:
        my_str (str): The JSON-formatted string to be converted.

    Returns:
        object: The object represented by the JSON string.

    """
    return json.loads(my_str)
