#!/usr/bin/python3


def pascal_triangle(n):
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
