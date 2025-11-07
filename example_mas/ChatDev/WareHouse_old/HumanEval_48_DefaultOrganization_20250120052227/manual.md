manual.md

```
# Palindrome Checker

A simple Python application to check if a given string is a palindrome.

## Introduction

The Palindrome Checker is a straightforward Python function that determines whether a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

## Main Function

The main function provided in this application is `is_palindrome(text: str) -> bool`. This function takes a single argument, `text`, which is a string, and returns a boolean value: `True` if the string is a palindrome, and `False` otherwise.

### Function Signature

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]
```

## Installation

This application does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download Python from the official website [here](https://www.python.org/downloads/).

2. **Clone the repository or download the script**: Obtain the `main.py` file containing the `is_palindrome` function.

3. **Run the script**: You can execute the script using a Python interpreter to test the function.

## Usage

To use the Palindrome Checker, follow these steps:

1. **Open a terminal or command prompt**.

2. **Navigate to the directory containing `main.py`**.

3. **Run the Python interpreter** and import the function:

   ```bash
   python
   ```

4. **Import the function and test it**:

   ```python
   from main import is_palindrome

   # Test the function with different inputs
   print(is_palindrome(''))         # Output: True
   print(is_palindrome('aba'))      # Output: True
   print(is_palindrome('aaaaa'))    # Output: True
   print(is_palindrome('zbcd'))     # Output: False
   ```

## Documentation

The function is self-documented with a docstring that includes examples of how to use it. You can also run the function with different inputs to see how it behaves with various strings.

This application is designed to be simple and efficient, with no additional setup or dependencies required. Enjoy checking palindromes with ease!
```