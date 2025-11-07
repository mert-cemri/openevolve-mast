# Prime Length Checker

This software module provides a simple utility to check if the length of a given string is a prime number. It is implemented in Python and does not require any external dependencies.

## Main Functions

### `prime_length(string)`

- **Description**: This function takes a string as input and returns `True` if the length of the string is a prime number, and `False` otherwise.
- **Usage**: 
  ```python
  result = prime_length("Hello")
  print(result)  # Output: True
  ```

### `is_prime(n)`

- **Description**: This is a helper function used by `prime_length` to determine if a given number `n` is a prime number.
- **Usage**: 
  ```python
  is_prime_number = is_prime(5)
  print(is_prime_number)  # Output: True
  ```

## Installation

This software does not require any external packages, so there is no need to install additional dependencies. It is implemented in pure Python.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Code**: You can use the functions directly in your Python scripts. Simply import the `prime_length` function from the `main.py` file.

   ```python
   from main import prime_length

   # Example usage
   print(prime_length("Hello"))  # Output: True
   ```

3. **Testing**: You can test the function with different strings to check if the length is a prime number.

## Example

Here's a quick example to demonstrate the usage:

```python
from main import prime_length

# Test strings
strings = ["Hello", "abcdcba", "kittens", "orange"]

# Check if the length of each string is a prime number
for s in strings:
    print(f"The length of '{s}' is prime: {prime_length(s)}")
```

## Conclusion

This module provides a straightforward way to check if the length of a string is a prime number. It is efficient and easy to integrate into any Python project. Feel free to modify and extend the functionality as needed for your specific use case.