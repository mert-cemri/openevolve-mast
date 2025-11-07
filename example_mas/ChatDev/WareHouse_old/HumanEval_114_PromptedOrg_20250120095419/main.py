'''
This module contains a function to find the minimum sum of any non-empty sub-array
of a given list of integers.
'''
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Args:
    nums (list of int): The list of integers to evaluate.
    Returns:
    int: The minimum sum of any non-empty sub-array.
    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    min_ending_here = nums[0]
    min_so_far = nums[0]
    for num in nums[1:]:
        min_ending_here = min(num, min_ending_here + num)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far