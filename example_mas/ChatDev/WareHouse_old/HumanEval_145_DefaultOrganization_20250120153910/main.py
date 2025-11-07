'''
This module contains the implementation of the order_by_points function.
The function sorts a list of integers based on the sum of their digits.
If two numbers have the same digit sum, they retain their original order.
'''
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index in the original list.
    Parameters:
    nums (list): A list of integers.
    Returns:
    list: A list of integers sorted by the sum of their digits.
    """
    # Helper function to calculate the sum of digits of a number
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))
    # Sort the list using the sum of digits as the key, and maintain original order for ties
    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))
# Example usage:
# print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
# print(order_by_points([]))  # Output: []