manual.md

```
# Simple Power Checker

This software provides a function to determine if a number `x` is a simple power of another number `n`. A number `x` is considered a simple power of `n` if there exists an integer `k` such that `n**k = x`.

## Main Function

The main function provided by this software is:

- `is_simple_power(x, n)`: This function returns `True` if `x` is a simple power of `n`, and `False` otherwise.

### Function Details

- **Parameters**:
  - `x`: The number to be checked.
  - `n`: The base number.

- **Returns**: 
  - `True` if `x` is a simple power of `n`.
  - `False` otherwise.

- **Examples**:
  - `is_simple_power(1, 4)` returns `True`
  - `is_simple_power(2, 2)` returns `True`
  - `is_simple_power(8, 2)` returns `True`
  - `is_simple_power(3, 2)` returns `False`
  - `is_simple_power(3, 1)` returns `False`
  - `is_simple_power(5, 3)` returns `False`

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the `main.py` file.
3. No additional installation steps are required.

## How to Use

1. Open the `main.py` file in your preferred Python editor or IDE.
2. Use the `is_simple_power(x, n)` function by passing the desired values for `x` and `n`.
3. Run the script to see the results.

### Example Usage

```python
from main import is_simple_power

# Example usage
result = is_simple_power(8, 2)
print(result)  # Output: True

result = is_simple_power(3, 2)
print(result)  # Output: False
```

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The function is designed to be straightforward and easy to integrate into other projects.

```