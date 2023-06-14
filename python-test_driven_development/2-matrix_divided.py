#!/usr/bin/python3
"""Task 2"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and returns the result.

    Args:
        matrix (list): The matrix to be divided. Must be a list of lists of
        integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats
        or if div is not a number.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (int or float)
        ZeroDivisionError: If div is equal to zero.

    Returns:
        list: The new matrix with the elements divided by div.
    """
    size = len(matrix[0])
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)
    for row in matrix:
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError(error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_element = []
        for col in row:
            new_element.append(round(col / div, 2))
        new_matrix.append(new_element)
    return new_matrix
