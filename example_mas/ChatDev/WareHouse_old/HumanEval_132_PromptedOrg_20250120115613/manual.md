# is_nested Function User Manual

## Introduction

The `is_nested` function is a Python utility designed to determine if a string composed solely of square brackets contains a valid subsequence where at least one bracket is nested. This function is particularly useful for validating bracket sequences in programming and mathematical expressions.

## Main Functionality

- **Function Name**: `is_nested`
- **Input**: A string containing only square brackets (`[` and `]`).
- **Output**: A boolean value (`True` or `False`).
  - Returns `True` if there is a valid subsequence of brackets where at least one bracket is nested.
  - Returns `False` otherwise.

### Example Usages

- `is_nested('[[]]')` ➞ `True`
- `is_nested('[]]]]]]][[[[[]')` ➞ `False`
- `is_nested('[][]')` ➞ `False`
- `is_nested('[]')` ➞ `False`
- `is_nested('[[][]]')` ➞ `True`
- `is_nested('[[]][[')` ➞ `True`

## Installation

This project does not require any external dependencies. You only need Python installed on your system to use the `is_nested` function.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `is_nested` function.

2. **Run the Function**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the `main.py` file.
   - Run the Python interpreter and import the function:
     ```bash
     python
     >>> from main import is_nested
     >>> print(is_nested('[[]]'))
     True
     ```

3. **Integrate into Your Project**:
   - Copy the `is_nested` function into your Python script.
   - Use it to validate bracket sequences as needed.

## Documentation

The `is_nested` function uses a stack-based approach to determine if a sequence of brackets is nested. It iterates through each character in the string, pushing opening brackets onto a stack and popping them when a closing bracket is encountered. If a closing bracket is encountered while the stack is not empty, it indicates nesting.

For more detailed information on how the function works, refer to the comments within the `main.py` file.

## Support

For further assistance or inquiries, please contact our support team at support@chatdev.com. We are here to help you with any questions or issues you may encounter while using the `is_nested` function.