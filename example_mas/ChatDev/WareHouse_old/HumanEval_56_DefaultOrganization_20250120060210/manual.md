# Correct Bracketing

This software provides a function to check if a string of brackets, consisting of "<" and ">", is correctly balanced. It ensures that every opening bracket "<" has a corresponding closing bracket ">".

## Main Function

The main function provided by this software is `correct_bracketing`.

### Functionality

- **correct_bracketing(brackets: str) -> bool**: This function takes a string of brackets as input and returns `True` if every opening bracket has a corresponding closing bracket, otherwise it returns `False`.

#### Examples

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

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Function**: You can run the function directly in a Python environment or script. Here is an example of how to use it in a Python script:

    ```python
    from main import correct_bracketing

    # Test the function
    print(correct_bracketing("<"))        # Output: False
    print(correct_bracketing("<>"))       # Output: True
    print(correct_bracketing("<<><>>"))   # Output: True
    print(correct_bracketing("><<>"))     # Output: False
    ```

4. **Testing**: You can test the function using the examples provided to ensure it works as expected.

## Documentation

For further information, you can refer to the docstring provided within the `main.py` file, which includes a detailed description of the function and examples of its usage.

This software is designed to be simple and efficient, focusing solely on the task of checking bracket balance without any additional features or dependencies.