# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to handle strings containing multiple groups of nested parentheses and return each group as a separate string in a list. The function ignores any spaces in the input string.

## Main Function

### `separate_paren_groups`

- **Description**: This function takes a string containing multiple groups of nested parentheses and separates them into individual strings. Each group is balanced, meaning every open parenthesis is properly closed, and groups are not nested within each other.
- **Input**: A string (`paren_string`) containing groups of parentheses.
- **Output**: A list of strings, where each string is a group of balanced parentheses.

#### Example

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_group = ""
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
            current_group = ""
    return result
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

No additional installation steps are necessary as there are no external dependencies.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can run the function by importing it into a Python script or an interactive Python session.

   ```python
   from main import separate_paren_groups

   # Example usage
   result = separate_paren_groups('( ) (( )) (( )( ))')
   print(result)  # Output: ['()', '(())', '(()())']
   ```

4. **Testing**: You can test the function with different input strings to ensure it behaves as expected.

## Documentation

For further details on how the function works, refer to the docstring provided in the code. It includes a description of the function, its input, and output, as well as an example of usage.

This software is designed to be simple and efficient, focusing solely on the task of separating groups of balanced parentheses.