manual.md

```
# Simple Power Checker

This software provides a function to determine if a number `x` is a simple power of another number `n`. A number `x` is considered a simple power of `n` if there exists an integer `k` such that `n**k = x`.

## Main Function

The main function provided by this software is `is_simple_power(x, n)`. This function checks if `x` is a simple power of `n` and returns `True` if it is, and `False` otherwise.

### Function Signature

```python
def is_simple_power(x, n):
```

### Parameters

- `x` (int): The number to be checked.
- `n` (int): The base number.

### Returns

- `bool`: Returns `True` if `x` is a simple power of `n`, otherwise returns `False`.

### Examples

```python
is_simple_power(1, 4)  # Returns: True
is_simple_power(2, 2)  # Returns: True
is_simple_power(8, 2)  # Returns: True
is_simple_power(3, 2)  # Returns: False
is_simple_power(3, 1)  # Returns: False
is_simple_power(5, 3)  # Returns: False
```

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

1. Clone or download the repository containing the `main.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where `main.py` is located.
4. Run the Python interpreter and import the function:

```bash
python
```

```python
from main import is_simple_power
```

5. Use the `is_simple_power` function with your desired inputs:

```python
result = is_simple_power(8, 2)
print(result)  # Output: True
```

## Documentation

For further details and examples, please refer to the comments within the `main.py` file. The function is well-documented to help you understand its usage and behavior.

```