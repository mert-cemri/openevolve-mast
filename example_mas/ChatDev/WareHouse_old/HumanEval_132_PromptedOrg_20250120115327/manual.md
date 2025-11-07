# is_nested Function User Manual

## Introduction

The `is_nested` function is a Python utility designed to determine whether a given string of square brackets contains a valid nested subsequence. The function evaluates the string and returns `True` if there is at least one nested bracket, and `False` otherwise.

### Key Features

- **Input:** A string consisting solely of square brackets (`[` and `]`).
- **Output:** A boolean value (`True` or `False`) indicating the presence of a nested bracket sequence.

### Example Usage

- `is_nested('[[]]')` returns `True`
- `is_nested('[]]]]]]][[[[[]')` returns `False`
- `is_nested('[][]')` returns `False`
- `is_nested('[]')` returns `False`
- `is_nested('[[][]]')` returns `True`
- `is_nested('[[]][[')` returns `True`

## Installation

The `is_nested` function does not require any external dependencies, making it straightforward to use. You only need a Python environment set up on your machine.

### Setting Up Your Environment

1. **Ensure Python is Installed:**
   - Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Verify Python Installation:**
   - Open your terminal or command prompt and run the following command to verify the installation:
     ```
     python --version
     ```
   - This should display the version of Python installed on your system.

3. **No Additional Dependencies:**
   - Since there are no external dependencies, you do not need to install any additional packages.

## How to Use

1. **Create a Python File:**
   - Create a new Python file, e.g., `main.py`.

2. **Implement the Function:**
   - Copy the following code into your `main.py` file:

     ```python
     def is_nested(string):
         stack = []
         nested = False
         for char in string:
             if char == '[':
                 stack.append(char)
             elif char == ']':
                 if stack:
                     stack.pop()
                     if stack:  # If stack is not empty after popping, it means there was nesting
                         nested = True
                 else:
                     return False
         return nested
     ```

3. **Run the Function:**
   - You can test the function by calling it with different strings of brackets. For example:

     ```python
     print(is_nested('[[]]'))  # Output: True
     print(is_nested('[]]]]]]][[[[[]'))  # Output: False
     ```

4. **Execute the Script:**
   - Run your script from the terminal or command prompt using the following command:
     ```
     python main.py
     ```

## Conclusion

The `is_nested` function is a simple yet effective tool for checking nested sequences in strings of square brackets. With no external dependencies, it is easy to integrate into any Python project. Use this function to ensure the correct nesting of brackets in your applications.