# Prime Checker Software

This software provides a simple utility to determine if a given number is a prime number and returns a specified value based on the result. It is implemented in Python and is designed to be lightweight with no external dependencies.

## Main Functions

### `is_prime(n)`

- **Purpose**: Checks if a number `n` is a prime number.
- **Input**: An integer `n`.
- **Output**: Returns `True` if `n` is a prime number, otherwise returns `False`.

### `x_or_y(n, x, y)`

- **Purpose**: Returns the value of `x` if `n` is a prime number, otherwise returns the value of `y`.
- **Input**: 
  - `n`: An integer to check for primality.
  - `x`: The value to return if `n` is a prime number.
  - `y`: The value to return if `n` is not a prime number.
- **Output**: Returns `x` if `n` is prime, otherwise returns `y`.

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).
2. **Clone or download the repository**: Obtain the code files from the repository.
3. **Navigate to the directory**: Use your command line interface to navigate to the directory containing the `main.py` file.

## Usage

To use the software, you simply need to run the `main.py` file and call the `x_or_y` function with the appropriate arguments.

### Example

```python
# Example usage of the x_or_y function
result1 = x_or_y(7, 34, 12)  # Should return 34 because 7 is a prime number
result2 = x_or_y(15, 8, 5)   # Should return 5 because 15 is not a prime number

print(result1)  # Output: 34
print(result2)  # Output: 5
```

## Documentation

For further details on how the functions work, you can refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the program.

This software is designed to be simple and efficient, providing a quick way to check for prime numbers and return values based on the result. Enjoy using the Prime Checker Software!