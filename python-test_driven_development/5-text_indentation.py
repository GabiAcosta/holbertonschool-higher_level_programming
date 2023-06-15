#!/usr/bin/python3
"""Task 5"""


def text_indentation(text):
    """
    Prints the given text with proper indentation.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chrs = ".?:"
    for i in range(len(text)):
        if text[i] in chrs:
            print("{}".format(text[i]), end="")
            print()
            print()
        else:
            if text[i - 1] in chrs and text[i] == " ":
                continue
            print("{}".format(text[i]), end="")
