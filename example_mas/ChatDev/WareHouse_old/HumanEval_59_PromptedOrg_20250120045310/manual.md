# Largest Prime Factor Finder

This software module provides a function to find the largest prime factor of a given integer. It is designed to be simple and efficient, suitable for use in various applications where prime factorization is required.

## Main Function

The main function provided by this module is:

### `largest_prime_factor(n: int) -> int`

- **Description**: This function returns the largest prime factor of the integer `n`. It assumes that `n` is greater than 1 and is not a prime number itself.
- **Parameters**: 
  - `n` (int): The integer for which the largest prime factor is to be found.
- **Returns**: 
  - (int): The largest prime factor of `n`.
- **Example Usage**:
  ```python
  >>> largest_prime_factor(13195)
  29
  >>> largest_prime_factor(2048)
  2
  ```

## Installation

To use this software, you need to have Python installed on your system. The module does not require any external dependencies, so no additional packages need to be installed.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the code by cloning the repository or downloading the files directly.

3. **Navigate to the directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

## Usage

To use the `largest_prime_factor` function, follow these steps:

1. **Open a Python environment**: You can use a Python interpreter, a script, or an integrated development environment (IDE) like PyCharm or VSCode.

2. **Import the function**: If you're using a script or an interactive Python session, import the function from the module.

   ```python
   from main import largest_prime_factor
   ```

3. **Call the function**: Pass the integer for which you want to find the largest prime factor.

   ```python
   result = largest_prime_factor(13195)
   print(result)  # Output: 29
   ```

## Documentation

This module is straightforward and does not include additional documentation beyond this manual. The function is designed to be self-contained and easy to integrate into larger projects.

For any further questions or support, please contact our development team. We are here to assist you in integrating this module into your applications effectively.