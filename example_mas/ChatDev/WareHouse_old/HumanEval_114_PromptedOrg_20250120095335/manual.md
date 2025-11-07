# MinSubArraySum User Manual

Welcome to the MinSubArraySum software user manual. This document provides a comprehensive guide on how to use the MinSubArraySum function, including installation instructions and usage examples.

## Introduction

The MinSubArraySum function is designed to find the minimum sum of any non-empty sub-array from a given list of integers. This can be particularly useful in scenarios where you need to identify the smallest possible sum from contiguous elements within an array.

### Main Functionality

- **Function Name:** `minSubArraySum`
- **Purpose:** To calculate the minimum sum of any non-empty sub-array from a list of integers.
- **Input:** A list of integers `nums`.
- **Output:** An integer representing the minimum sum of any non-empty sub-array.

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

The MinSubArraySum function is implemented in Python and does not require any external dependencies. You can simply copy the function into your Python script or project and use it directly.

### Environment Setup

1. **Python Installation:** Ensure that you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **No External Libraries Required:** This project does not require any additional Python packages or libraries. You can run the function using the standard Python environment.

## How to Use

1. **Copy the Function:**
   - Copy the `minSubArraySum` function from the provided code into your Python script.

2. **Call the Function:**
   - Pass a list of integers to the `minSubArraySum` function to get the minimum sum of any non-empty sub-array.

3. **Example Code:**

```python
def minSubArraySum(nums):
    if not nums:
        return 0  # Edge case: if the list is empty, return 0
    current_min = nums[0]
    global_min = nums[0]
    for num in nums[1:]:
        current_min = min(num, current_min + num)
        global_min = min(global_min, current_min)
    return global_min

# Example usage
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))        # Output: -6
```

## Conclusion

The MinSubArraySum function is a simple yet powerful tool for finding the minimum sum of sub-arrays in a list of integers. With no external dependencies, it is easy to integrate into any Python project. We hope this manual helps you effectively utilize the function in your applications. If you have any questions or need further assistance, please feel free to reach out.