#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists element by element.

    Args:
        my_list_1: First list of elements.
        my_list_2: Second list of elements.
        list_length: The number of elements to consider from both lists.

    Returns:
        A new list containing the results of the divisions.
    """
    result = [0] * list_length
    for i in range(list_length):
        try:
            result[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
    return result
