# Parse Nested Parentheses

This software provides a function to parse nested parentheses in a string and determine the deepest level of nesting for each group of parentheses. It is designed to handle multiple groups of parentheses separated by spaces and return a list of integers representing the maximum nesting level for each group.

## Main Function

The main function provided by this software is `parse_nested_parens`. This function takes a single input, a string containing multiple groups of nested parentheses separated by spaces, and returns a list of integers. Each integer in the list represents the deepest level of nesting for the corresponding group of parentheses in the input string.

### Function Signature

```python
def parse_nested_parens(paren_string: str) -> List[int]:
```

### Example Usage

```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

In this example, the function returns a list `[2, 3, 1, 3]`, indicating the maximum nesting levels for each group of parentheses in the input string.

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Start

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory containing the `main.py` file.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can run the function directly in a Python interpreter or script.

   ```python
   from main import parse_nested_parens

   result = parse_nested_parens('(()()) ((())) () ((())()())')
   print(result)  # Output: [2, 3, 1, 3]
   ```

## Documentation

### Getting Started

To get started with using the `parse_nested_parens` function, ensure you have Python installed on your system. You can then use the function in any Python script or interactive session by importing it from the `main.py` file.

### How-To Examples

- **Basic Example**: Parse a simple string with multiple groups of parentheses.

  ```python
  result = parse_nested_parens('() (()) ((()))')
  print(result)  # Output: [1, 2, 3]
  ```

- **Complex Example**: Handle strings with varying levels of nesting.

  ```python
  result = parse_nested_parens('(()(())) () ((())())')
  print(result)  # Output: [3, 1, 3]
  ```

## Resources

For further information and examples, you can refer to the inline documentation provided in the `main.py` file. This includes a detailed docstring for the `parse_nested_parens` function, explaining its input, output, and usage with examples.