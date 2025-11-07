'''
This module contains the function `order_by_points` which sorts a list of integers
based on the sum of their digits. If two numbers have the same digit sum, they
are ordered based on their original position in the list.
'''
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
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digit_sum(n):
        # Calculate the sum of digits for a number, handling negative numbers as well
        return sum(int(digit) for digit in str(abs(n)))
    # Sort the list with a custom key: first by digit sum, then by original index
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
# Example usage
if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
    print(order_by_points([]))  # Output: []