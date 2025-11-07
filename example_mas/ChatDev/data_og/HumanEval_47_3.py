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
    # Check if the number of elements is odd
    if n % 2 == 1:
        # Return the middle element
        return sorted_list[n // 2]
    else:
        # Return the average of the two middle elements
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2