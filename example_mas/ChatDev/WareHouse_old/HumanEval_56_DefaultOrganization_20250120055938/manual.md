# Correct Bracketing Software

This software provides a function to check if every opening bracket in a string has a corresponding closing bracket. It is designed to work with strings composed of the characters "<" and ">".

## Main Functionality

The main function provided by this software is `correct_bracketing`, which takes a string of brackets as input and returns a boolean value indicating whether the brackets are correctly matched.

### Function: `correct_bracketing`

- **Input**: A string `brackets` consisting of the characters "<" and ">".
- **Output**: Returns `True` if every opening bracket has a corresponding closing bracket and `False` otherwise.

#### Examples

```python
correct_bracketing("<")        # Returns: False
correct_bracketing("<>")       # Returns: True
correct_bracketing("<<><>>")   # Returns: True
correct_bracketing("><<>")     # Returns: False
```

## Installation

This project does not require any external dependencies, making it simple to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Use the command line to navigate to the directory where the code is located.

4. **Run the Code**: You can directly run the `main.py` file to test the function.
   ```bash
   python main.py
   ```

## Usage

To use the `correct_bracketing` function, you can import it into your Python script and call it with the desired input string.

### Example Usage

```python
from main import correct_bracketing

# Test the function with different inputs
print(correct_bracketing("<"))        # Output: False
print(correct_bracketing("<>"))       # Output: True
print(correct_bracketing("<<><>>"))   # Output: True
print(correct_bracketing("><<>"))     # Output: False
```

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is straightforward and does not require additional libraries or complex setup.

This software is designed to be lightweight and efficient, providing a simple solution to the problem of bracket matching.