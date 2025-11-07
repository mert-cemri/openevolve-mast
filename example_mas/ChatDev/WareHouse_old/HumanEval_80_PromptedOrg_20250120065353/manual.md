# is_happy Function User Manual

Welcome to the user manual for the `is_happy` function. This document will guide you through the purpose of the function, how to install any necessary dependencies, and how to use the function effectively.

## Introduction

The `is_happy` function is a simple utility designed to determine whether a given string is "happy." A string is considered happy if its length is at least 3 and every set of 3 consecutive letters within the string are distinct. This function is useful for validating strings based on this specific criterion.

### Main Functionality

- **is_happy(s)**: This function takes a single argument, `s`, which is a string. It returns `True` if the string is happy, and `False` otherwise.

### Examples

- `is_happy("a")` returns `False`
- `is_happy("aa")` returns `False`
- `is_happy("abcd")` returns `True`
- `is_happy("aabb")` returns `False`
- `is_happy("adb")` returns `True`
- `is_happy("xyy")` returns `False`

## Installation

The `is_happy` function does not require any external dependencies. It is implemented in pure Python, so you only need a Python environment to run it.

### Setting Up Your Environment

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Code**: Obtain the `main.py` file containing the `is_happy` function. You can clone the repository or download the file directly.

3. **Run the Function**: You can run the function in any Python environment, such as a terminal, command prompt, or an integrated development environment (IDE) like PyCharm or VSCode.

## Usage

To use the `is_happy` function, follow these steps:

1. **Open your Python environment**: This could be a terminal, command prompt, or an IDE.

2. **Import the Function**: If you have saved the `main.py` file in your project, you can import the function using:
   ```python
   from main import is_happy
   ```

3. **Call the Function**: Pass a string to the `is_happy` function to check if it is happy:
   ```python
   result = is_happy("your_string_here")
   print(result)
   ```

4. **Interpret the Result**: The function will return `True` if the string is happy and `False` otherwise.

## Conclusion

The `is_happy` function is a straightforward utility for checking the happiness of strings based on the distinctness of every 3 consecutive characters. With no external dependencies, it is easy to integrate into any Python project. Enjoy using the `is_happy` function to validate your strings!