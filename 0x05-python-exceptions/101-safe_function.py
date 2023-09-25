#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: A pointer to the function to execute.
        *args: A variable number of arguments for fct.

    Returns:
        The result of fct if it executes successfully, otherwise None.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
