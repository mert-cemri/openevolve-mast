# Parse Nested Parentheses

This software provides a function to calculate the deepest level of nested parentheses for each group in a given string. It is designed to handle multiple groups of parentheses separated by spaces and return a list of integers representing the maximum depth of nesting for each group.

## Main Functionality

The main function provided by this software is `parse_nested_parens`. This function takes a single input, a string containing multiple groups of nested parentheses separated by spaces, and returns a list of integers. Each integer in the list corresponds to the deepest level of nesting for each group of parentheses in the input string.

### Example

For example, given the input string `'(()()) ((())) () ((())()())'`, the function will return `[2, 3, 1, 3]`. This indicates that the first group `(()())` has a maximum nesting depth of 2, the second group `((()))` has a depth of 3, the third group `()` has a depth of 1, and the fourth group `((())()())` has a depth of 3.

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any environment that supports Python.

### Requirements

- Python 3.x

### Installation Steps

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone the repository or download the `main.py` file to your local machine.

## Usage

To use the `parse_nested_parens` function, follow these steps:

1. Open the `main.py` file in your preferred Python environment or editor.
2. Call the `parse_nested_parens` function with a string input containing groups of nested parentheses.

### Example Usage

```python
from main import parse_nested_parens

# Example input string
input_string = '(()()) ((())) () ((())()())'

# Call the function and print the result
result = parse_nested_parens(input_string)
print(result)  # Output: [2, 3, 1, 3]
```

## Documentation

The function is documented with a docstring that explains its purpose, input, and output. You can view this documentation by accessing the function in your Python environment or by reading the comments in the `main.py` file.

For any further questions or support, please feel free to contact our team. We are here to assist you in making the most out of this software.