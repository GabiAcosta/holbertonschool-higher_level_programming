#!/usr/bin/python3
"""Task 6"""
import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The object loaded from the JSON file.

    """
    with open(filename, encoding="utf-8") as f:
        json.load(f)
