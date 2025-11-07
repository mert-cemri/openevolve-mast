# Parentheses Group Separator

This software provides a function to separate groups of nested parentheses from a given string. It is designed to handle strings containing multiple groups of balanced parentheses, ignoring any spaces in the input.

## Main Functionality

The main function of this software is `separate_paren_groups`, which takes a string as input and returns a list of strings, each representing a separate group of balanced parentheses.

### Function: `separate_paren_groups`

- **Input**: A string containing multiple groups of nested parentheses.
- **Output**: A list of strings, each representing a separate group of balanced parentheses.
- **Example**: 
  ```python
  separate_paren_groups('( ) (( )) (( )( ))')
  # Output: ['()', '(())', '(()())']
  ```

## Installation

This project does not require any external dependencies, so you can use it directly with a standard Python installation.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the `main.py` file to your local machine.

3. No additional installation steps are required since there are no external dependencies.

## How to Use

1. Open your terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. You can use the function by importing it into your Python script or interactive session. Here is an example of how to use it:

   ```python
   from main import separate_paren_groups

   # Example usage
   paren_string = '( ) (( )) (( )( ))'
   result = separate_paren_groups(paren_string)
   print(result)  # Output: ['()', '(())', '(()())']
   ```

4. The function will process the input string and return a list of balanced parentheses groups.

## Documentation

For further information and examples, please refer to the docstring within the `main.py` file. The docstring provides a detailed explanation of the function's behavior and includes example usage.

This software is designed to be simple and efficient, focusing solely on the task of separating groups of nested parentheses. If you encounter any issues or have questions, please feel free to reach out for support.