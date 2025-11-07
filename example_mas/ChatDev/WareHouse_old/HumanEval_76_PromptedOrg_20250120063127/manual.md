# Simple Power Checker

This software provides a function to determine if a given number `x` is a simple power of another number `n`. Specifically, it checks if there exists an integer `k` such that `n**k = x`.

## Main Functionality

The core functionality of this software is encapsulated in the `is_simple_power(x, n)` function. This function returns `True` if `x` is a simple power of `n`, and `False` otherwise. 

### Examples

- `is_simple_power(1, 4)` returns `True`
- `is_simple_power(2, 2)` returns `True`
- `is_simple_power(8, 2)` returns `True`
- `is_simple_power(3, 2)` returns `False`
- `is_simple_power(3, 1)` returns `False`
- `is_simple_power(5, 3)` returns `False`

## Installation

This software does not require any external dependencies, so you can use it directly with a standard Python installation.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Download the Code**: Save the provided `main.py` file to your local machine.

2. **Run the Code**: You can run the function in a Python environment. Open a terminal or command prompt and navigate to the directory containing `main.py`.

3. **Execute the Function**: Use a Python interpreter to execute the function. For example:

   ```bash
   python
   ```

   Then, within the Python shell, you can test the function:

   ```python
   from main import is_simple_power

   print(is_simple_power(8, 2))  # Output: True
   print(is_simple_power(3, 2))  # Output: False
   ```

## Documentation

The function `is_simple_power(x, n)` is straightforward and does not require additional libraries or complex setup. It is designed to be used in any Python environment without additional configuration.

For any further questions or support, please contact our support team.