# MinSubArraySum User Manual

## Introduction

The `minSubArraySum` function is a Python utility designed to find the minimum sum of any non-empty sub-array within a given list of integers. This function is particularly useful for tasks involving array manipulation and optimization problems where identifying the smallest possible sub-array sum is required.

### Main Functionality

- **Function Name**: `minSubArraySum`
- **Purpose**: To compute the minimum sum of any non-empty sub-array from a list of integers.
- **Input**: A list of integers (`nums`).
- **Output**: An integer representing the minimum sum of any non-empty sub-array.

### Example Usage

```python
# Example 1
result = minSubArraySum([2, 3, 4, 1, 2, 4])
print(result)  # Output: 1

# Example 2
result = minSubArraySum([-1, -2, -3])
print(result)  # Output: -6
```

## Installation

### Environment Setup

This function does not require any external dependencies, making it straightforward to integrate into any Python environment. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python scripts. Simply copy the function code into your project.

## How to Use

1. **Copy the Function**: Include the `minSubArraySum` function in your Python script or project.

2. **Pass a List of Integers**: Call the function with a list of integers as an argument.

3. **Receive the Minimum Sub-array Sum**: The function will return the minimum sum of any non-empty sub-array.

### Example Code

```python
def minSubArraySum(nums):
    if not nums:
        return 0
    min_ending_here = nums[0]
    min_so_far = nums[0]
    for num in nums[1:]:
        min_ending_here = min(num, min_ending_here + num)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

# Using the function
nums = [2, 3, 4, 1, 2, 4]
print("Minimum sub-array sum:", minSubArraySum(nums))
```

## Conclusion

The `minSubArraySum` function is a simple yet effective tool for finding the minimum sum of any non-empty sub-array in a list of integers. With no external dependencies, it is easy to integrate and use in various Python projects.