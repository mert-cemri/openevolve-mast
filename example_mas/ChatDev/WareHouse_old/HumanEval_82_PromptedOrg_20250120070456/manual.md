# Prime Length Checker

This software provides a simple utility function to determine if the length of a given string is a prime number. It is designed to be lightweight and requires no external dependencies.

## Main Functionality

The primary function of this software is `prime_length`, which checks if the length of a given string is a prime number. It utilizes an internal helper function `is_prime` to determine the primality of the string length.

### Functions

- **is_prime(n)**: A helper function that checks if a number `n` is a prime number.
  - Returns `True` if `n` is a prime number, otherwise returns `False`.

- **prime_length(string)**: The main function that takes a string as input and returns `True` if the length of the string is a prime number, otherwise returns `False`.

### Examples

- `prime_length('Hello')` returns `True`
- `prime_length('abcdcba')` returns `True`
- `prime_length('kittens')` returns `True`
- `prime_length('orange')` returns `False`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply download the `main.py` file to your local environment.

## How to Use

1. **Download the Code**: Ensure you have the `main.py` file in your working directory.

2. **Run the Function**: You can use the `prime_length` function by importing it into your Python script or by running it directly in a Python environment.

   Example usage in a Python script:
   ```python
   from main import prime_length

   result = prime_length('Hello')
   print(result)  # Output: True
   ```

3. **Testing**: You can test the function with different strings to verify its functionality.

## No External Dependencies

This software is designed to be minimalistic and does not require any additional Python packages. You can run it in any standard Python environment without needing to install anything extra.

## Conclusion

The Prime Length Checker is a straightforward utility for determining the primality of string lengths. It is ideal for educational purposes, small projects, or any application where you need to check the prime status of string lengths quickly and efficiently.