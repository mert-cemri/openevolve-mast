# Filter by Substring

This software module provides a simple function to filter a list of strings based on the presence of a specified substring. It is designed to be lightweight and easy to integrate into larger Python applications.

## Main Function

The main function provided by this module is `filter_by_substring`.

### Function: `filter_by_substring`

- **Purpose**: Filters an input list of strings, returning only those strings that contain a specified substring.
- **Parameters**:
  - `strings` (List[str]): A list of strings to be filtered.
  - `substring` (str): The substring to filter the strings by.
- **Returns**: A list of strings that contain the specified substring.

#### Example Usage

```python
from main import filter_by_substring

# Example 1: Empty list
result1 = filter_by_substring([], 'a')
print(result1)  # Output: []

# Example 2: List with strings containing 'a'
result2 = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
print(result2)  # Output: ['abc', 'bacd', 'array']
```

## Installation

This module does not have any external dependencies, so installation is straightforward. You only need Python installed on your system.

### Quick Install

1. **Ensure you have Python installed**: You can download it from [python.org](https://www.python.org/).

2. **Clone or download the repository**: Place the `main.py` file in your project directory.

3. **Run your Python script**: Use the function `filter_by_substring` as demonstrated in the example usage section.

## Documentation

This module is designed to be simple and self-contained. For more advanced usage or integration into larger projects, consider the following:

- **Getting Started**: Simply import the function from the `main.py` file and use it in your Python scripts.
- **Integration**: This function can be easily integrated into larger applications where filtering of string lists is required.

For any further questions or support, please reach out to our development team. We are here to help you integrate this functionality into your projects efficiently.