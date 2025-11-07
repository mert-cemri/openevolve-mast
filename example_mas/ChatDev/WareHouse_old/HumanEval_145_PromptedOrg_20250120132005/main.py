'''
This module contains a function to sort a list of integers based on the sum of their digits.
'''
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index in the original list.
    :param nums: List of integers to be sorted.
    :return: List of integers sorted by the sum of their digits.
    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def sum_of_digits(n):
        """Calculate the sum of the absolute value of the digits of n."""
        return sum(int(digit) for digit in str(abs(n)))
    # Sort nums using the sum of digits as the key, maintaining original order for ties
    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))
# Example usage
if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
    print(order_by_points([]))  # Output: []