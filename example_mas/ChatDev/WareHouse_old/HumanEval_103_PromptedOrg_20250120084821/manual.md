# Rounded Average Function User Manual

Welcome to the user manual for the `rounded_avg` function. This function is designed to calculate the average of integers within a specified range, round the result to the nearest integer, and return the binary representation of the rounded average. If the starting integer is greater than the ending integer, the function will return -1.

## Main Functionality

The primary function provided by this software is:

- **`rounded_avg(n, m)`**: Computes the average of integers from `n` to `m` (inclusive), rounds the result to the nearest integer, and returns the binary representation of the rounded average. If `n` is greater than `m`, it returns -1.

### Examples

- `rounded_avg(1, 5)` returns `"0b11"`
- `rounded_avg(7, 5)` returns `-1`
- `rounded_avg(10, 20)` returns `"0b1111"`
- `rounded_avg(20, 33)` returns `"0b11010"`

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. No additional installation steps are required as there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where the `main.py` file is located.

3. Run a Python interpreter or script to use the `rounded_avg` function. You can do this by importing the function into your Python script or interactive session.

### Example Usage

```python
from main import rounded_avg

# Example usage of the rounded_avg function
result = rounded_avg(1, 5)
print(result)  # Output: "0b11"

result = rounded_avg(7, 5)
print(result)  # Output: -1

result = rounded_avg(10, 20)
print(result)  # Output: "0b1111"

result = rounded_avg(20, 33)
print(result)  # Output: "0b11010"
```

## Documentation

For further details on how the function works, please refer to the docstring provided within the `main.py` file. The docstring includes a description of the function, its parameters, and example outputs.

This concludes the user manual for the `rounded_avg` function. If you have any questions or require further assistance, please contact our support team.