# Parse Nested Parentheses

This software provides a function to determine the deepest level of nesting for groups of parentheses in a given string. It is designed to handle multiple groups of nested parentheses separated by spaces and return a list of integers representing the maximum nesting level for each group.

## Main Functionality

The main function of this software is `parse_nested_parens`, which takes a string input and returns a list of integers. Each integer corresponds to the deepest level of nesting for a group of parentheses in the input string.

### Example

For the input string `'(()()) ((())) () ((())()())'`, the function will return `[2, 3, 1, 3]`, indicating the maximum nesting levels for each group of parentheses.

## Installation

This software does not require any external dependencies, making it straightforward to use. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

To use the `parse_nested_parens` function, follow these steps:

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can run the function by executing the `main.py` file in a Python environment. Here is an example of how to use the function in a Python script:

    ```python
    from main import parse_nested_parens

    # Example input
    paren_string = '(()()) ((())) () ((())()())'

    # Get the maximum nesting levels
    result = parse_nested_parens(paren_string)

    # Print the result
    print(result)  # Output: [2, 3, 1, 3]
    ```

4. **Modify as Needed**: You can modify the input string to test different cases of nested parentheses.

## Documentation

The function is documented with a docstring that provides a brief description of its functionality and an example of its usage. For further information or questions, please refer to the comments within the code or contact the development team.

This software is designed to be simple and efficient, providing a quick solution for analyzing nested parentheses in strings.