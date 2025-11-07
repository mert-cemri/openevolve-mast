# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to handle strings containing multiple groups of nested parentheses and return each group as a separate string.

## Main Functionality

The main function provided by this software is `separate_paren_groups`. This function takes a string containing multiple groups of nested parentheses as input and returns a list of strings, each representing a separate group of balanced parentheses.

### Function Definition

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ 
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
```

## Installation

This project does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change your current directory to the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Run the Function:**

   You can use the `separate_paren_groups` function in your Python scripts. Here is an example of how to use it:

   ```python
   from main import separate_paren_groups

   input_string = '( ) (( )) (( )( ))'
   result = separate_paren_groups(input_string)
   print(result)  # Output: ['()', '(())', '(()())']
   ```

## Documentation

For further details on how to use the function, refer to the docstring provided in the function definition. The docstring includes a brief description of the function's purpose, input parameters, and expected output.

## Support

If you encounter any issues or have questions, please feel free to reach out to our support team. We are here to assist you in making the most out of this software.