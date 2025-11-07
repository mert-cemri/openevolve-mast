# Correct Bracketing

This software provides a simple utility function to check if a string of "<" and ">" brackets is correctly balanced. It ensures that every opening bracket has a corresponding closing bracket.

## Main Function

The main function provided by this software is `correct_bracketing`. This function takes a string of brackets as input and returns a boolean indicating whether the brackets are correctly balanced.

### Function Signature

```python
def correct_bracketing(brackets: str) -> bool:
```

### Parameters

- `brackets`: A string consisting of the characters "<" and ">".

### Returns

- `True` if every opening bracket has a corresponding closing bracket.
- `False` otherwise.

### Examples

```python
>>> correct_bracketing("<")
False
>>> correct_bracketing("<>")
True
>>> correct_bracketing("<<><>>")
True
>>> correct_bracketing("><<>")
False
```

## Installation

This software does not require any external dependencies. You can simply download the `main.py` file and run it in a Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Download the `main.py` file containing the `correct_bracketing` function.

3. No additional installation steps are required as there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where the `main.py` file is located.

3. Run the Python interpreter and import the function:

   ```bash
   python
   ```

4. Import the function and use it:

   ```python
   from main import correct_bracketing

   # Test the function with different inputs
   print(correct_bracketing("<"))       # Output: False
   print(correct_bracketing("<>"))      # Output: True
   print(correct_bracketing("<<><>>"))  # Output: True
   print(correct_bracketing("><<>"))    # Output: False
   ```

## Documentation

This software is straightforward and does not require extensive documentation. The function `correct_bracketing` is designed to be intuitive and easy to use for checking the balance of brackets in a string. For any further questions or support, please contact our support team.