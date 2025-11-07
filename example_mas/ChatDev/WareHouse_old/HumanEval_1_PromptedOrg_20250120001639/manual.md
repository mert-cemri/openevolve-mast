# Parentheses Group Separator

This software provides a function to separate groups of nested parentheses from a given string. It is designed to identify and extract balanced groups of parentheses, ignoring any spaces in the input string.

## Main Functionality

The main function of this software is `separate_paren_groups`, which takes a string containing multiple groups of nested parentheses and returns a list of separate strings, each representing a balanced group of parentheses.

### Example

```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```

## Quick Install

This software does not require any external dependencies. You can use it directly in your Python environment.

### Installation Steps

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing the `main.py` file.

4. You can now use the function in your Python scripts or interactive shell.

## How to Use

1. Open your Python environment (e.g., Python shell, Jupyter Notebook, or any Python IDE).

2. Import the function from the `main.py` file:

    ```python
    from main import separate_paren_groups
    ```

3. Call the function with a string containing groups of nested parentheses:

    ```python
    result = separate_paren_groups('( ) (( )) (( )( ))')
    print(result)  # Output: ['()', '(())', '(()())']
    ```

## Documentation

The function `separate_paren_groups` is designed to handle strings with multiple groups of nested parentheses. It ensures that each group is balanced, meaning every opening parenthesis has a corresponding closing parenthesis, and groups are not nested within each other.

- **Input:** A string containing multiple groups of nested parentheses.
- **Output:** A list of strings, each representing a balanced group of parentheses.

### Important Notes

- Spaces in the input string are ignored.
- The function assumes that the input string contains valid groups of parentheses.

For further assistance or questions, please contact our support team.