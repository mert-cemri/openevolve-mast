# Palindrome Utility

This software provides utility functions to work with palindromes, specifically to check if a string is a palindrome and to create the shortest palindrome by appending characters to the end of a given string.

## Main Functions

### 1. `is_palindrome(string: str) -> bool`

This function checks if the given string is a palindrome. A palindrome is a string that reads the same forward and backward.

**Usage:**

```python
result = is_palindrome("racecar")  # Returns: True
result = is_palindrome("hello")    # Returns: False
```

### 2. `make_palindrome(string: str) -> str`

This function finds the shortest palindrome that begins with the supplied string. It works by finding the longest postfix of the string that is a palindrome and appending the reverse of the prefix that comes before this palindromic suffix.

**Usage:**

```python
result = make_palindrome("")       # Returns: ""
result = make_palindrome("cat")    # Returns: "catac"
result = make_palindrome("cata")   # Returns: "catac"
```

## Installation

This software does not require any external dependencies, making it easy to set up and use.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py`.

4. No additional installation steps are required since there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory containing the `main.py` file.

3. You can use the functions by importing them into your Python script or interactive session. For example:

```python
from main import is_palindrome, make_palindrome

# Check if a string is a palindrome
print(is_palindrome("racecar"))  # Output: True

# Create the shortest palindrome
print(make_palindrome("cat"))    # Output: "catac"
```

4. Alternatively, you can directly modify the `main.py` file to test the functions with different inputs.

## Documentation

For more information on how the functions work, refer to the docstrings provided in the `main.py` file. These provide detailed explanations and examples of how to use each function.