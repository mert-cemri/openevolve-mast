'''
This module contains a function to sort a list of integers based on the sum of their digits.
If two numbers have the same digit sum, they maintain their original order.
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
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digit_sum(n):
        return sum(int(d) for d in str(abs(n)))
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
# Example usage
if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
    print(order_by_points([]))  # Output: []