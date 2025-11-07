# Rounded Average Calculator

This software module provides a function to compute the average of integers between two given numbers, rounds the result to the nearest integer, and converts it to a binary string. If the first number is greater than the second, it returns -1.

## Main Functionality

The main function provided by this module is `rounded_avg(n, m)`. It performs the following tasks:

- Computes the average of integers from `n` to `m` (inclusive).
- Rounds the average to the nearest integer.
- Converts the rounded average to a binary string.
- Returns `-1` if `n` is greater than `m`.

### Example Usage

```python
rounded_avg(1, 5)  # Returns "0b11"
rounded_avg(7, 5)  # Returns -1
rounded_avg(10, 20)  # Returns "0b1111"
rounded_avg(20, 33)  # Returns "0b11010"
```

## Installation

This module is implemented in Python and does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system.

### Quick Install

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

## How to Use

1. **Open a Python Interpreter**: You can use any Python interpreter or IDE of your choice.

2. **Import the Function**: Import the `rounded_avg` function from the `main.py` file.

   ```python
   from main import rounded_avg
   ```

3. **Call the Function**: Use the function by passing two positive integers as arguments.

   ```python
   result = rounded_avg(1, 5)
   print(result)  # Output: "0b11"
   ```

## Documentation

For further documentation and examples, refer to the comments within the `main.py` file. The function is designed to be straightforward and easy to integrate into larger projects.

## Support

For any issues or questions, please contact our support team or open an issue in the repository. We are here to assist you with any challenges you may encounter while using this module.