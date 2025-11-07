manual.md

```
# Pluck Function

The Pluck Function is a simple Python utility designed to identify and return the smallest even value from a list of non-negative integers, along with its index. This function is particularly useful in scenarios where you need to efficiently extract specific data from a list based on defined criteria.

## Main Functionality

The primary function provided by this software is:

- **pluck(arr):** This function takes a list of non-negative integers as input and returns a list containing the smallest even value and its index. If there are no even values or the list is empty, it returns an empty list.

### Function Details

- **Input:** A list of non-negative integers.
- **Output:** A list containing the smallest even value and its index, or an empty list if no even values are present.

### Example Usage

```python
# Example 1
print(pluck([4, 2, 3]))  # Output: [2, 1]

# Example 2
print(pluck([1, 2, 3]))  # Output: [2, 1]

# Example 3
print(pluck([]))         # Output: []

# Example 4
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
```

## Installation

This software does not require any external dependencies, making it easy to integrate into any Python environment. Simply ensure that you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed:** You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository:** You can clone the repository using Git or download the files directly.

3. **Run the code:** You can execute the `main.py` file directly in your Python environment.

## How to Use

1. **Prepare your environment:** Ensure you have Python installed and set up on your machine.

2. **Use the function:** Import the `pluck` function from the `main.py` file into your project or script.

3. **Call the function with your data:** Pass a list of non-negative integers to the `pluck` function to get the desired output.

## Documentation

For further details and examples, please refer to the comments within the `main.py` file. The function is straightforward and well-documented to facilitate easy understanding and integration.

```