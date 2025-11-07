# Intersection Function User Manual

## Introduction

This software provides a Python function named `intersection` that determines if the length of the intersection of two given intervals is a prime number. The intervals are closed, meaning they include both their start and end points. The function returns "YES" if the length of the intersection is a prime number and "NO" otherwise. If the intervals do not intersect, it also returns "NO".

## Main Functions

### `intersection(interval1, interval2)`

- **Description**: Determines if the length of the intersection of two intervals is a prime number.
- **Parameters**:
  - `interval1`: A tuple of two integers representing the first interval.
  - `interval2`: A tuple of two integers representing the second interval.
- **Returns**: A string "YES" if the length of the intersection is a prime number, otherwise "NO".

### `is_prime(n)`

- **Description**: Checks if a given number is a prime number.
- **Parameters**:
  - `n`: An integer to check for primality.
- **Returns**: `True` if the number is prime, otherwise `False`.

## Installation

### Environment Setup

This software does not require any external dependencies. You can run the code in any Python environment. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

## Usage

To use the `intersection` function, follow these steps:

1. **Open a Python Environment**: You can use a Python IDE or a terminal.
2. **Import the Function**: Ensure that the `intersection` function is accessible in your environment.
3. **Call the Function**: Use the function by passing two intervals as arguments.

### Example

```python
# Example usage of the intersection function
result1 = intersection((1, 2), (2, 3))
print(result1)  # Output: "NO"

result2 = intersection((-1, 1), (0, 4))
print(result2)  # Output: "NO"

result3 = intersection((-3, -1), (-5, 5))
print(result3)  # Output: "YES"
```

## Documentation

For further details on the implementation and logic of the intersection function, refer to the comments within the `main.py` file. The code is self-explanatory and includes inline comments to guide you through the logic.

## Support

For any issues or questions regarding the use of this software, please contact our support team. We are here to assist you in ensuring the software meets your needs effectively.