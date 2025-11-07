# Happy String Checker

This software provides a simple utility function to determine if a given string is "happy". A string is considered "happy" if its length is at least 3 and every 3 consecutive letters are distinct.

## Main Functionality

The main function provided by this software is `is_happy(s)`, which checks if a string `s` meets the criteria for being "happy".

### Function Definition

```python
def is_happy(s):
    """Check if the string s is happy.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
    Args:
    s (str): The string to check.
    Returns:
    bool: True if the string is happy, False otherwise.
    """
```

### How It Works

- The function first checks if the length of the string is less than 3. If so, it returns `False` because a string must be at least 3 characters long to be considered "happy".
- It then iterates over the string, checking every set of 3 consecutive characters.
- If any set of 3 consecutive characters contains duplicates, the function returns `False`.
- If all sets of 3 consecutive characters are distinct, the function returns `True`.

## Installation

This software does not require any external dependencies. It is implemented in pure Python and can be used in any environment where Python is installed.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can use the function in a Python script or an interactive Python session. Here is an example of how to use it:

```python
from main import is_happy

# Test the function with different strings
print(is_happy("a"))        # Output: False
print(is_happy("aa"))       # Output: False
print(is_happy("abcd"))     # Output: True
print(is_happy("aabb"))     # Output: False
print(is_happy("adb"))      # Output: True
print(is_happy("xyy"))      # Output: False
```

## Documentation

This software is straightforward and does not require extensive documentation. The function `is_happy(s)` is self-contained and can be easily integrated into larger projects that require checking for "happy" strings.

For further assistance or questions, please contact the development team at ChatDev.