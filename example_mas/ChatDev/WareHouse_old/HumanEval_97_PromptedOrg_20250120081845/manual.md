# Multiply Unit Digits

This software provides a simple function to multiply the unit digits of two integers. It is designed to be straightforward and efficient, with no external dependencies required.

## Main Function

The main function of this software is:

- `multiply(a, b)`: This function takes two integers as input and returns the product of their unit digits. The unit digit of a number is the last digit of its absolute value. For example, the unit digit of -15 is 5.

### Examples

- `multiply(148, 412)` returns `16`.
- `multiply(19, 28)` returns `72`.
- `multiply(2020, 1851)` returns `0`.
- `multiply(14, -15)` returns `20`.

## Installation

There are no external dependencies required for this project. You only need Python installed on your system to run the code.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: Download or clone the repository containing the `main.py` file.

3. **Run the code**: You can run the code directly using Python. Open a terminal or command prompt, navigate to the directory containing `main.py`, and execute the following command:

   ```bash
   python main.py
   ```

## How to Use

To use the `multiply` function, you can either import it into another Python script or run it directly in a Python environment.

### Example Usage

```python
from main import multiply

result = multiply(148, 412)
print(result)  # Output: 16
```

You can replace `148` and `412` with any other integers to get the product of their unit digits.

## Documentation

For further details on how the function works, refer to the docstring within the `main.py` file. The docstring provides a brief explanation of the function's purpose, input parameters, and expected output.

This software is designed to be simple and efficient, focusing solely on the task of multiplying unit digits without any additional features or complexities.