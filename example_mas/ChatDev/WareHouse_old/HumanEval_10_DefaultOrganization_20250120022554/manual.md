# Palindrome Utility

This software provides utility functions to work with palindromes. It includes functions to check if a string is a palindrome and to create the shortest palindrome starting with a given string.

## Main Functions

### `is_palindrome(string: str) -> bool`

This function checks if a given string is a palindrome. A palindrome is a string that reads the same backward as forward.

- **Parameters**: 
  - `string` (str): The string to be checked.
- **Returns**: 
  - `bool`: `True` if the string is a palindrome, `False` otherwise.

### `make_palindrome(string: str) -> str`

This function finds the shortest palindrome that begins with a supplied string. The algorithm works by finding the longest postfix of the supplied string that is a palindrome and appending the reverse of the string prefix that comes before the palindromic suffix.

- **Parameters**: 
  - `string` (str): The string to be transformed into a palindrome.
- **Returns**: 
  - `str`: The shortest palindrome starting with the supplied string.

## Installation

This project does not require any external dependencies. You can run the code using Python without installing any additional packages.

## Usage

To use the functions provided by this software, follow these steps:

1. **Clone the Repository**: 
   - Clone the repository to your local machine.

2. **Navigate to the Project Directory**: 
   - Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Script**: 
   - Execute the script using Python to see the example usage:
     ```bash
     python main.py
     ```

4. **Example Usage**:
   - The script includes example usage of the `make_palindrome` function:
     ```python
     print(make_palindrome(''))  # Output: ''
     print(make_palindrome('cat'))  # Output: 'catac'
     print(make_palindrome('cata'))  # Output: 'catac'
     ```

## Documentation

The code is documented with docstrings explaining the purpose and usage of each function. You can refer to these docstrings for a quick understanding of how each function works.

For further assistance or inquiries, please contact our support team.