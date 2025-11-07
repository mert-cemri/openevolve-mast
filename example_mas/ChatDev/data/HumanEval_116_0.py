'''
This module contains a function to sort an array of integers based on the number of ones in their binary representation for non-negative numbers.
For numbers with the same number of ones, they are sorted by their decimal value.
Negative numbers are sorted by their decimal value only.
'''
def sort_array(arr):
    """
    Sort an array of integers based on the number of ones in their binary representation for non-negative numbers.
    For numbers with the same number of ones, sort by decimal value.
    Negative numbers should be sorted by their decimal value.
    Args:
    arr (list of int): The list of integers to sort.
    Returns:
    list of int: The sorted list of integers.
    Examples:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """
    # Separate negative and non-negative numbers
    non_negative = [x for x in arr if x >= 0]
    negative = [x for x in arr if x < 0]
    # Sort non-negative numbers based on the number of ones in binary representation and then by decimal value
    sorted_non_negative = sorted(non_negative, key=lambda x: (bin(x).count('1'), x))
    # Sort negative numbers by their decimal value
    sorted_negative = sorted(negative)
    # Combine the sorted lists
    return sorted_negative + sorted_non_negative