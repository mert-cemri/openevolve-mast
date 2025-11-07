# Correct Bracketing

This software provides a simple utility function to check if a given string of brackets is correctly bracketed. It ensures that every opening bracket has a corresponding closing bracket in the correct order.

## Main Functionality

The main function provided by this software is `correct_bracketing`. It takes a string of brackets as input and returns a boolean value indicating whether the brackets are correctly balanced.

### Function: `correct_bracketing`

- **Input**: A string consisting of the characters `(` and `)`.
- **Output**: Returns `True` if every opening bracket has a corresponding closing bracket and they are correctly nested. Returns `False` otherwise.

#### Examples

```python
correct_bracketing("(")        # Returns: False
correct_bracketing("()")       # Returns: True
correct_bracketing("(()())")   # Returns: True
correct_bracketing(")(()")     # Returns: False
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: 

   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the function:

   ```bash
   python main.py
   ```

## Usage

To use the `correct_bracketing` function in your own projects, simply import it from the `main.py` file and call it with your desired input.

### Example Usage

```python
from main import correct_bracketing

# Test the function with different inputs
print(correct_bracketing("()"))       # Output: True
print(correct_bracketing("(()"))      # Output: False
print(correct_bracketing("(()())"))   # Output: True
print(correct_bracketing(")(()"))     # Output: False
```

## Documentation

For further documentation and examples, please refer to the docstring provided within the `main.py` file. The docstring includes usage examples and a brief description of the function's purpose.

This software is designed to be simple and efficient, providing a quick solution to check the correctness of bracket sequences in strings.