#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    Attempts to print an integer followed by a new line.

    If the value provided is not an integer, the function will print an
    error message to stderr, which describes the error encountered.
    
    Args:
        value: The value to be printed. Can be of any type.

    Returns:
        True if the value was successfully printed as an integer.
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
