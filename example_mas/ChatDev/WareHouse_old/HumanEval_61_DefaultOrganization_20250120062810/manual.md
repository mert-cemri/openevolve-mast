# Correct Bracketing

This software module provides a simple utility function to check if a string of brackets is correctly balanced. It is designed to ensure that every opening bracket has a corresponding closing bracket in the correct order.

## Main Function

The main function provided in this module is `correct_bracketing`.

### `correct_bracketing(brackets: str) -> bool`

- **Description**: This function takes a string of brackets as input and returns `True` if every opening bracket has a corresponding closing bracket in the correct order. Otherwise, it returns `False`.

- **Parameters**: 
  - `brackets` (str): A string consisting of the characters `(` and `)`.

- **Returns**: 
  - `bool`: `True` if the brackets are correctly balanced, `False` otherwise.

- **Examples**:
  ```python
  >>> correct_bracketing("(")
  False
  >>> correct_bracketing("()")
  True
  >>> correct_bracketing("(()())")
  True
  >>> correct_bracketing(")(()")
  False
  ```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use.

### Quick Install

Since there are no external dependencies, you can directly use the provided `main.py` file in your Python environment.

1. **Clone the repository** or download the `main.py` file to your local machine.

2. **Ensure you have Python installed**. This module is compatible with Python 3.x.

3. **Run the module** using your preferred Python interpreter.

## How to Use

1. **Import the function** in your Python script or interactive session:

   ```python
   from main import correct_bracketing
   ```

2. **Call the function** with a string of brackets to check if they are correctly balanced:

   ```python
   result = correct_bracketing("(()())")
   print(result)  # Output: True
   ```

3. **Test with different inputs** to ensure the function behaves as expected:

   ```python
   print(correct_bracketing("("))      # Output: False
   print(correct_bracketing("()"))     # Output: True
   print(correct_bracketing(")(()"))   # Output: False
   ```

This simple utility can be integrated into larger applications where bracket validation is necessary, such as parsing expressions or validating user input in mathematical or programming contexts.