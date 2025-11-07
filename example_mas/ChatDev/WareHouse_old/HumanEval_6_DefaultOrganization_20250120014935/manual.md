# Parse Nested Parentheses

This software provides a function to parse nested parentheses in a string and determine the maximum depth of nesting for each group of parentheses.

## Main Function

The main function provided by this software is `parse_nested_parens`, which takes a string of multiple groups of nested parentheses separated by spaces and returns a list of integers representing the deepest level of nesting for each group.

### Function Signature

```python
def parse_nested_parens(paren_string: str) -> List[int]:
```

### Example Usage

```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

In this example, the function analyzes each group of parentheses and returns the maximum depth of nesting for each group.

## Installation

This software does not require any external dependencies, so you can run it with a standard Python environment. Ensure you have Python installed on your system.

### Quick Install

1. Clone the repository or download the `main.py` file.
2. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory containing the `main.py` file.
3. Run a Python interpreter and import the function:

   ```bash
   python
   ```

4. Import the function and use it:

   ```python
   from main import parse_nested_parens
   result = parse_nested_parens('(()()) ((())) () ((())()())')
   print(result)  # Output: [2, 3, 1, 3]
   ```

## Documentation

The function `parse_nested_parens` is designed to be simple and efficient. It splits the input string by spaces to separate each group of parentheses, then calculates the maximum depth of nesting for each group using a helper function `max_depth`.

### Helper Function

- `max_depth(paren_group: str) -> int`: This function calculates the maximum depth of nested parentheses for a single group.

## Support

For any issues or questions, please contact the development team at ChatDev. We are committed to providing support and assistance for our software products.