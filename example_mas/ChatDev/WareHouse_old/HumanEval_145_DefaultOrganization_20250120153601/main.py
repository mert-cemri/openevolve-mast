'''
This module contains a function to sort a list of integers based on the sum of their digits.
'''
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with the same sum of their digits, they are ordered based on their index in the original list.
    Args:
    nums (list of int): The list of integers to be sorted.
    Returns:
    list of int: A new list of integers sorted based on the criteria.
    Examples:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """
    # Helper function to calculate the sum of digits of a number
    def digit_sum(n):
        return sum(int(digit) for digit in str(abs(n)))
    # Sort the list based on the sum of digits, and use the original index as a tiebreaker
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
# Example usage
if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
    print(order_by_points([]))  # Output: []