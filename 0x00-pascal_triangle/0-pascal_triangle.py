#!/usr/bin/python3

"""
This module generates Pascal's Triangle for a given number of rows `n`.
Pascal's Triangle is a triangular array of binomial coefficients where each
number is the sum of the two directly above it.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to `n` rows.

    Args:
    n (int): The number of rows in the Pascal's Triangle to generate.
    Must be a non-negative integer.

    Returns:
    list: A list of lists, where each sublist represents a row
    of Pascal's Triangle.
    If n <= 0, an empty list is returned.
    """

    matrix = []

    if n <= 0:
        return matrix
    matrix = [[1]]  # Start with the first row of Pascal's triangle

    for i in range(1, n):
        temp = [1]  # Every row starts with 1
        for j in range(1, len(matrix[i - 1])):  # Loop through the previous row
            temp.append(matrix[i - 1][j - 1] + matrix[i - 1][j])
        temp.append(1)  # Every row ends with 1
        matrix.append(temp)  # Add the row to the triangle

    return matrix
