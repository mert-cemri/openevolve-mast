# Palindrome Utility

This software provides utility functions to work with palindromes. It includes functions to check if a string is a palindrome and to create the shortest palindrome from a given string.

## Main Functions

### 1. `is_palindrome(string: str) -> bool`

This function checks if the given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

**Usage:**

```python
is_palindrome("racecar")  # Returns: True
is_palindrome("hello")    # Returns: False
```

### 2. `make_palindrome(string: str) -> str`

This function finds the shortest palindrome that begins with the supplied string. It works by finding the longest postfix of the supplied string that is a palindrome and appending the reverse of the string prefix that comes before the palindromic suffix.

**Usage:**

```python
make_palindrome("")       # Returns: ""
make_palindrome("cat")    # Returns: "catac"
make_palindrome("cata")   # Returns: "catac"
```

## Installation

No external packages are required to run this software. It is implemented purely in Python.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

Clone the repository or download the `main.py` file to your local machine.

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory where `main.py` is located.
3. Run Python in interactive mode or create a script to use the functions.

### Example

```bash
python
```

```python
from main import is_palindrome, make_palindrome

print(is_palindrome("racecar"))  # Output: True
print(make_palindrome("cat"))    # Output: "catac"
```

## Documentation

For further information and examples, refer to the inline documentation within the `main.py` file. Each function includes a docstring explaining its purpose and usage.

This utility is designed to be simple and efficient, focusing on providing core functionality for palindrome operations without any unnecessary complexity.