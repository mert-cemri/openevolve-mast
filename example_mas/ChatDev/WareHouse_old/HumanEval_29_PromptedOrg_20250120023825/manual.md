# Filter by Prefix

This software module provides a simple utility function for filtering a list of strings based on a given prefix. It is designed to be lightweight and easy to integrate into any Python application where such functionality is needed.

## Main Functionality

The primary function provided by this module is `filter_by_prefix`. This function takes a list of strings and a prefix, returning a new list containing only the strings that start with the specified prefix.

### Function Signature

```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
```

### Parameters

- `strings` (List[str]): The list of strings to filter.
- `prefix` (str): The prefix to filter strings by.

### Returns

- List[str]: A list of strings that start with the given prefix.

### Example Usage

```python
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

## Installation

This module does not require any external dependencies, making it straightforward to use in any Python environment.

### Quick Install

Since there are no external dependencies, you can directly use the module in your Python project. Simply include the `main.py` file in your project directory.

## How to Use

1. **Include the Module**: Ensure that the `main.py` file containing the `filter_by_prefix` function is in your project directory.

2. **Import the Function**: In your Python script, import the function using:
   ```python
   from main import filter_by_prefix
   ```

3. **Call the Function**: Use the function by passing a list of strings and the desired prefix:
   ```python
   result = filter_by_prefix(['example', 'test', 'execute', 'examine'], 'ex')
   print(result)  # Output: ['example', 'execute', 'examine']
   ```

## Documentation

For further details and examples, refer to the docstring within the `main.py` file. The docstring provides comprehensive information on the function's usage, parameters, and return values.

This module is designed to be simple and efficient, making it an ideal choice for applications that require filtering strings by a prefix without the overhead of additional dependencies.