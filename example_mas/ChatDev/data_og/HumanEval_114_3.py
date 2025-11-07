'''
Given an array of integers nums, find the minimum sum of any non-empty sub-array
of nums.
Example:
minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
minSubArraySum([-1, -2, -3]) == -6
'''
def minSubArraySum(nums):
    # Initialize the minimum sum to a large value and the current sum to 0
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        # Update the current sum to be the minimum of the current number itself
        # or the current sum plus the current number
        current_sum = min(num, current_sum + num)
        # Update the minimum sum if the current sum is less than the minimum sum
        min_sum = min(min_sum, current_sum)
    return min_sum
# Example usage
if __name__ == "__main__":
    print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
    print(minSubArraySum([-1, -2, -3]))        # Output: -6