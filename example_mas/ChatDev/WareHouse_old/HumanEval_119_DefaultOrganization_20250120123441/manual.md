# Parentheses Matcher

This software module provides a function to determine if two strings of parentheses can be concatenated in some order to form a balanced string. It is designed to solve the problem of checking if a combination of two strings consisting solely of open and close parentheses can result in a balanced string.

## Main Functionality

The main function provided by this module is `match_parens(lst)`. This function takes a list of two strings as input, where each string consists of open parentheses '(' or close parentheses ')' only. The function checks if it is possible to concatenate the two strings in some order such that the resulting string is balanced.

A string is considered balanced if all parentheses are properly closed and nested. For example, the string '(())()' is balanced, while the string '())' is not.

### Function Signature

```python
def match_parens(lst):
    '''
    Determines if two strings of parentheses can be concatenated in some order to form a balanced string.

    Parameters:
    lst (list): A list containing two strings of parentheses.

    Returns:
    str: 'Yes' if a balanced string can be formed, 'No' otherwise.
    '''
```

### Examples

- `match_parens(['()(', ')'])` returns `'Yes'`
- `match_parens([')', ')'])` returns `'No'`

## Installation

This module does not require any external dependencies. It is implemented purely in Python and can be used directly without any additional installations.

### Quick Start

1. Ensure you have Python installed on your system.
2. Clone or download the module to your local machine.
3. Use the function `match_parens(lst)` in your Python scripts by importing the module.

## Usage

To use the `match_parens` function, follow these steps:

1. Import the function into your Python script:

    ```python
    from main import match_parens
    ```

2. Call the function with a list of two strings as an argument:

    ```python
    result = match_parens(['()(', ')'])
    print(result)  # Output: 'Yes'
    ```

3. The function will return `'Yes'` if a balanced string can be formed by concatenating the two input strings in some order, and `'No'` otherwise.

## Conclusion

This module provides a simple yet effective solution for checking the balance of concatenated parentheses strings. It is easy to integrate into existing Python projects and requires no additional setup or dependencies.