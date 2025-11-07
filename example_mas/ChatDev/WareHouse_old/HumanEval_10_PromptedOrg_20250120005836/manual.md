# Palindrome Utility

This software provides utility functions to work with palindromes. It includes functions to check if a string is a palindrome and to create the shortest palindrome from a given string.

## Main Functions

### `is_palindrome`

- **Description**: This function checks if a given string is a palindrome.
- **Usage**: 
  ```python
  is_palindrome(string: str) -> bool
  ```
- **Parameters**: 
  - `string`: The string to be checked.
- **Returns**: 
  - `True` if the string is a palindrome, `False` otherwise.

### `make_palindrome`

- **Description**: This function finds the shortest palindrome that begins with a supplied string.
- **Usage**: 
  ```python
  make_palindrome(string: str) -> str
  ```
- **Parameters**: 
  - `string`: The string to be transformed into a palindrome.
- **Returns**: 
  - The shortest palindrome that starts with the given string.

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

## How to Use

1. **Clone the Repository**: 
   - Clone the repository to your local machine using:
     ```bash
     git clone <repository-url>
     ```
   - Navigate to the directory:
     ```bash
     cd <repository-directory>
     ```

2. **Run the Code**:
   - You can use the functions in your Python scripts by importing them:
     ```python
     from main import is_palindrome, make_palindrome
     ```
   - Example usage:
     ```python
     print(is_palindrome("racecar"))  # Output: True
     print(make_palindrome("cat"))    # Output: "catac"
     ```

3. **Testing**:
   - You can test the functions using the provided examples in the docstring:
     ```python
     assert make_palindrome('') == ''
     assert make_palindrome('cat') == 'catac'
     assert make_palindrome('cata') == 'catac'
     ```

## Documentation

For more detailed documentation, please refer to the docstrings provided in the `main.py` file. Each function includes a description, usage, parameters, and return values.

Feel free to reach out if you have any questions or need further assistance!