# Correct Bracketing

This software provides a simple utility function to check if a string of brackets is correctly balanced. It is designed to determine whether every opening bracket '(' has a corresponding closing bracket ')'.

## Main Function

### `correct_bracketing(brackets: str) -> bool`

- **Description**: This function takes a string of brackets as input and returns `True` if every opening bracket has a corresponding closing bracket, otherwise it returns `False`.
- **Parameters**: 
  - `brackets` (str): A string consisting of the characters '(' and ')'.
- **Returns**: 
  - `bool`: `True` if the brackets are correctly balanced, `False` otherwise.

### Examples

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

This software does not require any external dependencies. It is implemented in pure Python, so you only need to have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository or download the script**: You can clone the repository or simply download the `main.py` file containing the function.

## Usage

1. **Run the script**: You can execute the script in a Python environment. Open a terminal or command prompt and navigate to the directory containing `main.py`.

2. **Test the function**: You can test the function by calling it with different strings of brackets to see if they are correctly balanced.

```bash
python main.py
```

3. **Integrate into your project**: You can copy the `correct_bracketing` function into your own Python projects to use it as needed.

## Documentation

This function is straightforward and does not require additional documentation beyond the examples provided. It is designed to be a utility function that can be easily integrated into larger projects where bracket validation is necessary.