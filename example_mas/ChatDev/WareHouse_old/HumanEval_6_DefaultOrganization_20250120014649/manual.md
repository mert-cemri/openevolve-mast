# Parse Nested Parentheses

This software provides a function to determine the deepest level of nesting for groups of parentheses within a given string. It is designed to handle multiple groups of nested parentheses separated by spaces and return the maximum nesting level for each group.

## Main Functions

The main function provided by this software is `parse_nested_parens`, which takes a string input and returns a list of integers representing the deepest level of nesting for each group of parentheses.

### Function: `parse_nested_parens`

- **Input**: A string containing multiple groups of nested parentheses separated by spaces.
- **Output**: A list of integers, where each integer represents the maximum nesting level of the corresponding group of parentheses.

#### Example

```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def max_nesting_level(paren_group: str) -> int:
        max_level = 0
        current_level = 0
        for char in paren_group:
            if char == '(':
                current_level += 1
                if current_level > max_level:
                    max_level = current_level
            elif char == ')':
                current_level -= 1
        return max_level

    groups = paren_string.split()
    return [max_nesting_level(group) for group in groups]

# Example usage
if __name__ == "__main__":
    example_input = '(()()) ((())) () ((())()())'
    print(parse_nested_parens(example_input))  # Output: [2, 3, 1, 3]
```

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need to have Python installed on your system.

### Quick Install

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone the repository or download the `main.py` file to your local machine.

## How to Use

1. Open a terminal or command prompt.
2. Navigate to the directory where the `main.py` file is located.
3. Run the script using Python:

   ```bash
   python main.py
   ```

4. The script will execute the example usage and print the output `[2, 3, 1, 3]`, which corresponds to the deepest levels of nesting for each group of parentheses in the example input.

## Documentation

This software is straightforward and does not require additional documentation beyond this manual. The function `parse_nested_parens` is self-contained and can be easily integrated into other Python projects where similar functionality is needed.