'''
This module contains a function `order_by_points` which sorts a list of integers
based on the sum of their digits. If two numbers have the same digit sum, they
are ordered based on their original position in the list.
'''
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, they are ordered based on
    their index in the original list.
    Args:
    nums (list of int): The list of integers to sort.
    Returns:
    list of int: The sorted list of integers.
    """
    def digit_sum(n):
        """Calculate the sum of digits of an integer."""
        return sum(int(digit) for digit in str(abs(n)))
    # Sort the list using the digit sum as the key
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
# Example usage:
# print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
# print(order_by_points([]))  # Output: []