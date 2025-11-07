'''
Given an array of integers nums, find the minimum sum of any non-empty sub-array
of nums.
Example:
minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
minSubArraySum([-1, -2, -3]) == -6
'''
def minSubArraySum(nums):
    if not nums:
        return 0  # Return 0 if the list is empty, though the problem states non-empty sub-array
    current_min = nums[0]
    global_min = nums[0]
    for num in nums[1:]:
        current_min = min(num, current_min + num)
        global_min = min(global_min, current_min)
    return global_min