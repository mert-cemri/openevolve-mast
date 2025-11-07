# Parentheses Matcher

This software provides a simple function to determine if two strings of parentheses can be concatenated in some order to form a balanced string. A balanced string is one where every opening parenthesis '(' has a corresponding closing parenthesis ')'.

## Main Functionality

The main function provided by this software is `match_parens(lst)`. This function takes a list of two strings, each consisting solely of the characters '(' and ')'. It checks if there is a way to concatenate these two strings in any order such that the resulting string is balanced.

### Function Definition

```python
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''
```

## Installation

This project does not require any external dependencies. You only need Python installed on your system to run the function.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: If this code is part of a repository, clone it to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function in a Python script or an interactive Python session. Here’s how you can test it:

    ```python
    from main import match_parens

    # Test cases
    print(match_parens(['()(', ')']))  # Output: 'Yes'
    print(match_parens([')', ')']))    # Output: 'No'
    ```

4. **Modify as Needed**: You can modify the `main.py` file to include additional test cases or integrate the function into a larger application.

## Documentation

This function is straightforward and does not require additional documentation beyond the provided docstring. It is designed to be used in any Python environment without additional setup.

For further questions or support, please contact the development team.