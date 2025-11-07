# Happy String Checker

This software provides a simple utility function to determine if a given string is "happy". A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.

## Main Functionality

The main function provided by this software is `is_happy(s)`. This function checks whether a given string `s` meets the criteria of being a "happy" string.

### Function: `is_happy(s)`

- **Input**: A string `s`.
- **Output**: A boolean value (`True` or `False`).
  - Returns `True` if the string is happy.
  - Returns `False` if the string is not happy.

#### Examples:

- `is_happy("a")` => `False`
- `is_happy("aa")` => `False`
- `is_happy("abcd")` => `True`
- `is_happy("aabb")` => `False`
- `is_happy("adb")` => `True`
- `is_happy("xyy")` => `False`

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Otherwise, download the `main.py` file.

3. **No Additional Dependencies**: There are no additional packages to install, as specified in the `requirements.txt` file.

## Usage

To use the `is_happy` function, follow these steps:

1. **Open a Terminal or Command Prompt**: Navigate to the directory where `main.py` is located.

2. **Run Python Interpreter**: You can test the function directly in the Python interpreter or by creating a script.

### Example Usage in Python Interpreter

```bash
python
```

```python
from main import is_happy

# Test the function with different strings
print(is_happy("abcd"))  # Output: True
print(is_happy("aabb"))  # Output: False
```

### Example Usage in a Python Script

Create a new Python file, for example `test_happy.py`, and add the following code:

```python
from main import is_happy

# Test the function
print(is_happy("abcd"))  # Output: True
print(is_happy("aabb"))  # Output: False
```

Run the script using:

```bash
python test_happy.py
```

## Conclusion

This software provides a simple yet effective way to determine if a string is "happy". With no external dependencies, it is easy to integrate into any Python project. Enjoy using the Happy String Checker!