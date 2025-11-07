# Parentheses Group Separator

This software provides a function to separate groups of balanced parentheses from a given string. It is designed to handle strings containing multiple groups of nested parentheses and return them as separate strings in a list.

## Main Functionality

The main function of this software is `separate_paren_groups`, which takes a string as input and returns a list of strings, each representing a group of balanced parentheses. The function ignores spaces in the input string and ensures that each group is properly balanced and not nested within each other.

### Example Usage

```python
from main import separate_paren_groups

# Example input
input_string = '( ) (( )) (( )( ))'

# Function call
result = separate_paren_groups(input_string)

# Output
print(result)  # Output: ['()', '(())', '(()())']
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the code by cloning the repository or downloading the ZIP file.

3. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the code is located.

4. **Run the Code**: You can directly run the code using a Python interpreter.

## How to Use

1. **Prepare Your Input**: Ensure your input string contains groups of balanced parentheses. Spaces will be ignored by the function.

2. **Call the Function**: Use the `separate_paren_groups` function to process your input string.

3. **Get the Result**: The function will return a list of strings, each representing a separate group of balanced parentheses.

## Additional Information

- **No External Libraries**: The software is designed to be lightweight and does not require any external libraries or dependencies.

- **Python Compatibility**: Ensure you are using a compatible version of Python (preferably Python 3.x) for optimal performance.

This manual provides all the necessary information to effectively use the Parentheses Group Separator software. If you encounter any issues or have further questions, please feel free to reach out for support.