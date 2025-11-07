# Match Parens User Manual

Welcome to the Match Parens software! This software is designed to help you determine if two strings of parentheses can be concatenated in some order to form a balanced string. A balanced string is one where every opening parenthesis '(' has a corresponding closing parenthesis ')'.

## Main Functionality

The primary function of this software is `match_parens(lst)`, which takes a list of two strings as input. Each string consists solely of open '(' and close ')' parentheses. The function checks if there is a way to concatenate these two strings in any order such that the resulting string is balanced. It returns 'Yes' if a balanced string can be formed, and 'No' otherwise.

### Example Usage

- `match_parens(['()(', ')'])` returns `'Yes'`
- `match_parens([')', ')'])` returns `'No'`

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need to have Python installed on your system.

### Quick Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change into the directory where the code is located:
   ```bash
   cd <repository-directory>
   ```

4. **Run the Code**: You can run the code directly using Python:
   ```bash
   python main.py
   ```

## How to Use

To use the `match_parens` function, follow these steps:

1. **Import the Function**: If you're using this function in another script, make sure to import it:
   ```python
   from main import match_parens
   ```

2. **Call the Function**: Pass a list of two strings to the function and capture the result:
   ```python
   result = match_parens(['()(', ')'])
   print(result)  # Output: 'Yes'
   ```

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The function includes a helper function `is_balanced(s)` that checks if a given string of parentheses is balanced.

This software is designed to be simple and efficient, providing a quick solution to check the balance of parentheses in concatenated strings. If you have any questions or need further assistance, please reach out to our support team.