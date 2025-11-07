manual.md

```
# Simple Power Checker

This software provides a function to determine if a given number is a simple power of another number. It is implemented in Python and is designed to be straightforward and efficient.

## Main Functionality

The main function provided by this software is `is_simple_power(x, n)`. This function checks if a number `x` is a simple power of another number `n`. A number `x` is considered a simple power of `n` if there exists an integer `k` such that `n**k = x`.

### Function Signature

```python
def is_simple_power(x, n):
    """Returns True if x is a simple power of n, otherwise False."""
```

### Example Usage

```python
# Example usage:
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are necessary since there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python script using the command:

   ```bash
   python main.py
   ```

4. You can modify the script to test different values of `x` and `n` by changing the parameters in the `is_simple_power` function calls.

## Documentation

For further details and documentation, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and functionality.

Feel free to reach out for support or further inquiries if needed.
```
