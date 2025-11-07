# Palindrome Utility

This software provides utility functions to work with palindromes. It includes functions to check if a string is a palindrome and to create the shortest palindrome from a given string.

## Main Functions

### 1. `is_palindrome(string: str) -> bool`

This function checks if a given string is a palindrome. A palindrome is a string that reads the same backward as forward.

**Usage:**

```python
is_palindrome('racecar')  # Returns: True
is_palindrome('hello')    # Returns: False
```

### 2. `make_palindrome(string: str) -> str`

This function generates the shortest palindrome that starts with the supplied string. It works by finding the longest postfix of the string that is a palindrome and appending the reverse of the prefix that comes before this palindromic suffix.

**Usage:**

```python
make_palindrome('cat')   # Returns: 'catac'
make_palindrome('cata')  # Returns: 'catac'
make_palindrome('')      # Returns: ''
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required since there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run a Python interpreter and import the functions:

```bash
python
```

```python
from main import is_palindrome, make_palindrome

# Example usage
print(is_palindrome('racecar'))  # Output: True
print(make_palindrome('cat'))    # Output: 'catac'
```

4. You can now use the functions `is_palindrome` and `make_palindrome` as demonstrated above.

## Documentation

For further information and examples, please refer to the docstrings provided in the `main.py` file. The docstrings include detailed descriptions and example usages for each function.