'''
This module contains the implementation of the sort_array function, which sorts an array of integers based on the number of ones in their binary representation for non-negative numbers. Negative numbers are sorted by their decimal value.
'''
def sort_array(arr):
    """
    Sort an array of integers according to the number of ones in their binary representation for non-negative numbers.
    For numbers with the same number of ones, sort them by their decimal value.
    Negative numbers should be sorted by their decimal value.
    Args:
    arr (list): A list of integers.
    Returns:
    list: A sorted list of integers.
    Examples:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """
    non_negatives = sorted((x for x in arr if x >= 0), key=lambda x: (bin(x).count('1'), x))
    negatives = sorted((x for x in arr if x < 0))
    return negatives + non_negatives