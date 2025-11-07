manual.md

```
# Bracket Nesting Checker

This software provides a simple function to determine if a string of square brackets contains a valid subsequence where at least one bracket is nested. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Functionality

The core functionality of this software is encapsulated in the `is_nested` function. This function takes a string as input, which contains only square brackets (`[` and `]`), and returns a boolean value:

- `True` if there is a valid subsequence of brackets where at least one bracket is nested.
- `False` otherwise.

### Examples

- `is_nested('[[]]')` returns `True`
- `is_nested('[]]]]]]][[[[[]')` returns `False`
- `is_nested('[][]')` returns `False`
- `is_nested('[]')` returns `False`
- `is_nested('[[][]]')` returns `True`
- `is_nested('[[]][[')` returns `True`

## Installation

This software does not require any external libraries or dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Step-by-Step Installation

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the code files for the software.

3. **Navigate to the project directory**: Use your command line interface to navigate to the directory where the `main.py` file is located.

## Usage

To use the `is_nested` function, follow these steps:

1. **Open the `main.py` file**: This file contains the `is_nested` function.

2. **Call the function**: You can call the `is_nested` function with a string of square brackets as an argument. For example:

   ```python
   result = is_nested('[[]]')
   print(result)  # Output: True
   ```

3. **Interpret the result**: The function will return `True` if there is a nested subsequence of brackets, and `False` otherwise.

## Notes

- The function assumes that the input string contains only square brackets. Any other characters in the string may lead to unexpected results.
- The function efficiently checks for nested brackets by maintaining a count of the current depth and the maximum depth encountered during the traversal of the string.

This software is designed to be straightforward and efficient, providing a quick way to check for nested brackets in a string.
```