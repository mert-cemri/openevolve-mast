# Parse Nested Parentheses

This software provides a function to parse nested parentheses and determine the deepest level of nesting for each group of parentheses in a given string.

## Main Functionality

The main function of this software is `parse_nested_parens`, which takes a string of multiple groups of nested parentheses separated by spaces and returns a list of integers representing the deepest level of nesting for each group.

### Example

For example, given the input string `'(()()) ((())) () ((())()())'`, the function will return `[2, 3, 1, 3]`.

## Installation

This software does not require any external dependencies beyond the standard Python library. You can run it in any environment where Python is installed.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**

   Change into the directory containing the `main.py` file:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**

   You can run the function by executing the `main.py` file in a Python environment. Open a Python interpreter or script and import the function:

   ```python
   from main import parse_nested_parens

   # Example usage
   result = parse_nested_parens('(()()) ((())) () ((())()())')
   print(result)  # Output: [2, 3, 1, 3]
   ```

## Documentation

The function is documented with a docstring that explains its purpose, input, and output. You can view this documentation directly in the code or by using Python's built-in help system:

```python
help(parse_nested_parens)
```

This will display the function's documentation, including an example of how to use it.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to assist you with any inquiries you may have regarding the software.