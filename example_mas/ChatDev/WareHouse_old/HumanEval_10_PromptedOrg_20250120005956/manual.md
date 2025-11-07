# Palindrome Utility

This software provides utility functions to work with palindromes. It includes functions to check if a string is a palindrome and to create the shortest palindrome that starts with a given string.

## Main Functions

### `is_palindrome(string: str) -> bool`

This function checks if the given string is a palindrome. A palindrome is a string that reads the same backward as forward.

**Usage:**

```python
is_palindrome("racecar")  # Returns: True
is_palindrome("hello")    # Returns: False
```

### `make_palindrome(string: str) -> str`

This function finds the shortest palindrome that begins with the supplied string. It works by finding the longest palindromic suffix of the string and appending the reverse of the prefix that comes before this suffix.

**Usage:**

```python
make_palindrome("")       # Returns: ""
make_palindrome("cat")    # Returns: "catac"
make_palindrome("cata")   # Returns: "catac"
```

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

## How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change your working directory to the location where you cloned the repository:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code:**

   You can run the functions directly in a Python environment. Open a Python shell or create a Python script and import the functions:

   ```python
   from main import is_palindrome, make_palindrome

   # Example usage
   print(is_palindrome("racecar"))  # Output: True
   print(make_palindrome("cat"))    # Output: "catac"
   ```

## Documentation

For further details on how to use the functions, refer to the docstrings provided in the code. Each function includes examples and explanations of its behavior.

This utility is designed to be simple and efficient, focusing on solving specific problems related to palindromes. Feel free to integrate it into larger projects or use it for educational purposes.