# Palindrome Checker

This software provides a simple function to check if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

## Main Functionality

The main function of this software is:

- **is_palindrome(text: str) -> bool**: This function takes a string as input and returns `True` if the string is a palindrome, and `False` otherwise.

### Examples

- `is_palindrome('')` returns `True`
- `is_palindrome('aba')` returns `True`
- `is_palindrome('aaaaa')` returns `True`
- `is_palindrome('zbcd')` returns `False`

## Installation

This software does not require any external dependencies. You can use it directly with Python.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required since there are no external dependencies.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. You can test the function using Python's interactive shell or by creating a script. For example, to test the function in the interactive shell:

   ```bash
   python
   ```

   Then, in the Python shell, you can import the function and test it:

   ```python
   from main import is_palindrome

   print(is_palindrome('aba'))  # Output: True
   print(is_palindrome('zbcd')) # Output: False
   ```

4. Alternatively, you can create a Python script to test the function:

   ```python
   # test_palindrome.py
   from main import is_palindrome

   print(is_palindrome(''))      # Output: True
   print(is_palindrome('aba'))   # Output: True
   print(is_palindrome('aaaaa')) # Output: True
   print(is_palindrome('zbcd'))  # Output: False
   ```

   Run the script using:

   ```bash
   python test_palindrome.py
   ```

## Documentation

The function is documented with examples in the docstring. You can view the documentation by using Python's built-in help function:

```python
help(is_palindrome)
```

This will display the function's docstring, which includes example usage and expected output.