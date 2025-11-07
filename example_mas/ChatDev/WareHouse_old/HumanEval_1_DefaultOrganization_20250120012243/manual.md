# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a string. It is designed to handle strings containing multiple groups of nested parentheses and return each group as a separate string. The function ensures that each group is balanced, meaning every open parenthesis is properly closed, and it ignores any spaces in the input string.

## Main Functionality

The core functionality of this software is encapsulated in the `separate_paren_groups` function. This function takes a single input, a string containing groups of parentheses, and returns a list of strings, each representing a separate group of balanced parentheses.

### Function Signature

```python
def separate_paren_groups(paren_string: str) -> List[str]:
```

### Example Usage

```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required since there are no external dependencies.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run a Python interpreter session by typing `python` in the terminal.

4. Import the function from the `main.py` file:

   ```python
   from main import separate_paren_groups
   ```

5. Call the function with a string input to separate the parentheses groups:

   ```python
   result = separate_paren_groups('( ) (( )) (( )( ))')
   print(result)  # Output: ['()', '(())', '(()())']
   ```

## Documentation

For further details on how the function works, refer to the docstring provided within the `main.py` file. The docstring includes a description of the function's purpose, input parameters, and an example of expected output.

This software is designed to be simple and efficient, focusing solely on the task of separating balanced parentheses groups from a string.