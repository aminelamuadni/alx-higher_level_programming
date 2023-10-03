#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The matrix must be a list of lists of integers or floats.
Each row of the matrix must have the same size.
The division value must be a number (integer or float) and can't be zero.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with all values divided by div,
                       rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix isn't a list of lists of integers/floats,
                   if rows of the matrix are of different sizes,
                   or if div isn't a number.
        ZeroDivisionError: If div is zero.
    """
    # Check matrix and elements
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    row_length = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    # Check div and division by zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Compute the divided matrix
    return [[round(element / div, 2) for element in row] for row in matrix]

