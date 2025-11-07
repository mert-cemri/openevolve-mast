# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to handle strings containing multiple groups of nested parentheses and separate them into individual balanced groups.

## Main Function

The main function provided by this software is `separate_paren_groups`. This function takes a string as input and returns a list of strings, each representing a separate group of balanced parentheses.

### Function Signature

```python
def separate_paren_groups(paren_string: str) -> List[str]:
```

### Parameters

- `paren_string` (str): A string containing multiple groups of nested parentheses. Spaces in the input string are ignored.

### Returns

- `List[str]`: A list of strings, each representing a separate group of balanced parentheses.

### Example

```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```

## Installation

This project does not require any external dependencies. You can simply use the provided Python script to run the function.

### Quick Setup

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where the project is located.

3. **Run the Script**: You can directly run the script using Python.

   ```bash
   python main.py
   ```

## Usage

To use the `separate_paren_groups` function, you can import it into your own Python script or use it directly in the provided `main.py` file.

### Example Usage

```python
from main import separate_paren_groups

# Example input
input_string = '( ) (( )) (( )( ))'

# Get the separated groups
groups = separate_paren_groups(input_string)

# Output the result
print(groups)  # Output: ['()', '(())', '(()())']
```

## Documentation

For further documentation and examples, please refer to the inline comments and docstrings within the `main.py` file. These provide detailed explanations of the function's behavior and usage.

This software is designed to be simple and efficient, focusing solely on the task of separating balanced parentheses groups from a given string. Enjoy using the Parentheses Group Separator!