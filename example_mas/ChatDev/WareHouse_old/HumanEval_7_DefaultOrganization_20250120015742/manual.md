# Filter by Substring

A simple Python utility to filter a list of strings based on the presence of a specified substring.

## Overview

This software provides a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only those strings from the input list that contain the specified substring.

## Main Functionality

- **filter_by_substring(strings: List[str], substring: str) -> List[str]**: This function filters an input list of strings, returning only those strings that contain the specified substring.

### Example Usage

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Example usage
result = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
print(result)  # Output: ['abc', 'bacd', 'array']
```

## Installation

### Environment Setup

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Running the Code

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Script**: Execute the script using Python.

   ```bash
   python main.py
   ```

## Usage

To use the `filter_by_substring` function, you can import it into your Python script and call it with the desired list of strings and the substring you want to filter by.

### Example

```python
from main import filter_by_substring

# Define a list of strings
strings = ['hello', 'world', 'python', 'programming']

# Define the substring to filter by
substring = 'o'

# Call the function
filtered_strings = filter_by_substring(strings, substring)

# Output the result
print(filtered_strings)  # Output: ['hello', 'world', 'python']
```

## Conclusion

This utility is a straightforward solution for filtering lists of strings based on substrings. It is designed to be simple and efficient, making it a useful tool for developers needing this functionality in their Python applications.