# Parse Nested Parentheses

This software provides a function to calculate the deepest level of nested parentheses for each group in a given string. It is designed to handle multiple groups of nested parentheses separated by spaces and return a list of integers representing the maximum nesting level for each group.

## Main Function

The main function provided by this software is `parse_nested_parens`.

### Function: `parse_nested_parens`

- **Input**: A string containing multiple groups of nested parentheses separated by spaces.
- **Output**: A list of integers, where each integer represents the deepest level of nesting for the corresponding group of parentheses.

#### Example

```python
from main import parse_nested_parens

result = parse_nested_parens('(()()) ((())) () ((())()())')
print(result)  # Output: [2, 3, 1, 3]
```

## Installation

This software does not require any external dependencies, making it simple to set up and use.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory containing the `main.py` file.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can directly run the code as it does not require any additional setup.

## Usage

To use the `parse_nested_parens` function, follow these steps:

1. **Import the Function**: Import the `parse_nested_parens` function from the `main.py` file.

   ```python
   from main import parse_nested_parens
   ```

2. **Call the Function**: Pass a string containing groups of nested parentheses to the function.

   ```python
   result = parse_nested_parens('(()()) ((())) () ((())()())')
   ```

3. **Output the Result**: The function will return a list of integers representing the deepest level of nesting for each group.

   ```python
   print(result)  # Output: [2, 3, 1, 3]
   ```

## Documentation

For further information and examples, please refer to the inline documentation within the `main.py` file. The function is well-documented to provide clarity on its usage and expected input/output.

This software is designed to be straightforward and efficient, providing a simple solution to calculate the nesting levels of parentheses in a string.