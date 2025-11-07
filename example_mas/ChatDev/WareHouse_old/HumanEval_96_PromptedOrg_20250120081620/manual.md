# Prime Number Finder

This software module provides a function to find all prime numbers less than a given non-negative integer. It is implemented in Python and does not require any external dependencies.

## Main Functions

### `count_up_to(n)`

- **Description**: This function takes a non-negative integer `n` and returns a list of all prime numbers less than `n`.
- **Parameters**: 
  - `n` (int): The non-negative integer limit.
- **Returns**: 
  - `list`: A list of prime numbers less than `n`.

### `is_prime(num)`

- **Description**: This helper function checks if a given number is a prime number.
- **Parameters**: 
  - `num` (int): The number to check.
- **Returns**: 
  - `bool`: `True` if `num` is a prime number, `False` otherwise.

## Installation

This software does not require any external dependencies, so there is no need to install additional packages. Ensure you have Python installed on your system.

## Usage

1. **Clone the Repository**: Clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing `main.py`.

3. **Run the Function**: You can run the function by executing the script in a Python environment. For example:

   ```python
   from main import count_up_to

   print(count_up_to(5))  # Output: [2, 3]
   print(count_up_to(11)) # Output: [2, 3, 5, 7]
   print(count_up_to(0))  # Output: []
   print(count_up_to(20)) # Output: [2, 3, 5, 7, 11, 13, 17, 19]
   ```

4. **Modify and Extend**: Feel free to modify the code to suit your needs or extend its functionality.

## Documentation

For further details on how the functions work, please refer to the docstrings provided in the code. Each function is documented with its purpose, parameters, and return values.

## Support

If you encounter any issues or have questions, please reach out to our support team for assistance. We are here to help you make the most of this software.