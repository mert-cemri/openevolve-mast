# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to handle strings containing multiple groups of nested parentheses, separating them into individual strings and returning them as a list. The function ensures that each group is balanced, meaning each open parenthesis is properly closed, and ignores any spaces in the input string.

## Main Function

### `separate_paren_groups`

- **Description**: This function takes a string containing multiple groups of nested parentheses and separates these groups into individual strings. It returns a list of these strings, ensuring that each group is balanced and not nested within each other.
  
- **Input**: A string (`paren_string`) containing groups of nested parentheses.
  
- **Output**: A list of strings, where each string is a separate group of balanced parentheses.

- **Example**:
  ```python
  separate_paren_groups('( ) (( )) (( )( ))')
  # Output: ['()', '(())', '(()())']
  ```

## Installation

This project does not require any external dependencies, so you can use it directly with Python. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the Code**: You can run the code directly using Python.
   ```bash
   python main.py
   ```

## Usage

1. **Import the Function**: If you are using this function in another Python script, import it from the module.
   ```python
   from main import separate_paren_groups
   ```

2. **Call the Function**: Use the function by passing a string containing groups of parentheses.
   ```python
   result = separate_paren_groups('( ) (( )) (( )( ))')
   print(result)  # Output: ['()', '(())', '(()())']
   ```

## Documentation

For further information and examples, refer to the function's docstring within the code. The docstring provides a detailed explanation of the function's purpose, input, and output.

This software is designed to be simple and efficient, focusing solely on the task of separating balanced parentheses groups from a string. It is a lightweight solution that does not require any additional libraries or dependencies.