manual.md

```
# Greatest Common Divisor Calculator

This software module provides a function to calculate the greatest common divisor (GCD) of two integers. The GCD is the largest positive integer that divides each of the integers without leaving a remainder.

## Main Function

The main function provided by this module is `greatest_common_divisor(a, b)`. This function takes two integer inputs and returns their greatest common divisor.

### Function Signature

```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return the greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
```

### Example Usage

```python
# Example 1
result = greatest_common_divisor(3, 5)
print(result)  # Output: 1

# Example 2
result = greatest_common_divisor(25, 15)
print(result)  # Output: 5
```

## Installation

This module does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file containing the function.
2. **Ensure Python is installed** on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Open your Python environment** (e.g., terminal, command prompt, or an IDE like PyCharm or VSCode).
2. **Navigate to the directory** where `main.py` is located.
3. **Run your Python script** or open a Python shell and import the function:

   ```python
   from main import greatest_common_divisor
   ```

4. **Call the function** with two integer arguments to get their greatest common divisor.

## Documentation

This module is straightforward and does not require extensive documentation. The function is implemented using the Euclidean algorithm, which is efficient and widely used for computing the GCD.

For further inquiries or support, please contact our support team or visit our website for more information.

```