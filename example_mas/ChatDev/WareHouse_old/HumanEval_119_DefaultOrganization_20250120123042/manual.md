# Parentheses Matcher

This software provides a simple function to determine if two strings of parentheses can be concatenated in some order to form a balanced string. A string is considered balanced if all parentheses are properly matched and closed.

## Main Function

The main function provided by this software is `match_parens(lst)`. This function takes a list of two strings, each consisting of open parentheses `'('` and close parentheses `')'` only. It checks if there is a way to concatenate the two strings in any order such that the resulting string is balanced.

### Function Signature

```python
def match_parens(lst):
    """
    Determines if two strings of parentheses can be concatenated to form a balanced string.

    Parameters:
    lst (list): A list containing two strings of parentheses.

    Returns:
    str: 'Yes' if the strings can be concatenated to form a balanced string, 'No' otherwise.
    """
```

### Examples

- `match_parens(['()(', ')'])` returns `'Yes'`
- `match_parens([')', ')'])` returns `'No'`

## Installation

This software does not require any external dependencies, making it straightforward to use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

## Usage

To use the `match_parens` function, you can run the `main.py` file directly or import the function into your own Python script.

### Running Directly

1. Open a terminal or command prompt.
2. Navigate to the directory containing `main.py`.
3. Run the script using Python.

   ```bash
   python main.py
   ```

### Importing into Another Script

You can import the `match_parens` function into your own Python script as follows:

```python
from main import match_parens

# Example usage
result = match_parens(['()(', ')'])
print(result)  # Output: 'Yes'
```

## Documentation

For further details on how the function works, you can refer to the comments within the `main.py` file. The function is designed to be simple and efficient, ensuring that it performs well even with larger strings of parentheses.

Feel free to reach out for support if you encounter any issues or have questions about using the software.