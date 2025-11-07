# Words String Splitter

This software module provides a simple function to split a string of words separated by commas or spaces into an array of words. It is designed to be straightforward and efficient, requiring no external dependencies.

## Main Function

The main function provided by this module is `words_string(s)`. This function takes a single string argument and returns a list of words. The string can contain words separated by either commas or spaces.

### Function Definition

```python
def words_string(s):
    """
    Splits a string into words separated by commas or spaces and returns a list of words.
    
    Args:
    s (str): A string of words separated by commas or spaces.
    
    Returns:
    list: A list of words.
    
    Examples:
    >>> words_string("Hi, my name is John")
    ['Hi', 'my', 'name', 'is', 'John']
    >>> words_string("One, two, three, four, five, six")
    ['One', 'two', 'three', 'four', 'five', 'six']
    """
    return s.replace(',', ' ').split()
```

## Installation

This module does not require any external dependencies, making it easy to integrate into any Python environment.

### Quick Install

Since there are no dependencies, you can directly use the function in your Python environment. Simply copy the function into your Python script or module.

## Usage

To use the `words_string` function, follow these steps:

1. **Import or Define the Function**: Ensure that the function is available in your script. You can copy the function definition provided above into your Python file.

2. **Call the Function**: Pass a string of words separated by commas or spaces to the function.

### Example Usage

```python
# Example 1
result1 = words_string("Hi, my name is John")
print(result1)  # Output: ['Hi', 'my', 'name', 'is', 'John']

# Example 2
result2 = words_string("One, two, three, four, five, six")
print(result2)  # Output: ['One', 'two', 'three', 'four', 'five', 'six']
```

## Documentation

The function is self-contained and does not require additional documentation. The docstring within the function provides a clear explanation of its purpose, usage, and examples.

For any further questions or support, please contact our development team.