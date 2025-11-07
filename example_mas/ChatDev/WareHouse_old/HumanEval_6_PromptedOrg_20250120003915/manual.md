# Parse Nested Parentheses

This software module provides a function to parse nested parentheses and determine the deepest level of nesting for each group of parentheses in a given string.

## Main Function

The main function provided by this module is `parse_nested_parens`.

### Function: `parse_nested_parens`

- **Input**: A string containing multiple groups of nested parentheses separated by spaces.
- **Output**: A list of integers, where each integer represents the deepest level of nesting for the corresponding group of parentheses.

#### Example

```python
from main import parse_nested_parens

result = parse_nested_parens('(()()) ((())) () ((())()())')
print(result)  # Output: [2, 3, 1, 3]
```

## Installation

To use this software, you need to have Python installed on your system. The module does not require any additional dependencies, so you can directly use the provided code.

### Quick Install

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Code**: You can directly run the code using Python.

```bash
python main.py
```

## How to Use

1. **Import the Function**: Import the `parse_nested_parens` function from the `main.py` file.

2. **Call the Function**: Pass a string containing groups of nested parentheses to the function.

3. **Get the Result**: The function will return a list of integers indicating the deepest level of nesting for each group.

### Example Usage

```python
from main import parse_nested_parens

# Define a string with groups of nested parentheses
paren_string = '(()()) ((())) () ((())()())'

# Parse the string and get the deepest level of nesting for each group
nesting_levels = parse_nested_parens(paren_string)

# Output the result
print(nesting_levels)  # Output: [2, 3, 1, 3]
```

## Documentation

This module is designed to be simple and straightforward, focusing on parsing nested parentheses. For further information or assistance, please refer to the comments within the code or contact our support team.