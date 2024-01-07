#!/usr/bin/python3
"""
Module 6-peak
Contains function find_peak: Finds a peak in a list of unsorted integers.
Uses modified binary search for efficiency.
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    Args:
        list_of_integers: List of integers.
    Returns:
        An integer (peak) or None if list is empty or no peak found.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]

    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if list_of_integers[mid] >= list_of_integers[mid - 1] and \
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]

        if list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None
