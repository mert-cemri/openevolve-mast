# Intersection Prime Checker

This software module provides a function to determine if the length of the intersection of two intervals is a prime number. It is implemented in Python and can be used to evaluate pairs of integer intervals.

## Main Functionality

The main function provided by this module is `intersection(interval1, interval2)`. This function takes two intervals as input, each represented as a pair of integers `(start, end)`, and returns "YES" if the length of their intersection is a prime number, otherwise returns "NO". If the intervals do not intersect, it also returns "NO".

### How It Works

1. **Intersection Calculation**: The function calculates the intersection of the two intervals.
2. **Length Calculation**: It computes the length of the intersection.
3. **Prime Check**: It checks if the length is a prime number using the helper function `is_prime(n)`.
4. **Return Result**: Based on the prime check, it returns "YES" or "NO".

## Installation

To use this software, ensure you have Python installed on your system. The module does not require any additional dependencies beyond the Python standard library.

### Quick Install

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing `main.py`.

## Usage

To use the `intersection` function, follow these steps:

1. **Open a Python Interpreter**: You can use the command line or any Python IDE.
2. **Import the Function**: Import the `intersection` function from the `main.py` file.
3. **Call the Function**: Pass two intervals as arguments to the function.

### Example

```python
from main import intersection

# Example intervals
result1 = intersection((1, 2), (2, 3))
print(result1)  # Output: "NO"

result2 = intersection((-1, 1), (0, 4))
print(result2)  # Output: "NO"

result3 = intersection((-3, -1), (-5, 5))
print(result3)  # Output: "YES"
```

## Documentation

For further details on the implementation, refer to the comments within the `main.py` file. The code is documented to provide insights into the logic and flow of the program.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided within the code. We are here to assist you in integrating and using this module effectively.