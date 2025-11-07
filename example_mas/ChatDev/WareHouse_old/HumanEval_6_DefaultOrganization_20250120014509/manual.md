# Parse Nested Parentheses

This software provides a function to determine the deepest level of nesting for multiple groups of nested parentheses within a given string. It is designed to be simple and efficient, requiring no external dependencies.

## Main Functionality

The main function of this software is `parse_nested_parens`, which takes a string input consisting of multiple groups of nested parentheses separated by spaces. For each group, it calculates and returns the deepest level of nesting.

### Example

For the input string `'(()()) ((())) () ((())()())'`, the function will return `[2, 3, 1, 3]`, indicating the maximum nesting levels for each group of parentheses.

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the code files for the software.

3. **Navigate to the directory**: Use the command line to navigate to the directory containing the `main.py` file.

## Usage

To use the `parse_nested_parens` function, follow these steps:

1. **Open a Python environment**: This can be done through a terminal or an IDE like PyCharm or VSCode.

2. **Import the function**: Ensure the `main.py` file is in your working directory or adjust the import path accordingly.

    ```python
    from main import parse_nested_parens
    ```

3. **Call the function with your input**: Pass a string of nested parentheses groups to the function.

    ```python
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    print(result)  # Output: [2, 3, 1, 3]
    ```

## Documentation

The function is self-contained and documented within the code. The docstring provides a clear explanation of the input and expected output, along with an example.

For further assistance or inquiries, please contact our support team.