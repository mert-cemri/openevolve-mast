# Parse Nested Parentheses

This software provides a function to calculate the deepest level of nesting of parentheses for each group in a given string. It is designed to handle multiple groups of nested parentheses separated by spaces.

## Main Function

### `parse_nested_parens`

- **Description**: This function takes a string input representing multiple groups of nested parentheses separated by spaces. For each group, it outputs the deepest level of nesting of parentheses.
  
- **Input**: A string with groups of nested parentheses separated by spaces. For example: `'(()()) ((())) () ((())()())'`.

- **Output**: A list of integers, where each integer represents the maximum depth of nesting for the corresponding group. For example: `[2, 3, 1, 3]`.

- **Example Usage**:
  ```python
  from typing import List

  def parse_nested_parens(paren_string: str) -> List[int]:
      groups = paren_string.split()
      max_depths = []
      for group in groups:
          current_depth = 0
          max_depth = 0
          for char in group:
              if char == '(':
                  current_depth += 1
                  max_depth = max(max_depth, current_depth)
              elif char == ')':
                  current_depth -= 1
          max_depths.append(max_depth)
      return max_depths

  # Example
  result = parse_nested_parens('(()()) ((())) () ((())()())')
  print(result)  # Output: [2, 3, 1, 3]
  ```

## Installation

To use this function, you need to have Python installed on your system. You can download Python from the official website: [python.org](https://www.python.org/).

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**:
   ```bash
   cd <repository-directory>
   ```

3. **Install Dependencies**: If there are any dependencies, install them using:
   ```bash
   pip install -r requirements.txt
   ```

   Note: The current implementation does not require any external dependencies beyond the standard Python library.

## How to Use

1. **Prepare Your Input**: Ensure your input string is formatted correctly, with groups of nested parentheses separated by spaces.

2. **Run the Function**: Use the `parse_nested_parens` function to calculate the maximum depth of nesting for each group.

3. **Interpret the Output**: The function will return a list of integers, each representing the maximum depth of nesting for the corresponding group in the input string.

## Documentation

For further details and examples, refer to the function's docstring and comments within the code. This will provide additional insights into how the function processes the input and calculates the nesting depth.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided within the code comments.