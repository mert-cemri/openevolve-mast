'''
This module contains a function to sort an array of non-negative integers
based on the number of ones in their binary representation.
'''
def sort_array(arr):
    """
    Sort an array of non-negative integers according to the number of ones
    in their binary representation in ascending order. For similar number of
    ones, sort based on decimal value.
    Args:
    arr (list): List of non-negative integers to be sorted.
    Returns:
    list: Sorted list of integers.
    Examples:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 4, 3, 5]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 4, 3]
    """
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))