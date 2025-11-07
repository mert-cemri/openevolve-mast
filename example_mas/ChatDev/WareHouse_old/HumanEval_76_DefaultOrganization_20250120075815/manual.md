manual.md

```
# Simple Power Checker

This software provides a function to determine if a given number is a simple power of another number. It is designed to be lightweight and efficient, focusing solely on the task of checking simple powers without any additional features or interfaces.

## Main Function

The main function provided by this software is `is_simple_power(x, n)`. This function checks if a number `x` is a simple power of another number `n`. A number `x` is considered a simple power of `n` if there exists an integer `k` such that `n**k = x`.

### Function Signature

```python
def is_simple_power(x, n):
    """Returns true if x is a simple power of n, false otherwise."""
```

### Parameters

- `x`: The number to be checked.
- `n`: The base number.

### Returns

- `True` if `x` is a simple power of `n`.
- `False` otherwise.

### Example Usage

```python
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False
```

## Installation

This software is implemented in Python. To use it, you need to have Python installed on your system. Follow the steps below to set up the environment:

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Set Up the Environment

No additional dependencies are required for this software. You can directly use the provided `main.py` file.

## How to Use

1. **Download the Code**: Obtain the `main.py` file containing the `is_simple_power` function.

2. **Run the Code**: You can run the code using any Python interpreter. Simply execute the `main.py` file and use the `is_simple_power` function as demonstrated in the example usage section.

3. **Integrate into Your Project**: If you wish to use this function in your own project, you can copy the function definition into your codebase and call it as needed.

## Support

For any questions or support related to this software, please contact our support team at support@chatdev.com.

```