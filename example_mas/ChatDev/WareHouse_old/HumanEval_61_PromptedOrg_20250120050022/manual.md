# Correct Bracketing

This software provides a function to check if a string of brackets is correctly balanced. It ensures that every opening bracket has a corresponding closing bracket.

## Quick Install

To use this software, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can use the function directly in your Python environment. There are no additional dependencies required for this software.

## 🤔 What is this?

The `correct_bracketing` function is designed to verify the correctness of bracket sequences. It checks if every opening bracket `(` has a corresponding closing bracket `)`, and that they are correctly nested.

### Main Function

- **correct_bracketing(brackets: str) -> bool**: This function takes a string of brackets as input and returns `True` if the brackets are correctly balanced, otherwise it returns `False`.

### Examples

- `correct_bracketing("(")` returns `False`
- `correct_bracketing("()")` returns `True`
- `correct_bracketing("(()())")` returns `True`
- `correct_bracketing(")(()")` returns `False`

## How to Use

1. **Open your Python environment**: You can use any Python IDE or a simple command line interface.

2. **Define the function**: Copy the function code into your Python environment.

    ```python
    def correct_bracketing(brackets: str) -> bool:
        balance = 0
        for char in brackets:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    ```

3. **Call the function**: Use the function by passing a string of brackets to it.

    ```python
    print(correct_bracketing("()"))  # Output: True
    print(correct_bracketing("(()"))  # Output: False
    ```

## Documentation

The function is simple and does not require additional documentation. However, if you need further assistance, you can refer to Python's official documentation for more information on running Python scripts and functions.

This software is designed to be straightforward and easy to integrate into any Python project where bracket validation is necessary.