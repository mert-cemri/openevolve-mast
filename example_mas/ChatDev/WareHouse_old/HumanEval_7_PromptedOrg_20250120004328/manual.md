# Filter By Substring

This software module provides a simple utility function to filter a list of strings based on the presence of a given substring. It is designed to be lightweight and easy to integrate into other Python projects.

## Main Function

The primary function provided by this module is `filter_by_substring`. This function takes a list of strings and a substring as input and returns a new list containing only those strings from the input list that contain the specified substring.

### Function Signature

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
```

### Parameters

- `strings` (List[str]): A list of strings to be filtered.
- `substring` (str): The substring to filter the strings by.

### Returns

- List[str]: A list of strings from the input list that contain the specified substring.

### Example Usage

```python
from main import filter_by_substring

# Example 1: Empty list
result1 = filter_by_substring([], 'a')
print(result1)  # Output: []

# Example 2: List with strings containing the substring 'a'
result2 = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
print(result2)  # Output: ['abc', 'bacd', 'array']
```

## Installation

This module does not require any external dependencies, making it straightforward to use. You can simply copy the `main.py` file into your project directory.

## How to Use

1. **Copy the `main.py` file**: Ensure the `main.py` file containing the `filter_by_substring` function is in your project directory.

2. **Import the function**: In your Python script, import the `filter_by_substring` function.

3. **Call the function**: Use the function by passing a list of strings and the substring you want to filter by.

## No External Dependencies

This module does not require any external libraries or dependencies. It uses only Python's built-in libraries, ensuring compatibility and ease of use.

## Conclusion

The `filter_by_substring` function is a simple yet powerful tool for filtering lists of strings. Its ease of use and lack of dependencies make it an ideal choice for projects that require string filtering functionality.