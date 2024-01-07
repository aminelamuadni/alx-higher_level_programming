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

    low, high = 0, len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = list_of_integers[mid]

        is_left_peak = (mid == 0 or list_of_integers[mid - 1] <= mid_val)
        is_right_peak = (mid == len(list_of_integers) - 1 or 
                         list_of_integers[mid + 1] <= mid_val)

        if is_left_peak and is_right_peak:
            return mid_val

        if mid > 0 and list_of_integers[mid - 1] > mid_val:
            high = mid - 1
        else:
            low = mid + 1

    return None
