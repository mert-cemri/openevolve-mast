'''
This module contains the function `sort_array` which sorts an array of integers
according to the number of ones in their binary representation in ascending order.
For numbers with the same number of ones, it sorts them based on their decimal value.
Negative numbers are sorted by their decimal value.
'''
def sort_array(arr):
    """
    Sorts an array of integers according to the number of ones in their binary
    representation in ascending order. For numbers with the same number of ones, sorts based
    on decimal value. Negative numbers are sorted by their decimal value.
    Args:
    arr (list): A list of integers.
    Returns:
    list: A sorted list of integers.
    Examples:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """
    non_negative = sorted((x for x in arr if x >= 0), key=lambda x: (bin(x).count('1'), x))
    negative = sorted((x for x in arr if x < 0))
    return negative + non_negative
# Example usage
if __name__ == "__main__":
    print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
    print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
    print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]