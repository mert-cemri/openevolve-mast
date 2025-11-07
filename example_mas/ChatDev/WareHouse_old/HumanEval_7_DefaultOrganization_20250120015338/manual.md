# Filter By Substring

This software module provides a simple utility function to filter a list of strings based on the presence of a specified substring. It is designed to be lightweight and efficient, requiring no external dependencies.

## Main Functionality

The primary function provided by this module is `filter_by_substring`. This function takes a list of strings and a substring as input and returns a new list containing only those strings from the input list that contain the specified substring.

### Function Signature

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
```

### Parameters

- `strings` (List[str]): The list of strings to filter.
- `substring` (str): The substring to search for within each string.

### Returns

- List[str]: A list of strings that contain the given substring.

### Example Usage

```python
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
```

## Installation

This module does not require any external dependencies, making it easy to integrate into your existing Python projects.

### Quick Install

Since there are no external dependencies, you can simply copy the `main.py` file into your project directory.

## How to Use

1. **Copy the Code**: Ensure that the `main.py` file containing the `filter_by_substring` function is in your project directory.

2. **Import the Function**: In your Python script, import the function using:

   ```python
   from main import filter_by_substring
   ```

3. **Call the Function**: Use the function by passing a list of strings and the substring you want to filter by:

   ```python
   result = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
   print(result)  # Output: ['abc', 'bacd', 'array']
   ```

## Documentation

For further details on the usage and examples, please refer to the inline documentation within the `main.py` file. The function is straightforward and designed to be self-explanatory for ease of use.

This module is ideal for applications where you need to quickly filter strings based on a substring without the overhead of additional libraries or complex setups.