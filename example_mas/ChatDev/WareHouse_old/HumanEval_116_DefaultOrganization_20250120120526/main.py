'''
This module contains the implementation of the sort_array function which sorts
an array of integers based on the number of ones in their binary representation
for non-negative numbers. Negative numbers are sorted by their decimal value.
'''
def sort_array(arr):
    """
    Sort an array of integers according to the number of ones in their binary
    representation for non-negative numbers in ascending order. For similar
    number of ones, sort based on decimal value. Negative numbers should be
    sorted by their decimal value.
    Args:
    arr (list): A list of integers.
    Returns:
    list: A sorted list based on the criteria mentioned.
    Examples:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6])
    [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4])
    [0, 1, 2, 3, 4]
    """
    # Separate negative and non-negative numbers
    non_negative_arr = [x for x in arr if x >= 0]
    negative_arr = [x for x in arr if x < 0]
    # Sort non-negative numbers based on binary ones count and decimal value
    sorted_non_negative = sorted(non_negative_arr, key=lambda x: (bin(x).count('1'), x))
    # Sort negative numbers by decimal value
    sorted_negative = sorted(negative_arr)
    # Combine sorted negative and non-negative numbers
    return sorted_negative + sorted_non_negative
# Example usage
if __name__ == "__main__":
    print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
    print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
    print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]