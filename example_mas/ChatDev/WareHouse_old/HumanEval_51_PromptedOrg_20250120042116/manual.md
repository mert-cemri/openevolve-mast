manual.md

```
# Remove Vowels Function

This software provides a simple function to remove vowels from a given string. It is implemented in Python and is designed to be straightforward and efficient.

## Main Functionality

The main function of this software is `remove_vowels`, which takes a string as input and returns a new string with all vowels removed. The function handles both uppercase and lowercase vowels.

### Example Usage

```python
from main import remove_vowels

# Example usage
print(remove_vowels("abcdef\nghijklm"))  # Output: 'bcdf\nghjklm'
print(remove_vowels("abcdef"))           # Output: 'bcdf'
print(remove_vowels("aaaaa"))            # Output: ''
print(remove_vowels("aaBAA"))            # Output: 'B'
print(remove_vowels("zbcd"))             # Output: 'zbcd'
```

## Installation

To use this software, you need to have Python installed on your system. The function does not require any additional dependencies, so no installation of external packages is necessary.

### Step-by-Step Installation Guide

1. **Install Python**: Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

3. **Run the Function**: You can run the function directly in a Python environment or script by importing it from `main.py`.

## How to Use

1. **Import the Function**: Import the `remove_vowels` function from the `main.py` file into your Python script or interactive environment.

2. **Call the Function**: Pass a string to the `remove_vowels` function to get a new string with vowels removed.

3. **View the Result**: The function will return the modified string, which you can print or use in further processing.

## Documentation

The function is documented with examples in the docstring. You can view these examples by accessing the function's docstring in your Python environment.

For further information or support, please contact our development team.

```