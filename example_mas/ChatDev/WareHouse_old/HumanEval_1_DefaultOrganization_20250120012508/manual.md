# Parentheses Group Separator

This software provides a function to separate groups of nested parentheses from a given string. It is designed to handle strings containing multiple groups of balanced parentheses, separating them into individual strings.

## Main Functionality

The main function of this software is:

- **`separate_paren_groups(paren_string: str) -> List[str]`**: This function takes a string containing multiple groups of nested parentheses and returns a list of strings, each representing a separate group of balanced parentheses. Spaces in the input string are ignored.

### Example Usage

```python
from main import separate_paren_groups

# Example input
input_string = '( ) (( )) (( )( ))'
# Function call
result = separate_paren_groups(input_string)
# Output: ['()', '(())', '(()())']
print(result)
```

## Installation

This project does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

1. **Ensure you have Python installed**: This software requires Python to run. You can download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone or download the repository**: You can clone the repository using Git or download the ZIP file and extract it.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**: Open a terminal and navigate to the directory where the project files are located.

   ```bash
   cd <project-directory>
   ```

4. **Run the software**: You can run the software directly using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the function**: Import the `separate_paren_groups` function from the `main.py` file.

2. **Prepare your input**: Create a string containing groups of nested parentheses that you wish to separate.

3. **Call the function**: Pass your input string to the `separate_paren_groups` function and capture the output list.

4. **Process the output**: Use the returned list of strings as needed in your application.

## Documentation

This software is simple and straightforward, designed to perform a specific task efficiently. For any further questions or support, please refer to the code comments and docstrings within the `main.py` file for additional guidance on usage and functionality.