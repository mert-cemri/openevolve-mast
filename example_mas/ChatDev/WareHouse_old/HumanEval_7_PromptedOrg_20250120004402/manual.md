# Filter by Substring

This software provides a simple utility function to filter a list of strings based on the presence of a specified substring. It is implemented in Python and does not require any external dependencies.

## Main Function

The main function of this software is `filter_by_substring`, which takes a list of strings and a substring as input and returns a new list containing only the strings that include the specified substring.

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

Since this software does not require any external dependencies, you can use it directly without any additional installation steps. Ensure you have Python installed on your system.

## How to Use

1. **Clone or Download the Repository**

   Clone the repository to your local machine or download the `main.py` file directly.

2. **Run the Code**

   You can run the code by importing the function into your Python script or interactive session. Here's an example:

   ```python
   from main import filter_by_substring

   # Example usage
   strings = ['abc', 'bacd', 'cde', 'array']
   substring = 'a'
   filtered_strings = filter_by_substring(strings, substring)
   print(filtered_strings)  # Output: ['abc', 'bacd', 'array']
   ```

3. **Testing**

   You can test the function with different inputs to ensure it works as expected. The function is designed to handle empty lists and will return an empty list if no strings contain the specified substring.

## Documentation

The function is documented with a docstring that includes usage examples. You can view this documentation directly in the `main.py` file or by using Python's built-in help function:

```python
help(filter_by_substring)
```

This will display the docstring and provide you with information on how to use the function.

## Conclusion

This software provides a straightforward utility for filtering strings by a substring. It is easy to use and integrate into your Python projects. If you have any questions or need further assistance, please feel free to reach out.