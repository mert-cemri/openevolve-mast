# Parse Nested Parentheses

This software provides a function to analyze strings containing multiple groups of nested parentheses and determine the deepest level of nesting for each group. It is a simple utility written in Python, designed to handle strings of parentheses and return a list of integers representing the maximum nesting depth for each group.

## Main Functions

The core function of this software is:

- `parse_nested_parens(paren_string: str) -> List[int]`: This function takes a string input where multiple groups of nested parentheses are separated by spaces. It returns a list of integers, each representing the deepest level of nesting for the corresponding group of parentheses.

### Example

Given the input string `'(()()) ((())) () ((())()())'`, the function will return `[2, 3, 1, 3]`, indicating the maximum nesting levels for each group of parentheses.

## Installation

### Environment Setup

This project does not require any external dependencies, making it straightforward to set up. You only need Python installed on your system.

1. **Ensure Python is Installed**: Make sure you have Python 3.x installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**:

   ```bash
   cd <project-directory>
   ```

4. **Run the Script**: You can execute the script using Python:

   ```bash
   python main.py
   ```

## Usage

To use the `parse_nested_parens` function, you can either run the provided `main.py` script or import the function into your own Python scripts.

### Running the Script

The `main.py` script includes an example usage of the `parse_nested_parens` function. Simply run the script to see the output for the example input:

```bash
python main.py
```

### Importing the Function

If you want to use the function in your own code, you can import it as follows:

```python
from main import parse_nested_parens

# Example usage
input_string = '(()()) ((())) () ((())()())'
result = parse_nested_parens(input_string)
print(result)  # Output: [2, 3, 1, 3]
```

## Documentation

For further details on how the function works or to contribute to the project, please refer to the inline comments and docstrings within the `main.py` file. This will provide a deeper understanding of the logic and structure of the code.

Feel free to modify and extend the functionality as needed for your specific use cases.