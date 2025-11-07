manual.md

```
# Simple Power Checker

This software provides a simple function to determine if a given number is a simple power of another number. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function provided by this software is `is_simple_power(x, n)`. This function checks if a number `x` is a simple power of `n`. A number `x` is considered a simple power of `n` if there exists an integer `k` such that `n**k = x`.

### Function Signature

```python
def is_simple_power(x, n):
```

### Parameters

- `x`: The number to check if it is a simple power of `n`.
- `n`: The base number to check against.

### Returns

- `True` if `x` is a simple power of `n`.
- `False` otherwise.

### Examples

- `is_simple_power(1, 4)` returns `True`
- `is_simple_power(2, 2)` returns `True`
- `is_simple_power(8, 2)` returns `True`
- `is_simple_power(3, 2)` returns `False`
- `is_simple_power(3, 1)` returns `False`
- `is_simple_power(5, 3)` returns `False`

## Installation

This software does not require any external dependencies. You only need to have Python installed on your system.

### Quick Install

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run the Python interpreter and import the function:

   ```bash
   python
   ```

   ```python
   from main import is_simple_power
   ```

4. Use the function by passing the desired values for `x` and `n`:

   ```python
   result = is_simple_power(8, 2)
   print(result)  # Output: True
   ```

## Documentation

For further documentation, please refer to the comments within the `main.py` file, which provide additional insights into the function's logic and usage.

```