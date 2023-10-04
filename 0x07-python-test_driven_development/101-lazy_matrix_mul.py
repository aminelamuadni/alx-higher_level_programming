#!/usr/bin/python3
"""Module for lazy_matrix_mul method.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        list of list of int/float: A matrix.
    """
    # Use numpy's matmul function to multiply the matrices
    return np.matmul(m_a, m_b)
