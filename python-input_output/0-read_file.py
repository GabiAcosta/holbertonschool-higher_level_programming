#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """
    Read and print the contents of a file.

    Args:
        filename (str): The name of the file to be read. Defaults to an
        empty string.

    Returns:
        None

    """
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print("{}".format(text))
