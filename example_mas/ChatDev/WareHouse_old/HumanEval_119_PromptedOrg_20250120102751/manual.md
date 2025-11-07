# Match Parens User Manual

## Introduction

The `match_parens` function is a simple Python utility designed to determine if two strings of parentheses can be concatenated in some order to form a balanced string. A balanced string is one where every opening parenthesis '(' has a corresponding closing parenthesis ')'.

## Main Functionality

- **Function Name**: `match_parens`
- **Input**: A list containing two strings, each consisting solely of the characters '(' and ')'.
- **Output**: Returns 'Yes' if there is a way to concatenate the two strings to form a balanced string, and 'No' otherwise.

### Example Usage

- `match_parens(['()(', ')'])` returns `'Yes'`
- `match_parens([')', ')'])` returns `'No'`

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `match_parens` function.

2. **Run the Function**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `main.py`.
   - Run Python in interactive mode by typing `python` or `python3` depending on your installation.
   - Import the function using: 
     ```python
     from main import match_parens
     ```
   - Call the function with your desired input:
     ```python
     result = match_parens(['()(', ')'])
     print(result)  # Output: 'Yes'
     ```

## Documentation

The function is straightforward and does not require additional libraries or frameworks. It uses a helper function `is_balanced` to check if a given string of parentheses is balanced. The main logic checks both possible concatenations of the input strings to determine if either results in a balanced string.

For more detailed information or support, please refer to the comments within the `main.py` file, which explain the logic and flow of the function.

## Support

For further assistance or to report issues, please contact our support team through our official website or support email. We are committed to helping you resolve any issues and improve your experience with our software.