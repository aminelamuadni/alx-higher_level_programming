#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints a value if it's an integer.

    Args:
        value: The value to be printed.

    Returns:
        True if the value is printed successfully (i.e., it's an integer);
        otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
