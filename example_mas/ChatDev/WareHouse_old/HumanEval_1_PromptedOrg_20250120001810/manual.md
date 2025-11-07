# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to handle strings containing multiple groups of nested parentheses and return each group as a separate string. The function ensures that each group is balanced, meaning each open parenthesis is properly closed, and it ignores any spaces in the input string.

## Main Function

### `separate_paren_groups`

- **Description**: This function takes a string containing multiple groups of nested parentheses and separates those groups into individual strings. Each group is balanced and not nested within each other.
- **Input**: A string (`paren_string`) containing multiple groups of nested parentheses.
- **Output**: A list of strings, where each string is a group of balanced parentheses.

#### Example Usage

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    current_group = ''
    balance = 0
    for char in paren_string:
        if char == ' ':
            continue
        current_group += char
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance == 0 and current_group:
            groups.append(current_group)
            current_group = ''
    return groups
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

1. **Clone the repository** (if applicable) or download the `main.py` file.
2. **Run the script** using Python:

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: If you are integrating this function into another project, ensure you import it correctly.

   ```python
   from main import separate_paren_groups
   ```

2. **Call the Function**: Pass a string containing groups of parentheses to the function.

   ```python
   result = separate_paren_groups('( ) (( )) (( )( ))')
   print(result)  # Output: ['()', '(())', '(()())']
   ```

## Documentation

This software is straightforward and does not require extensive documentation. The main function is well-documented with a docstring explaining its purpose, inputs, and outputs. For any further questions or support, please contact the development team.