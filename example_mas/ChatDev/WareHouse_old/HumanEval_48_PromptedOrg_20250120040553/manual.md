# Palindrome Checker

This software provides a simple function to check if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

## Main Function

The main function of this software is `is_palindrome(text: str) -> bool`. It checks if the input string `text` is a palindrome and returns `True` if it is, and `False` otherwise.

### Function Details

- **Function Name:** `is_palindrome`
- **Input:** A string `text`
- **Output:** A boolean value (`True` or `False`)
- **Description:** The function checks if the given string is a palindrome by comparing the string with its reverse.

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

This software does not require any external dependencies, so there is no need for a `requirements.txt` file. You can directly use the function in your Python environment.

## How to Use

1. **Clone the Repository:**
   - Clone the repository to your local machine.

2. **Navigate to the Directory:**
   - Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function:**
   - You can use the function by importing it into your Python script or interactive shell.
   - Example:
     ```python
     from main import is_palindrome

     print(is_palindrome('racecar'))  # Output: True
     print(is_palindrome('hello'))    # Output: False
     ```

4. **Testing:**
   - You can test the function using the provided examples in the function's docstring.

## Documentation

For more information on how to use the function, refer to the docstring within the `main.py` file. The docstring provides example usages and expected outputs.

This software is designed to be simple and straightforward, focusing solely on checking if a string is a palindrome. If you have any questions or need further assistance, please contact our support team.