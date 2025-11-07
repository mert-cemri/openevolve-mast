'''
This module contains a function to calculate the median of a list of numbers.
'''
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Sort the list
    sorted_list = sorted(l)
    n = len(sorted_list)
    mid = n // 2
    # If the number of elements is odd, return the middle element
    if n % 2 == 1:
        return sorted_list[mid]
    # If the number of elements is even, return the average of the two middle elements
    else:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2