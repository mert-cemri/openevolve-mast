# is_nested Function User Manual

## Introduction

The `is_nested` function is a simple Python utility designed to determine if a given string of square brackets contains a valid subsequence where at least one bracket is nested. This function can be useful in scenarios where you need to validate the structure of bracket sequences, such as in parsing tasks or syntax checking.

## Main Functionality

The primary function provided by this software is:

- **is_nested(string):** This function takes a single string input consisting only of square brackets ('[' and ']'). It returns `True` if there exists a valid subsequence of brackets where at least one bracket is nested, and `False` otherwise.

### Example Usage

```python
print(is_nested('[[]]'))          # Output: True
print(is_nested('[]]]]]]][[[[[]')) # Output: False
print(is_nested('[][]'))          # Output: False
print(is_nested('[]'))            # Output: False
print(is_nested('[[][]]'))        # Output: True
print(is_nested('[[]][['))        # Output: True
```

## Installation

### Environment Setup

This project does not require any external dependencies, so setting up the environment is straightforward. You only need to have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download it from the official Python website: [python.org](https://www.python.org/). Follow the instructions for your operating system to install Python.

### Running the Code

1. **Clone the Repository:**
   - Download or clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory:**
   - Open a terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Script:**
   - Execute the script using Python by running the following command:
     ```bash
     python main.py
     ```

## How to Use

To use the `is_nested` function, you can either import it into another Python script or run it directly from the `main.py` file. Here’s how you can use it in a Python script:

```python
from main import is_nested

# Test the function with different inputs
print(is_nested('[[]]'))          # Output: True
print(is_nested('[]]]]]]][[[[[]')) # Output: False
```

## Conclusion

The `is_nested` function is a simple yet effective tool for checking nested bracket sequences. With no external dependencies, it is easy to integrate into existing Python projects. Whether you are working on parsing tasks or need to validate bracket structures, this function provides a straightforward solution.