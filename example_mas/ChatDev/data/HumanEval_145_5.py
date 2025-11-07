'''
This module contains the implementation of the function `order_by_points`
which sorts a list of integers based on the sum of their digits.
'''
def digit_sum(n):
    """
    Calculate the sum of the digits of a number.
    Args:
    n (int): The number whose digits will be summed.
    Returns:
    int: The sum of the digits.
    """
    return sum(int(digit) for digit in str(abs(n)))
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index
    in the original list.
    Args:
    nums (list of int): The list of integers to sort.
    Returns:
    list of int: The sorted list of integers.
    Examples:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))