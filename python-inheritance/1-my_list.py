#!/usr/bin/python3
"""Task 1"""


class MyList(list):
    """
    Subclass of the built-in list class.

    Inherits all the functionality of the list class.

    """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))
