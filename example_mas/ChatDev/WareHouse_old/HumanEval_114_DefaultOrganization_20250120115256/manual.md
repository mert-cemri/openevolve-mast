manual.md

```
# MinSubArraySum

A simple Python application to find the minimum sum of any non-empty sub-array of a given list of integers.

## Overview

The `minSubArraySum` function is designed to solve the problem of finding the minimum sum of any non-empty sub-array within a list of integers. This can be useful in various computational scenarios where you need to determine the smallest possible sum from contiguous elements in an array.

## Features

- **Efficient Calculation**: The function efficiently computes the minimum sub-array sum using a linear time complexity algorithm.
- **No External Dependencies**: The application does not require any external libraries or dependencies, making it easy to integrate and use in any Python environment.

## Installation

Since there are no external dependencies required for this application, you can simply use the function in any Python environment without additional installations.

### Requirements

- Python 3.x

## Usage

To use the `minSubArraySum` function, follow these steps:

1. **Clone or Download the Repository**: Obtain the `main.py` file from the repository.

2. **Run the Function**: You can directly run the function in a Python environment. Here's an example of how to use it:

```python
# Import the function from the main.py file
from main import minSubArraySum

# Example usage
result1 = minSubArraySum([2, 3, 4, 1, 2, 4])
print(result1)  # Output: 1

result2 = minSubArraySum([-1, -2, -3])
print(result2)  # Output: -6
```

3. **Modify the Input**: You can modify the input list to test with different arrays of integers.

## How It Works

The function iterates through the list of integers, maintaining a running sum of the current sub-array. It updates the minimum sum whenever the current sum is less than the previously recorded minimum. If the current sum becomes positive, it resets to zero to ensure that the sub-array remains non-empty and the minimum sum is correctly calculated.

## Conclusion

The `minSubArraySum` function is a straightforward and efficient solution for finding the minimum sum of any non-empty sub-array in a list of integers. Its simplicity and lack of dependencies make it easy to use and integrate into various Python projects.
```