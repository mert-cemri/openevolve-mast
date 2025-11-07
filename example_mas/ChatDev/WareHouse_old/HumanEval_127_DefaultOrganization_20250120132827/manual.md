# Interval Intersection Prime Checker

This software provides a function to determine if the length of the intersection of two intervals is a prime number. It is designed to be simple and efficient, with no external dependencies required.

## Main Functions

### `intersection(interval1, interval2)`

- **Description**: This function takes two intervals as input and determines if the length of their intersection is a prime number.
- **Parameters**:
  - `interval1`: A tuple representing the first interval (start1, end1).
  - `interval2`: A tuple representing the second interval (start2, end2).
- **Returns**: 
  - `"YES"` if the length of the intersection is a prime number.
  - `"NO"` if the length of the intersection is not a prime number or if the intervals do not intersect.

### `is_prime(n)`

- **Description**: A helper function used to check if a given number is a prime number.
- **Parameters**:
  - `n`: An integer to check for primality.
- **Returns**: 
  - `True` if `n` is a prime number.
  - `False` otherwise.

## Installation

This software does not require any external dependencies, so you can use it directly without any additional installations. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Clone the repository to your local machine to access the `main.py` file.

2. **Run the Code**: You can run the code using any Python environment. Open the `main.py` file and use the `intersection` function to check the intersection of two intervals.

3. **Example Usage**:
   ```python
   from main import intersection

   result1 = intersection((1, 2), (2, 3))
   print(result1)  # Output: "NO"

   result2 = intersection((-1, 1), (0, 4))
   print(result2)  # Output: "NO"

   result3 = intersection((-3, -1), (-5, 5))
   print(result3)  # Output: "YES"
   ```

4. **Modify and Test**: Feel free to modify the intervals and test with different values to see how the function behaves.

## Documentation

For further details on how the function works, you can refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the program.

## Support

If you encounter any issues or have questions about using this software, please feel free to reach out for support. We are here to help you make the most out of this tool.