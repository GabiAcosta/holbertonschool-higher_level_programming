#!/usr/bin/python3
"""Task 1"""


def write_file(filename="", text=""):
    """
    Write text to a file.

    Args:
        filename (str): The name of the file to be written. Defaults to an
        empty string.
        text (str): The text to be written to the file. Defaults to an
        empty string.

    Returns:
        int: The number of characters written to the file.

    """
    with open(filename, 'w', encoding="utf-8") as f:
        chr_written = f.write(text)
        return chr_written
