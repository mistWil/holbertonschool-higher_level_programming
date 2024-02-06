#!/usr/bin/python3


"""
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The matrix to divide.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by `div`,
        rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers or floats,
            if each row of the matrix does not have the same size,
            or if `div` is not a number (integer or float).
        ZeroDivisionError: If `div` is equal to 0.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    """

    # Validate input types
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
            (list of lists) of integers/floats")

    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
