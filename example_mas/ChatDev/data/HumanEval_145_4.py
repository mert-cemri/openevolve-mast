'''
This module contains the function order_by_points which sorts a list of integers
based on the sum of their digits. If two numbers have the same digit sum,
they maintain their original order.
'''
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index in the original list.
    :param nums: List of integers to be sorted.
    :return: List of integers sorted by the sum of their digits.
    """
    # Helper function to calculate the sum of digits of a number
    def digit_sum(n):
        return sum(int(digit) for digit in str(abs(n)))
    # Sort the list using the digit_sum as the key, maintaining original order for ties
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))