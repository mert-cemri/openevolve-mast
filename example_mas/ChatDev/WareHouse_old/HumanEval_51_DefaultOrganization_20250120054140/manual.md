# Remove Vowels Function

This software module provides a simple function to remove vowels from a given string. It is designed to be lightweight and does not require any external dependencies.

## Main Functionality

The main function provided by this module is `remove_vowels`, which takes a string as input and returns a new string with all vowels removed. The function is case-insensitive and removes both uppercase and lowercase vowels.

### Function Definition

```python
def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)
```

## Installation

Since this module does not require any external libraries, there is no need to install additional dependencies. You can directly use the function in your Python environment.

## Usage

To use the `remove_vowels` function, follow these steps:

1. **Copy the Code**: Copy the function definition from the code snippet provided above into your Python script or interactive environment.

2. **Call the Function**: Use the function by passing a string as an argument. The function will return a new string with all vowels removed.

### Example Usage

```python
# Example 1: Removing vowels from a simple string
result = remove_vowels("abcdef")
print(result)  # Output: 'bcdf'

# Example 2: Removing vowels from a string with mixed case
result = remove_vowels("aaBAA")
print(result)  # Output: 'B'

# Example 3: Removing vowels from a string with newline characters
result = remove_vowels("abcdef\nghijklm")
print(result)  # Output: 'bcdf\nghjklm'
```

## Testing

The function includes several doctests to verify its correctness. You can run these tests by executing the following command in your terminal:

```bash
python -m doctest main.py
```

This command will run the embedded tests and report any failures. If all tests pass, the function is working as expected.

## Conclusion

This module provides a straightforward solution for removing vowels from strings. It is easy to integrate into existing projects and requires no additional setup. Feel free to modify and extend the function to suit your specific needs.