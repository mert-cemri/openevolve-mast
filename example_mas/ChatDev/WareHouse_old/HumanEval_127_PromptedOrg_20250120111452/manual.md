manual.md

```
# Interval Intersection Prime Checker

This software module provides a function to determine if the length of the intersection of two intervals is a prime number. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this module is `intersection(interval1, interval2)`. This function takes two intervals as input, each represented as a pair of integers, and returns "YES" if the length of their intersection is a prime number, and "NO" otherwise.

### Function Details

- **Function Name:** `intersection`
- **Parameters:**
  - `interval1`: A tuple of two integers representing the first interval (start, end).
  - `interval2`: A tuple of two integers representing the second interval (start, end).
- **Returns:** A string "YES" or "NO" based on whether the length of the intersection is a prime number.

### Example Usage

```python
# Example 1
result = intersection((1, 2), (2, 3))
print(result)  # Output: "NO"

# Example 2
result = intersection((-1, 1), (0, 4))
print(result)  # Output: "NO"

# Example 3
result = intersection((-3, -1), (-5, 5))
print(result)  # Output: "YES"
```

## Installation

This module does not require any external dependencies, making it easy to integrate into any Python environment. Simply include the `main.py` file in your project and import the `intersection` function as needed.

## How to Use

1. **Include the Module:**
   - Ensure the `main.py` file containing the `intersection` function is in your project directory.

2. **Import the Function:**
   - Use the following import statement in your Python script:
     ```python
     from main import intersection
     ```

3. **Call the Function:**
   - Pass the desired intervals as arguments to the `intersection` function and handle the output as needed.

## Additional Information

- **Prime Number Check:** The function includes an internal helper function `is_prime(n)` to determine if a number is prime.
- **Closed Intervals:** The intervals are considered closed, meaning both the start and end points are included in the interval.

This module is designed to be straightforward and efficient, providing a quick way to determine the primality of interval intersections without the need for additional libraries or complex setup.
```