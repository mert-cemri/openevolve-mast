# Correct Bracketing Software

This software provides a simple utility function to check if a string of brackets ("<" and ">") is correctly bracketed. It ensures that every opening bracket has a corresponding closing bracket in the correct order.

## Main Function

The main function provided by this software is `correct_bracketing`. It takes a string of brackets as input and returns a boolean value indicating whether the brackets are correctly matched.

### Function Signature

```python
def correct_bracketing(brackets: str) -> bool:
```

### Functionality

- **Input**: A string consisting of the characters "<" and ">".
- **Output**: Returns `True` if every opening bracket has a corresponding closing bracket in the correct order. Returns `False` otherwise.

### Examples

```python
correct_bracketing("<")       # Returns: False
correct_bracketing("<>")      # Returns: True
correct_bracketing("<<><>>")  # Returns: True
correct_bracketing("><<>")    # Returns: False
```

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `correct_bracketing` function.

3. **Run the script**: You can execute the script using Python to test the function with different inputs.

## Usage

To use the `correct_bracketing` function, follow these steps:

1. **Open a terminal or command prompt**.

2. **Navigate to the directory** where the `main.py` file is located.

3. **Run Python interactive shell** or create a Python script to import and use the function.

### Example Usage

```python
# In a Python script or interactive shell
from main import correct_bracketing

# Test the function with different inputs
print(correct_bracketing("<"))       # Output: False
print(correct_bracketing("<>"))      # Output: True
print(correct_bracketing("<<><>>"))  # Output: True
print(correct_bracketing("><<>"))    # Output: False
```

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed for easy integration into larger projects if needed.

This software is ideal for applications that require validation of bracket sequences, such as parsing or syntax checking tasks.