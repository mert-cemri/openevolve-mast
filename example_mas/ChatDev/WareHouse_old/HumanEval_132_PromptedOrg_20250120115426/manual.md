# is_nested Function User Manual

## Introduction

The `is_nested` function is a Python utility designed to determine whether a given string of square brackets contains a valid subsequence where at least one bracket is nested. This function is useful for validating bracket sequences in various applications, such as parsing expressions or checking the correctness of nested structures.

## Main Functionality

The main function provided by this software is:

- `is_nested(string)`: This function takes a string as input, which contains only square brackets ('[' and ']'). It returns `True` if there is a valid subsequence of brackets where at least one bracket is nested, and `False` otherwise.

### Example Usage

```python
print(is_nested('[[]]'))  # Output: True
print(is_nested('[]]]]]]][[[[[]'))  # Output: False
print(is_nested('[][]'))  # Output: False
print(is_nested('[]'))  # Output: False
print(is_nested('[[][]]'))  # Output: True
print(is_nested('[[]][['))  # Output: True
```

## Installation

### Environment Setup

This software does not require any external dependencies, making it straightforward to set up and use. You only need to have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download it from the official Python website: [python.org](https://www.python.org/downloads/). Follow the instructions for your operating system to complete the installation.

## How to Use

1. **Clone or Download the Repository:**
   - You can clone the repository or download the `main.py` file containing the `is_nested` function.

2. **Run the Code:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the Python script using the command:
     ```bash
     python main.py
     ```
   - You can modify the script to test different input strings by calling the `is_nested` function with various bracket sequences.

3. **Integrate into Your Project:**
   - You can copy the `is_nested` function into your own Python projects and use it as needed to validate bracket sequences.

## Conclusion

The `is_nested` function is a simple yet effective tool for checking nested bracket sequences in strings. With no external dependencies required, it is easy to integrate into any Python project. Use this function to ensure the correctness of nested structures in your applications.