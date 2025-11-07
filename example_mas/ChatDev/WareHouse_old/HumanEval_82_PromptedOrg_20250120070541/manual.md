# Prime Length Checker

This software module provides a function to determine if the length of a given string is a prime number. It is designed to be simple and efficient, with no external dependencies required.

## Quick Install

Since there are no external dependencies, you can directly use the provided Python code without any additional installation steps.

## 🤔 What is this?

This module is a utility for checking if the length of a string is a prime number. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. This functionality can be useful in various applications where string length characteristics are important.

## Main Functions

### `prime_length(string)`

- **Description**: This function takes a string as input and returns `True` if the length of the string is a prime number, and `False` otherwise.
- **Parameters**: 
  - `string` (str): The input string whose length is to be checked.
- **Returns**: 
  - `bool`: `True` if the length of the string is a prime number, `False` otherwise.

### `is_prime(n)`

- **Description**: This helper function checks if a given number `n` is a prime number.
- **Parameters**: 
  - `n` (int): The number to check for primality.
- **Returns**: 
  - `bool`: `True` if `n` is a prime number, `False` otherwise.

## How to Use

1. **Copy the Code**: Copy the provided Python code into a file named `main.py`.

2. **Run the Code**: You can use the `prime_length` function in your Python environment. Here is an example of how to use it:

    ```python
    from main import prime_length

    print(prime_length('Hello'))    # Output: True
    print(prime_length('abcdcba'))  # Output: True
    print(prime_length('kittens'))  # Output: True
    print(prime_length('orange'))   # Output: False
    ```

3. **No External Dependencies**: There are no additional libraries or dependencies required to use this module. Simply ensure you have Python installed on your system.

## Documentation

For further details on how the functions work, you can refer to the comments within the code. The logic for checking prime numbers is implemented efficiently to handle typical string lengths encountered in most applications.