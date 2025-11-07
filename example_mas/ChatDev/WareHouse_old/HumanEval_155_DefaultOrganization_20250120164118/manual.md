manual.md

```
# Even Odd Digit Counter

This software provides a simple utility function to count the number of even and odd digits in a given integer. It is designed to be straightforward and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this software is encapsulated in the `even_odd_count` function, which takes an integer as input and returns a tuple containing the count of even and odd digits in that integer.

### Function Definition

```python
def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.
    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
```

### How It Works

- The function first converts the input integer to a string, ignoring any negative sign.
- It then iterates over each digit in the string representation.
- For each digit, it checks whether it is even or odd and increments the respective counter.
- Finally, it returns a tuple with the counts of even and odd digits.

## Installation

No installation of external dependencies is required for this project. The function is implemented in pure Python and can be used directly.

## Usage

To use the `even_odd_count` function, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the function code into a Python file, e.g., `main.py`.
3. Call the function with an integer argument to get the count of even and odd digits.

### Example Usage

```python
# Import the function from the module
from main import even_odd_count

# Example calls
result1 = even_odd_count(-12)
print(result1)  # Output: (1, 1)

result2 = even_odd_count(123)
print(result2)  # Output: (1, 2)
```

## Additional Information

- The function handles negative numbers by considering only the absolute value of the integer.
- It works with any integer, including zero and positive numbers.
- The function is efficient and suitable for use in larger applications where counting even and odd digits is required.

This utility is a simple yet effective tool for developers needing to analyze the composition of digits in integers.
```