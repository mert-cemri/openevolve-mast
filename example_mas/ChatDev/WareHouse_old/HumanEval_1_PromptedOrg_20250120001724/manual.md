# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to handle strings containing multiple groups of nested parentheses, separating each group into individual strings and returning them as a list. The function ensures that each group is balanced, meaning every open parenthesis is properly closed, and ignores any spaces in the input string.

## Main Function

### `separate_paren_groups`

- **Description**: This function takes a string containing multiple groups of nested parentheses and separates those groups into individual strings. Each group is balanced and not nested within each other.
- **Input**: A string containing groups of parentheses.
- **Output**: A list of strings, each representing a separate group of balanced parentheses.

#### Example Usage

```python
from main import separate_paren_groups

paren_string = '( ) (( )) (( )( ))'
result = separate_paren_groups(paren_string)
print(result)  # Output: ['()', '(())', '(()())']
```

## Installation

This project does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

1. **Ensure you have Python installed**: This software requires Python to run. You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository**: If you have access to the repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the code**: You can execute the function directly in a Python environment or script.

## How to Use

1. **Import the function**: Ensure that the `main.py` file is in your working directory or in your Python path.

2. **Call the function**: Use the `separate_paren_groups` function by passing a string with groups of parentheses.

3. **Process the output**: The function will return a list of strings, each representing a separate group of balanced parentheses.

## Documentation

For further details on how the function works, refer to the docstring within the `main.py` file. The docstring provides a concise explanation of the function's purpose, input, and output.

This software is designed to be simple and efficient, focusing solely on the task of separating groups of balanced parentheses. If you encounter any issues or have questions, please feel free to reach out for support.