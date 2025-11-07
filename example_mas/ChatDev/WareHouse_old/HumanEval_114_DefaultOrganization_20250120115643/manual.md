manual.md

```
# MinSubArraySum

A Python utility to find the minimum sum of any non-empty sub-array from a given list of integers.

## Overview

The `minSubArraySum` function is designed to efficiently compute the minimum sum of any non-empty sub-array within a list of integers. This can be particularly useful in scenarios where you need to identify the smallest possible sum that can be derived from contiguous elements in an array.

### Key Features

- **Efficient Calculation**: The function uses an optimized approach to determine the minimum sub-array sum, ensuring quick results even for larger arrays.
- **Simple Interface**: Easy to use with a single function call.
- **No External Dependencies**: The function is implemented in pure Python, requiring no additional libraries.

## Installation

Since the function does not rely on any external libraries, you do not need to install any dependencies. Simply ensure you have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download it from the official [Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## Usage

To use the `minSubArraySum` function, follow these steps:

1. **Create a Python Script**: Create a new Python file, for example, `main.py`.

2. **Copy the Function**: Copy the following code into your `main.py` file:

    ```python
    def minSubArraySum(nums):
        """
        Given an array of integers nums, find the minimum sum of any non-empty sub-array
        of nums.
        Example:
        minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
        minSubArraySum([-1, -2, -3]) == -6
        """
        if not nums:
            return 0
        min_sum = float('inf')
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum < min_sum:
                min_sum = current_sum
            if current_sum > 0:
                current_sum = 0
        return min_sum
    ```

3. **Run the Script**: Execute the script using Python. You can do this by opening a terminal or command prompt, navigating to the directory where your `main.py` file is located, and running the command:

    ```bash
    python main.py
    ```

4. **Test the Function**: You can test the function by calling it with different lists of integers. For example:

    ```python
    print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
    print(minSubArraySum([-1, -2, -3]))        # Output: -6
    ```

## Conclusion

The `minSubArraySum` function is a straightforward and efficient tool for finding the minimum sum of any non-empty sub-array in a list of integers. With no external dependencies, it is easy to integrate into any Python project.
```