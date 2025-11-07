# Filter by Substring

This software module provides a simple function to filter a list of strings based on a given substring. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The primary function provided by this module is `filter_by_substring`. This function takes a list of strings and a substring as input and returns a new list containing only those strings from the input list that include the specified substring.

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

Since this module does not require any external dependencies, you can use it directly in your Python environment without any additional installation steps. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone or Download the Module:**

   Download the `main.py` file containing the `filter_by_substring` function.

2. **Import the Function:**

   In your Python script, import the function from the `main.py` file.

   ```python
   from main import filter_by_substring
   ```

3. **Call the Function:**

   Use the function by passing a list of strings and the substring you want to filter by.

   ```python
   result = filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
   print(result)  # Output: ['abc', 'bacd', 'array']
   ```

## Documentation

For further details and examples, refer to the docstring provided within the `main.py` file. The docstring includes usage examples and a description of the function's behavior.

This module is designed to be simple and straightforward, making it easy to integrate into larger projects or use as a standalone utility for filtering lists of strings.