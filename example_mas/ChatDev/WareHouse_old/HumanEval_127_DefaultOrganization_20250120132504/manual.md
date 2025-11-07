# Interval Intersection Prime Checker

This software provides a function to determine if the length of the intersection of two intervals is a prime number. It is a simple utility written in Python, designed to handle closed intervals where each interval is a pair of integers.

## Main Functions

### `intersection(interval1, interval2)`

- **Purpose**: Determines if the length of the intersection of two intervals is a prime number.
- **Parameters**:
  - `interval1`: A tuple representing the first interval (start1, end1).
  - `interval2`: A tuple representing the second interval (start2, end2).
- **Returns**: 
  - `"YES"` if the length of the intersection is a prime number.
  - `"NO"` if the length of the intersection is not a prime number or if the intervals do not intersect.

### `is_prime(n)`

- **Purpose**: Checks if a given number is a prime number.
- **Parameters**:
  - `n`: An integer to check for primality.
- **Returns**: 
  - `True` if `n` is a prime number.
  - `False` otherwise.

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: 
   - Use `git clone <repository-url>` to clone the repository to your local machine.

2. **Navigate to the Directory**:
   - Use `cd <repository-directory>` to navigate to the directory containing the `main.py` file.

3. **Run the Script**:
   - Execute the script using Python: `python main.py`.

## Usage

To use the `intersection` function, simply import it into your Python script and call it with the desired intervals. Here is an example:

```python
from main import intersection

result = intersection((1, 2), (2, 3))
print(result)  # Output: "NO"

result = intersection((-1, 1), (0, 4))
print(result)  # Output: "NO"

result = intersection((-3, -1), (-5, 5))
print(result)  # Output: "YES"
```

## Documentation

For further information on how the functions work, please refer to the docstrings provided in the `main.py` file. These docstrings offer detailed explanations of the parameters and return values for each function.

This software is designed to be simple and efficient, providing a straightforward solution to the problem of determining the primality of the length of interval intersections.