# File Name Check Utility

This utility provides a function to validate file names based on specific criteria. It is designed to ensure that file names conform to a set of rules, making them suitable for certain applications or systems.

## Main Functionality

The core functionality of this utility is encapsulated in the `file_name_check` function. This function takes a string representing a file's name and returns 'Yes' if the file's name is valid according to the specified criteria, and 'No' otherwise.

### Criteria for Valid File Names

A file name is considered valid if it meets all of the following conditions:

1. **Digit Count**: The file name must not contain more than three digits ('0'-'9').
2. **Dot Presence**: The file name must contain exactly one dot ('.').
3. **Prefix Requirements**: The substring before the dot must not be empty and must start with a letter from the Latin alphabet ('a'-'z' or 'A'-'Z').
4. **Extension Validity**: The substring after the dot must be one of the following: 'txt', 'exe', 'dll'.

### Examples

- `file_name_check("example.txt")` returns `'Yes'`
- `file_name_check("1example.dll")` returns `'No'` (the name should start with a Latin alphabet letter)

## Installation

This utility does not require any external dependencies, making it straightforward to use in any Python environment.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python project. Simply copy the code into your project or import it if you have saved it as a module.

## Usage

To use the `file_name_check` function, follow these steps:

1. **Copy the Code**: Ensure that the function code is available in your Python environment. You can copy the function from the provided code snippet.

2. **Call the Function**: Use the function by passing a file name string as an argument. The function will return 'Yes' or 'No' based on the validity of the file name.

```python
def file_name_check(file_name):
    # Split the file name by the dot
    parts = file_name.split('.')
    # Check if there is exactly one dot
    if len(parts) != 2:
        return 'No'
    name, extension = parts
    # Check if the name part is not empty and starts with a letter
    if not name or not name[0].isalpha():
        return 'No'
    # Count the number of digits in the name
    digit_count = sum(char.isdigit() for char in name)
    if digit_count > 3:
        return 'No'
    # Check if the extension is valid
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'

# Example usage
print(file_name_check("example.txt"))  # Output: Yes
print(file_name_check("1example.dll")) # Output: No
```

## Documentation

For further information on how to integrate this utility into larger projects or for advanced usage scenarios, please refer to the full documentation (if available) or contact the support team for assistance.