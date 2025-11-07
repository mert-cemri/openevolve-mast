# Match Parens User Manual

Welcome to the Match Parens software! This tool is designed to help you determine if two strings of parentheses can be concatenated in some order to form a balanced string. This user manual will guide you through the main functions of the software, how to install it, and how to use it effectively.

## Main Functionality

The primary function of this software is `match_parens`, which takes a list of two strings as input. Each string consists solely of open parentheses '(' or close parentheses ')'. The function checks if it is possible to concatenate the two strings in some order such that the resulting string is balanced. A string is considered balanced if every opening parenthesis has a corresponding closing parenthesis and they are correctly nested.

### Example Usage

- `match_parens(['()(', ')'])` returns `'Yes'` because the strings can be concatenated to form `'()()'`, which is balanced.
- `match_parens([')', ')'])` returns `'No'` because there is no way to concatenate the strings to form a balanced string.

## Installation

This software does not require any external dependencies, making the installation process straightforward. You only need to have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the software**: You can execute the `main.py` file directly to use the `match_parens` function.

## How to Use

1. **Open your terminal or command prompt**.

2. **Navigate to the directory containing `main.py`**.

3. **Run Python in interactive mode**:
   ```bash
   python
   ```

4. **Import the function and use it**:
   ```python
   from main import match_parens
   result = match_parens(['()(', ')'])
   print(result)  # Output: 'Yes'
   ```

5. **Exit the Python interactive mode** by typing `exit()` or pressing `Ctrl+D`.

## Documentation

For further details on the implementation, you can refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic behind the function.

## Support

If you encounter any issues or have questions about using the software, please reach out to our support team through the contact information provided in the repository or on our website.

Thank you for using Match Parens! We hope this tool helps you efficiently determine the balance of parentheses strings.