# Intersection Prime Checker

This software module provides a function to determine if the length of the intersection of two intervals is a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function of this software is `intersection(interval1, interval2)`, which takes two intervals as input and returns "YES" if the length of their intersection is a prime number, and "NO" otherwise. If the intervals do not intersect, it also returns "NO".

### Function Details

- **intersection(interval1, interval2):**
  - **Input:** Two intervals, each represented as a tuple of two integers (start, end).
  - **Output:** A string "YES" or "NO".
  - **Description:** The function calculates the intersection of the two intervals and checks if the length of this intersection is a prime number.

## Installation

This software does not require any external libraries or dependencies, so no installation is necessary beyond having Python installed on your system.

## Usage

To use the `intersection` function, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the code from `main.py` into your Python environment or script.
3. Call the `intersection` function with two intervals as arguments.

### Example Usage

```python
# Example 1
result1 = intersection((1, 2), (2, 3))
print(result1)  # Output: "NO"

# Example 2
result2 = intersection((-1, 1), (0, 4))
print(result2)  # Output: "NO"

# Example 3
result3 = intersection((-3, -1), (-5, 5))
print(result3)  # Output: "YES"
```

## Documentation

The code is documented with comments explaining the logic and purpose of each function. The `is_prime` helper function is used to determine if a number is prime, which is crucial for the main functionality of checking the intersection length.

For any further questions or support, please contact our support team.