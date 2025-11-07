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
    n = len(l)
    sorted_list = sorted(l)
    mid = n // 2
    if n % 2 == 0:
        # If even, return the average of the middle two numbers
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        # If odd, return the middle number
        return sorted_list[mid]