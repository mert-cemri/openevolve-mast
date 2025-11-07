manual.md

```
# Simple Power Checker

This software provides a function to determine if a given number is a simple power of another number. It is implemented in Python and is designed to be straightforward and efficient.

## Main Functionality

The main function provided by this software is `is_simple_power(x, n)`. This function checks if a number `x` is a simple power of another number `n`. A number `x` is considered a simple power of `n` if there exists an integer `k` such that `n**k = x`.

### Function Definition

```python
def is_simple_power(x, n):
    """Check if x is a simple power of n."""
    if x < 1 or n < 1:
        return False
    if x == 1:
        return True
    while x % n == 0:
        x //= n
    return x == 1
```

### Usage Examples

- `is_simple_power(1, 4)` returns `True` because 4^0 = 1.
- `is_simple_power(2, 2)` returns `True` because 2^1 = 2.
- `is_simple_power(8, 2)` returns `True` because 2^3 = 8.
- `is_simple_power(3, 2)` returns `False` because there is no integer k such that 2^k = 3.
- `is_simple_power(3, 1)` returns `False` because 1^k cannot equal 3 for any integer k.
- `is_simple_power(5, 3)` returns `False` because there is no integer k such that 3^k = 5.

## Installation

To use this software, you need to have Python installed on your system. The function does not require any external dependencies, so no additional packages are needed.

### Step-by-Step Installation Guide

1. **Install Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Move into the directory containing the `main.py` file:
   ```bash
   cd <directory-name>
   ```

4. **Run the Function**: You can test the function by running the `main.py` file in a Python environment:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you want to use the function in another script, you can import it:
   ```python
   from main import is_simple_power
   ```

2. **Call the Function**: Use the function by passing the numbers you want to check:
   ```python
   result = is_simple_power(8, 2)
   print(result)  # Output: True
   ```

## Conclusion

This software provides a simple and efficient way to check if a number is a simple power of another number. It is easy to integrate into other Python projects and requires no additional dependencies.
```