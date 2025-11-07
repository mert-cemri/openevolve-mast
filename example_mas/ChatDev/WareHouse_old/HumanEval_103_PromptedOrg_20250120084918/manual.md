# Rounded Average Function User Manual

Welcome to the user manual for the `rounded_avg` function. This function is designed to compute the average of integers within a specified range, round it to the nearest integer, and convert the result to a binary string. If the range is invalid (i.e., the starting integer is greater than the ending integer), the function will return -1.

## Main Functionality

The `rounded_avg` function performs the following tasks:

1. **Input Validation**: Checks if the starting integer `n` is greater than the ending integer `m`. If so, it returns -1.
2. **Sum Calculation**: Computes the sum of all integers from `n` to `m`, inclusive.
3. **Average Calculation**: Calculates the average of these integers.
4. **Rounding**: Rounds the average to the nearest integer.
5. **Binary Conversion**: Converts the rounded average to a binary string prefixed with "0b".

## Installation

This function does not require any external dependencies, so there is no need to install additional packages. You can directly use the function in your Python environment.

## Usage

To use the `rounded_avg` function, follow these steps:

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Create a Python Script**: Create a Python file (e.g., `main.py`) and include the `rounded_avg` function code provided below.

```python
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    # Calculate the sum of integers from n to m
    total_sum = sum(range(n, m + 1))
    # Calculate the count of integers from n to m
    count = m - n + 1
    # Calculate the average and round it to the nearest integer
    average = round(total_sum / count)
    # Convert the rounded average to a binary string
    return bin(average)
```

3. **Run the Script**: Execute the script using a Python interpreter. You can test the function with different values of `n` and `m` to see the results.

Example usage:

```python
print(rounded_avg(1, 5))  # Output: "0b11"
print(rounded_avg(7, 5))  # Output: -1
print(rounded_avg(10, 20))  # Output: "0b1111"
print(rounded_avg(20, 33))  # Output: "0b11010"
```

## Conclusion

The `rounded_avg` function is a simple yet effective tool for calculating the rounded average of a range of integers and converting it to a binary format. It is easy to integrate into any Python project without the need for additional dependencies.