'''
This module contains a function to sort a list of integers based on the sum of their digits.
'''
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, they are ordered based on their index in the original list.
    Args:
    nums (list of int): The list of integers to sort.
    Returns:
    list of int: The sorted list of integers.
    """
    def digit_sum(n):
        """Calculate the sum of the digits of an integer."""
        return sum(int(digit) for digit in str(abs(n)))
    # Sort the list with a custom key: first by digit sum, then by original index
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))