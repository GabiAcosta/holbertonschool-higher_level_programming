#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """
    Append text to a file.

    If the file does not exist, it will be created.

    Args:
        filename (str): The name of the file to which the text will be appended
        Defaults to an empty string.
        text (str): The text to be appended to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.

    """
    with open(filename, 'a', encoding="utf-8") as f:
        chr_written = f.write(text)
        return chr_written
