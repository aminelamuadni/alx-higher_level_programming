#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x integers in my_list.

    Args:
        my_list: List of elements.
        x: Number of elements to access in my_list.

    Returns:
        The number of integers printed.
    """
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return count
