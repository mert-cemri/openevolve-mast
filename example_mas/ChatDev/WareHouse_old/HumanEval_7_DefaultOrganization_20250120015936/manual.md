manual.md

```
# Filter by Substring

This software module provides a simple utility function to filter a list of strings based on a given substring. It is designed to be lightweight and easy to use, with no external dependencies required.

## Main Functionality

The main function provided by this module is `filter_by_substring`. This function takes a list of strings and a substring as input and returns a new list containing only the strings that include the specified substring.

### Function Signature

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
```

### Example Usage

```python
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
```

## Installation

Since this module does not require any external dependencies, you can use it directly in your Python environment. Simply ensure that you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the module**: Obtain the `main.py` file containing the function.

## How to Use

1. **Import the function**: In your Python script, import the `filter_by_substring` function from the module.

```python
from main import filter_by_substring
```

2. **Call the function**: Use the function by passing a list of strings and the substring you want to filter by.

```python
result = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
print(result)  # Output: ['abc', 'bacd', 'array']
```

## Documentation

For further details on how to use the function, refer to the docstring within the `main.py` file. The docstring provides examples and a brief description of the function's purpose and usage.

## Support

If you encounter any issues or have questions about the module, please contact our support team for assistance.

```