# Rounded Average Function

This software provides a simple Python function, `rounded_avg`, which calculates the average of integers between two given numbers, rounds the result to the nearest integer, and converts it to a binary string. If the first number is greater than the second, it returns -1.

## Main Function

### `rounded_avg(n, m)`

- **Description**: Computes the average of integers from `n` to `m` (inclusive), rounds it to the nearest integer, and returns the binary representation of the result. If `n` is greater than `m`, it returns -1.
- **Parameters**:
  - `n` (int): The starting integer.
  - `m` (int): The ending integer.
- **Returns**:
  - A string representing the binary form of the rounded average, prefixed with "0b", or -1 if `n` > `m`.
- **Examples**:
  - `rounded_avg(1, 5)` returns `"0b11"`
  - `rounded_avg(7, 5)` returns `-1`
  - `rounded_avg(10, 20)` returns `"0b1111"`
  - `rounded_avg(20, 33)` returns `"0b11010"`

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change into the directory where the code is located:
   ```bash
   cd <repository-directory>
   ```

## Usage

To use the `rounded_avg` function, follow these steps:

1. **Open a Python Environment**: You can use any Python environment, such as IDLE, PyCharm, or a simple terminal.

2. **Import the Function**: Ensure you are in the directory containing `main.py`, then import the function:
   ```python
   from main import rounded_avg
   ```

3. **Call the Function**: Use the function with your desired input values:
   ```python
   result = rounded_avg(1, 5)
   print(result)  # Output: "0b11"
   ```

## Documentation

For further documentation and examples, refer to the comments within the `main.py` file. The function is straightforward and designed for ease of use in calculating and converting averages to binary.

If you encounter any issues or have questions, please contact our support team for assistance.