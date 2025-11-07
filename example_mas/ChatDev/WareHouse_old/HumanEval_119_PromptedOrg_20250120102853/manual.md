# Parentheses Matcher

This software provides a function to determine if two strings of parentheses can be concatenated in some order to form a balanced string. A balanced string is one where every opening parenthesis '(' has a corresponding closing parenthesis ')'.

## Main Functionality

The main function provided by this software is `match_parens`, which checks if two given strings of parentheses can be concatenated to form a balanced string. The function returns 'Yes' if it is possible, and 'No' otherwise.

### Function: `match_parens(lst)`

- **Input**: A list of two strings, each consisting of only '(' and ')'.
- **Output**: A string, either 'Yes' or 'No'.

#### Examples

- `match_parens(['()(', ')'])` returns `'Yes'`
- `match_parens([')', ')'])` returns `'No'`

## Installation

This software does not require any external dependencies. It is implemented purely in Python, so you only need a Python environment to run it.

### Setting Up Your Environment

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the code**: You can execute the function in a Python environment or script.

## Usage

To use the `match_parens` function, you can include it in your Python script or run it in an interactive Python session. Here's a quick guide on how to use it:

1. **Open a Python environment**: You can use the command line to start a Python interactive session by typing `python` or `python3`.

2. **Define the function**: Copy the `match_parens` function into your Python environment.

3. **Call the function**: Pass a list of two strings to the function and observe the output.

   ```python
   result = match_parens(['()(', ')'])
   print(result)  # Output: 'Yes'
   ```

4. **Test with different inputs**: You can test the function with different combinations of parentheses strings to see if they can form a balanced string.

## Documentation

For further information or detailed examples, please refer to the comments within the `main.py` file. The function is documented to provide clarity on its usage and expected behavior.