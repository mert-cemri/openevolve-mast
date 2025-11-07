manual.md

```
# Filter by Substring

A simple Python utility to filter a list of strings based on the presence of a given substring.

## Overview

This software provides a function `filter_by_substring` that takes a list of strings and a substring as inputs and returns a new list containing only the strings that include the specified substring. This can be useful for tasks such as searching, filtering, and data processing where you need to isolate strings containing specific patterns.

## Main Function

### `filter_by_substring(strings: List[str], substring: str) -> List[str]`

- **Purpose**: Filters an input list of strings to include only those that contain the specified substring.
- **Parameters**:
  - `strings`: A list of strings to be filtered.
  - `substring`: The substring to search for within each string.
- **Returns**: A list of strings from the input list that contain the specified substring.

#### Example Usage

```python
from main import filter_by_substring

# Example 1: Empty list
result = filter_by_substring([], 'a')
print(result)  # Output: []

# Example 2: List with strings containing 'a'
result = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
print(result)  # Output: ['abc', 'bacd', 'array']
```

## Installation

### Environment Setup

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Navigate to the directory** containing `main.py` in your terminal or command prompt.

3. **Run your Python script** using the Python interpreter. For example:

   ```bash
   python main.py
   ```

## Usage

To use the `filter_by_substring` function, simply import it into your Python script or interactive session and call it with the appropriate arguments as demonstrated in the example usage section.

## Documentation

For further details and advanced usage, refer to the inline documentation within the `main.py` file. The function is well-documented with docstrings that provide additional context and examples.

```