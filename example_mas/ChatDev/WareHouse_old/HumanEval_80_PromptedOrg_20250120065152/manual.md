# is_happy Function User Manual

## Introduction

The `is_happy` function is a simple Python utility designed to determine whether a given string is "happy." A string is considered happy if it meets the following criteria:
- The string has a length of at least 3 characters.
- Every set of 3 consecutive characters in the string are distinct.

This function can be useful in various applications where pattern recognition or validation of character sequences is required.

## Main Functionality

The primary function provided by this software is:

- **is_happy(s):** Takes a string `s` as input and returns `True` if the string is happy, otherwise returns `False`.

### Examples

- `is_happy("a")` returns `False`
- `is_happy("aa")` returns `False`
- `is_happy("abcd")` returns `True`
- `is_happy("aabb")` returns `False`
- `is_happy("adb")` returns `True`
- `is_happy("xyy")` returns `False`

## Installation

This software does not require any external dependencies beyond a standard Python environment. To use the `is_happy` function, ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

## Usage

1. **Clone or Download the Repository:**
   - You can clone the repository using Git or download the files directly.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Function:**
   - You can use the function by importing it into your Python script or by directly running the `main.py` file in a Python environment.

### Example Usage in a Python Script

```python
from main import is_happy

# Test the function with various strings
print(is_happy("abcd"))  # Output: True
print(is_happy("aabb"))  # Output: False
```

### Running Directly from Command Line

You can also test the function directly by running the `main.py` file and modifying it to include test cases.

```bash
python main.py
```

## Conclusion

The `is_happy` function is a straightforward utility for checking the distinctiveness of consecutive character sequences in a string. It is easy to integrate into existing Python projects and requires no additional dependencies. Feel free to modify and expand upon this function to suit your specific needs.