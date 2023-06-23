#!/usr/bin/python3
"""Task 12"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to a specified number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return list()
    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        prev_row = triangle[-1]
        for i in range(len(prev_row) - 1):
            row.append(prev_row[i] + prev_row[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
