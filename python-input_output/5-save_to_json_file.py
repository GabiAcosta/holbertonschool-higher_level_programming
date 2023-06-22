#!/usr/bin/python3
"""Task 5"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj (object): The object to be saved to the JSON file.
        filename (str): The name of the file to save the object to.

    Returns:
        None

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
