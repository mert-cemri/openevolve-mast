manual.md

```
# Count Nums

A simple Python application to count the number of integers in an array whose sum of digits is greater than zero.

## Introduction

The `count_nums` function is designed to process an array of integers and return the count of numbers where the sum of their digits is greater than zero. This function handles both positive and negative integers, considering the sign of the first digit in negative numbers.

## Features

- **Sum of Digits Calculation**: Accurately calculates the sum of digits for each integer in the array.
- **Negative Number Handling**: Properly accounts for the sign of the first digit in negative numbers.
- **Zero Dependency**: No external libraries are required, making it lightweight and easy to integrate.

## Installation

Since this application does not require any external dependencies, you can directly use the provided Python script without any additional installation steps.

## Usage

To use the `count_nums` function, follow these steps:

1. **Prepare Your Environment**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Create a Python Script**: Save the provided code into a file named `main.py`.

3. **Run the Script**: Execute the script using a Python interpreter. You can test the function with different arrays of integers.

### Example

Here's a simple example of how to use the `count_nums` function:

```python
# Import the function from the script
from main import count_nums

# Define an array of integers
numbers = [-1, 11, -11, 1, 1, 2]

# Call the function and print the result
result = count_nums(numbers)
print(f"The number of elements with a sum of digits > 0 is: {result}")
```

## Testing

You can test the function using the provided examples in the docstring:

- `count_nums([]) == 0`
- `count_nums([-1, 11, -11]) == 1`
- `count_nums([1, 1, 2]) == 3`

These examples can be used to verify that the function behaves as expected.

## Conclusion

The `count_nums` function is a straightforward tool for counting numbers based on the sum of their digits. Its simplicity and lack of dependencies make it an ideal choice for quick integration into larger projects or for standalone use.
```