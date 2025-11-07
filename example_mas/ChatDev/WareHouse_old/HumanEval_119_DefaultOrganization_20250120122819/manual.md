manual.md

```
# Parentheses Matcher

A simple Python application to determine if two strings of parentheses can be concatenated in some order to form a balanced string.

## Overview

The Parentheses Matcher is a utility function designed to check if two given strings, consisting solely of open '(' and close ')' parentheses, can be concatenated in any order to form a balanced string. A string is considered balanced if every opening parenthesis has a corresponding closing parenthesis and they are correctly nested.

### Main Function

- **match_parens(lst):** This function takes a list of two strings as input and returns 'Yes' if there is a way to concatenate the two strings such that the resulting string is balanced, and 'No' otherwise.

### Example Usage

```python
# Example 1
result = match_parens(['()(', ')'])
print(result)  # Output: 'Yes'

# Example 2
result = match_parens([')', ')'])
print(result)  # Output: 'No'
```

## Installation

### Prerequisites

- Python 3.x

### Environment Setup

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Navigate to the project directory** where `main.py` is located.

3. **Install Python** if it is not already installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

4. **No external dependencies** are required for this application, as specified in the `requirements.txt` file.

## How to Use

1. **Open a terminal or command prompt**.

2. **Navigate to the directory** containing the `main.py` file.

3. **Run the Python script** using the following command:

   ```bash
   python main.py
   ```

4. **Modify the script** to test different inputs by changing the list passed to the `match_parens` function.

## Documentation

For further details on how the function works, refer to the comments within the `main.py` file. The function is self-contained and does not require any additional libraries or frameworks.

```