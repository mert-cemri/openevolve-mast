# Parentheses Matcher

This software provides a function to determine if two strings of parentheses can be concatenated in some order to form a balanced string. A balanced string is one where every opening parenthesis '(' has a corresponding closing parenthesis ')'.

## Main Functionality

The main function provided by this software is `match_parens(lst)`. This function takes a list of two strings, each consisting solely of parentheses, and returns 'Yes' if there is a way to concatenate the two strings to form a balanced string, and 'No' otherwise.

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
    '''
    def is_balanced(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    # Check both possible concatenations
    if is_balanced(lst[0] + lst[1]) or is_balanced(lst[1] + lst[0]):
        return 'Yes'
    else:
        return 'No'
```

## Installation

This project does not require any external dependencies. You can use the function directly in your Python environment.

### Quick Start

1. **Clone the Repository:**

   Clone the repository to your local machine using:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd <project-directory>
   ```

3. **Run the Function:**

   You can run the function directly in a Python environment. For example:

   ```python
   from main import match_parens

   result = match_parens(['()(', ')'])
   print(result)  # Output: 'Yes'
   ```

## Usage

To use the `match_parens` function, simply pass a list of two strings containing only parentheses to the function. The function will return 'Yes' if the strings can be concatenated to form a balanced string, and 'No' otherwise.

### Example Usage

```python
from main import match_parens

# Example 1
result1 = match_parens(['()(', ')'])
print(result1)  # Output: 'Yes'

# Example 2
result2 = match_parens([')', ')'])
print(result2)  # Output: 'No'
```

## Documentation

For further information and examples, please refer to the comments within the code. The function is designed to be straightforward and easy to integrate into larger projects.

This software is designed to be simple and efficient, providing a quick solution to check the balance of concatenated parentheses strings.