# Palindrome Checker

This software provides a simple function to check if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

## Main Function

The main function provided by this software is `is_palindrome(text: str) -> bool`. It checks if the given string is a palindrome and returns `True` if it is, otherwise `False`.

### Function Details

- **Input**: A string `text`.
- **Output**: A boolean value:
  - `True` if the input string is a palindrome.
  - `False` if the input string is not a palindrome.

### Example Usage

```python
>>> is_palindrome('')
True
>>> is_palindrome('aba')
True
>>> is_palindrome('aaaaa')
True
>>> is_palindrome('zbcd')
False
```

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function in a Python script or an interactive Python shell.

### Example

To use the `is_palindrome` function, you can include it in your Python script as follows:

```python
from main import is_palindrome

# Test the function
print(is_palindrome('racecar'))  # Output: True
print(is_palindrome('hello'))    # Output: False
```

## Documentation

For further information and examples, refer to the docstring provided in the `main.py` file. The docstring includes usage examples and expected outputs for various input cases.

This software is designed to be simple and efficient, focusing solely on checking palindromes without any additional features or dependencies.