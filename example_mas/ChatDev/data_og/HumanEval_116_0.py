'''
This module contains a function to sort an array of integers
based on the number of ones in their binary representation. If two numbers
have the same number of ones, they are sorted by their decimal value.
'''
def sort_array(arr):
    """
    Sort an array of integers according to the number of ones
    in their binary representation in ascending order. For numbers with the
    same number of ones, sort based on decimal value.
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
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
# Example usage
if __name__ == "__main__":
    print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
    print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
    print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]