# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to handle strings containing multiple groups of nested parentheses, separating them into individual strings and returning them as a list. Each group is balanced, meaning every open parenthesis is properly closed, and groups are not nested within each other. Spaces in the input string are ignored.

## Main Functionality

The main function provided by this software is `separate_paren_groups`, which processes a string containing multiple groups of parentheses and returns a list of those groups.

### Function: `separate_paren_groups`

- **Input**: A string containing multiple groups of nested parentheses.
- **Output**: A list of strings, each representing a separate group of balanced parentheses.
- **Example**:
  ```python
  >>> separate_paren_groups('( ) (( )) (( )( ))')
  ['()', '(())', '(()())']
  ```

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change your directory to the project folder:
   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the function:
   ```bash
   python main.py
   ```

## How to Use

To use the `separate_paren_groups` function, follow these steps:

1. **Import the Function**: Ensure that the function is imported into your Python script or interactive environment.

2. **Call the Function**: Pass a string containing groups of parentheses to the function and capture the output.
   ```python
   from main import separate_paren_groups

   result = separate_paren_groups('( ) (( )) (( )( ))')
   print(result)  # Output: ['()', '(())', '(()())']
   ```

3. **Process the Output**: The output will be a list of strings, each representing a separate group of balanced parentheses.

## Documentation

For further information and detailed documentation, please refer to the code comments and docstrings provided within the `main.py` file. These comments explain the logic and flow of the function, ensuring clarity and ease of understanding.

Feel free to reach out for any support or questions regarding the use of this software.