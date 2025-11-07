'''
This module contains the implementation of the function `order_by_points`,
which sorts a list of integers based on the sum of their digits.
'''
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index in the original list.
    Args:
    nums (list of int): The list of integers to be sorted.
    Returns:
    list of int: The sorted list of integers.
    Examples:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """
    # Helper function to calculate the sum of digits of a number
    def digit_sum(n):
        return sum(int(digit) for digit in str(abs(n)))
    # Sort the list using the digit sum as the key, with the original index as a tiebreaker
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
# Example usage
if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))
    print(order_by_points([]))