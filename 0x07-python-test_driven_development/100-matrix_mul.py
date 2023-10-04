#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: A matrix containing the product of m_a and m_b.
    """

    # Validation
    for name, matrix in (("m_a", m_a), ("m_b", m_b)):
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))
        if not matrix or not all(isinstance(row, list) for row in matrix):
            raise TypeError("{} must be a list of lists".format(name))
        if not all(row for row in matrix):
            raise ValueError("{} can't be empty".format(name))

        row_len = len(matrix[0])
        for row in matrix:
            if not all(isinstance(num, (int, float)) for num in row):
                msg = ("{} should contain only integers or "
                       "floats").format(name)
                raise TypeError(msg)
            if len(row) != row_len:
                error_msg = ("each row of {}"
                             " must be of the same size").format(name)
                raise TypeError(error_msg)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
        for row_a in m_a
    ]
    return result

