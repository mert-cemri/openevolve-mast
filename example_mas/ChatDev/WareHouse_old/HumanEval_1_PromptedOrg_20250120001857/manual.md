# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to process strings containing multiple groups of nested parentheses and return each group as a separate string.

## Main Functionality

The primary function of this software is:

- `separate_paren_groups(paren_string: str) -> List[str]`: This function takes a string containing multiple groups of nested parentheses and returns a list of those groups. Each group is balanced, meaning every open parenthesis is properly closed. Spaces in the input string are ignored.

### Example

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
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
            result.append(current_group)
            current_group = ''
    return result
```

## Installation

This software does not require any external dependencies. It is implemented in pure Python, and you can run it in any environment that supports Python.

### Quick Install

Ensure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/).

## How to Use

1. **Clone or Download the Repository**: Obtain the source code by cloning the repository or downloading it as a ZIP file.

2. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

3. **Run the Code**: You can use the function in your Python scripts by importing it. Here's an example of how to use the function:

   ```python
   from main import separate_paren_groups

   paren_string = '( ) (( )) (( )( ))'
   groups = separate_paren_groups(paren_string)
   print(groups)  # Output: ['()', '(())', '(()())']
   ```

## Documentation

For further documentation and examples, please refer to the comments within the code. The function is designed to be straightforward and easy to integrate into other Python projects.

Feel free to modify and extend the code to suit your specific needs. If you encounter any issues or have questions, please reach out to our support team.