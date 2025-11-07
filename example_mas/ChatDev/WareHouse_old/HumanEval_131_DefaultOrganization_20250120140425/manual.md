# Digits Product Calculator

This software provides a simple function to calculate the product of odd digits in a given positive integer. If all digits are even, the function returns 0.

## Main Functionality

The main function provided by this software is `digits(n)`, which performs the following operations:

- **Input**: A positive integer `n`.
- **Output**: The product of all odd digits in `n`. If there are no odd digits, it returns 0.

### Example Usage

- `digits(1)` returns `1`
- `digits(4)` returns `0`
- `digits(235)` returns `15`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `digits` function.

## How to Use

1. **Open your Python environment**: You can use any Python IDE or a simple command-line interface.

2. **Import the function**: If you have saved the `main.py` file in your project, you can import the function using:
   ```python
   from main import digits
   ```

3. **Call the function**: Use the `digits` function by passing a positive integer as an argument:
   ```python
   result = digits(235)
   print(result)  # Output will be 15
   ```

## Documentation

The function is straightforward and does not require additional configuration or setup. For any further questions or support, please refer to the comments within the `main.py` file, which provide a clear explanation of the logic and usage of the function.