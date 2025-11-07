# Palindrome Checker

This software provides a simple function to check if a given string is a palindrome. A palindrome is a string that reads the same forward and backward, such as "aba" or "racecar".

## Quick Install

This project does not require any external dependencies, so you can run it with a standard Python installation. Ensure you have Python installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

## How to Use

### Functionality

The main function provided by this software is `is_palindrome`, which checks if a given string is a palindrome.

### Usage

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder.

   ```bash
   cd <project-directory>
   ```

3. **Run the Function**: You can use the function in a Python script or an interactive Python session.

   ```python
   from main import is_palindrome

   # Examples
   print(is_palindrome(''))        # Output: True
   print(is_palindrome('aba'))     # Output: True
   print(is_palindrome('aaaaa'))   # Output: True
   print(is_palindrome('zbcd'))    # Output: False
   ```

### Testing

You can test the function using the provided examples in the docstring. Simply run the function with different strings to see if it correctly identifies palindromes.

## Documentation

The function `is_palindrome` is documented within the code with a docstring that provides examples of usage. You can view this documentation by accessing the function's `__doc__` attribute in Python.

```python
print(is_palindrome.__doc__)
```

This will display the function's description, parameters, return values, and examples.

## Conclusion

This software provides a straightforward way to check for palindromes in strings using Python. It is easy to integrate into other projects or use as a standalone utility. Enjoy exploring palindromes with this simple tool!