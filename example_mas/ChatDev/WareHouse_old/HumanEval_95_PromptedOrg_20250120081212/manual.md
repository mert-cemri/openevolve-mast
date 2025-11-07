manual.md

```
# CheckDictCase

A Python utility function to verify the case consistency of dictionary keys.

## Overview

The `check_dict_case` function is designed to evaluate whether all keys in a given dictionary are either all lowercase or all uppercase strings. The function returns `True` if this condition is met and `False` otherwise. Additionally, it returns `False` if the dictionary is empty or if any key is not a string.

## Features

- **Case Consistency Check**: Determines if all dictionary keys are either all lowercase or all uppercase.
- **Type Safety**: Ensures that all keys are strings.
- **Empty Dictionary Handling**: Returns `False` for empty dictionaries.

## Installation

This function does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Python Installation

If you do not have Python installed, you can download it from the official [Python website](https://www.python.org/downloads/).

## Usage

To use the `check_dict_case` function, follow these steps:

1. **Copy the Code**: Copy the function code into your Python script or interactive environment.

```python
def check_dict_case(d):
    # Check if the dictionary is empty
    if not d:
        return False
    # Initialize flags for lowercase and uppercase
    all_lower = True
    all_upper = True
    for key in d.keys():
        # Check if the key is a string
        if not isinstance(key, str):
            return False
        # Check if the key is lowercase
        if not key.islower():
            all_lower = False
        # Check if the key is uppercase
        if not key.isupper():
            all_upper = False
    # Return True if all keys are either all lowercase or all uppercase
    return all_lower or all_upper
```

2. **Call the Function**: Pass a dictionary to the `check_dict_case` function to evaluate its keys.

### Examples

```python
# Example 1: All lowercase keys
result = check_dict_case({"a": "apple", "b": "banana"})
print(result)  # Output: True

# Example 2: Mixed case keys
result = check_dict_case({"a": "apple", "A": "banana", "B": "banana"})
print(result)  # Output: False

# Example 3: Non-string key
result = check_dict_case({"a": "apple", 8: "banana", "a": "apple"})
print(result)  # Output: False

# Example 4: Mixed case keys
result = check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})
print(result)  # Output: False

# Example 5: All uppercase keys
result = check_dict_case({"STATE": "NC", "ZIP": "12345"})
print(result)  # Output: True
```

## Conclusion

The `check_dict_case` function is a simple yet effective tool for ensuring the case consistency of dictionary keys in Python. It is easy to integrate into existing projects and requires no additional dependencies.
```