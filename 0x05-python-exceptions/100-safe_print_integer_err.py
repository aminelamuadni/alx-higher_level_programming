#!/usr/bin/python3

def safe_print_integer_err(value):
    """Prints an integer or an error message if not possible."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
