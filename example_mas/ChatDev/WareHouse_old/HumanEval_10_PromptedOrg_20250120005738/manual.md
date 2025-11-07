# Palindrome Utility

This software provides utility functions to work with palindromes. It includes functions to check if a string is a palindrome and to create the shortest palindrome from a given string.

## Quick Install

No external dependencies are required for this software. Simply ensure you have Python installed on your system.

## 🤔 What is this?

This software is designed to help you work with palindromes in Python. A palindrome is a string that reads the same forwards and backwards. This utility provides two main functions:

1. **`is_palindrome(string: str) -> bool`**: This function checks if a given string is a palindrome.

2. **`make_palindrome(string: str) -> str`**: This function generates the shortest palindrome that begins with the supplied string.

## 📖 Documentation

### Main Functions

- **`is_palindrome(string: str) -> bool`**

  - **Description**: Tests if the given string is a palindrome.
  - **Parameters**: 
    - `string` (str): The string to be tested.
  - **Returns**: 
    - `bool`: `True` if the string is a palindrome, `False` otherwise.

- **`make_palindrome(string: str) -> str`**

  - **Description**: Finds the shortest palindrome that begins with the supplied string.
  - **Parameters**: 
    - `string` (str): The string to be transformed into a palindrome.
  - **Returns**: 
    - `str`: The shortest palindrome starting with the given string.

### How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Code**: You can test the functions by running the `main.py` file in a Python environment.

   ```bash
   python main.py
   ```

4. **Example Usage**:

   ```python
   # Import the functions
   from main import is_palindrome, make_palindrome

   # Check if a string is a palindrome
   print(is_palindrome("racecar"))  # Output: True

   # Create the shortest palindrome from a string
   print(make_palindrome("cat"))  # Output: "catac"
   ```

### Getting Started

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

- No additional packages are required, so you can directly run the Python script.

This utility is a simple yet powerful tool for anyone needing to work with palindromes in Python. Enjoy using it for your projects!