manual.md

```
# CheckDictCase

CheckDictCase is a simple Python utility function designed to evaluate the case consistency of dictionary keys. It determines whether all keys in a given dictionary are either all lowercase or all uppercase strings. This function is particularly useful for data validation and preprocessing tasks where case consistency is required.

## Main Functionality

The primary function provided by this utility is `check_dict_case(d)`, which performs the following checks:

1. **Empty Dictionary Check**: Returns `False` if the dictionary is empty.
2. **Key Type Check**: Returns `False` if any key in the dictionary is not a string.
3. **Case Consistency Check**: Returns `True` if all keys are either all lowercase or all uppercase strings. Otherwise, it returns `False`.

### Examples

- `check_dict_case({"a":"apple", "b":"banana"})` returns `True`.
- `check_dict_case({"a":"apple", "A":"banana", "B":"banana"})` returns `False`.
- `check_dict_case({"a":"apple", 8:"banana", "a":"apple"})` returns `False`.
- `check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})` returns `False`.
- `check_dict_case({"STATE":"NC", "ZIP":"12345" })` returns `True`.

## Installation

This utility does not require any external dependencies, making it easy to integrate into any Python project.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python environment. Simply copy the function code into your project:

```python
def check_dict_case(d):
    # Check if the dictionary is empty
    if not d:
        return False
    # Check if all keys are strings
    if not all(isinstance(key, str) for key in d.keys()):
        return False
    # Check if all keys are lowercase
    all_lower = all(key.islower() for key in d.keys())
    # Check if all keys are uppercase
    all_upper = all(key.isupper() for key in d.keys())
    # Return True if all keys are either all lowercase or all uppercase
    return all_lower or all_upper
```

## Usage

To use the `check_dict_case` function, simply call it with a dictionary as an argument. The function will return a boolean value indicating whether the dictionary keys meet the specified case consistency criteria.

```python
# Example usage
result = check_dict_case({"a": "apple", "b": "banana"})
print(result)  # Output: True
```

## Documentation

For further information and updates, please refer to the project repository or contact the development team at ChatDev.

```