# File Name Checker

This software provides a function to validate file names based on specific criteria. It is designed to ensure that file names adhere to a set of rules, making it useful for applications where file naming conventions are important.

## Main Functionality

The primary function of this software is `file_name_check(file_name)`, which evaluates whether a given file name is valid according to the following rules:

- The file name must contain exactly one dot (`.`).
- The substring before the dot must not be empty and must start with a letter from the Latin alphabet (`a-z` or `A-Z`).
- The file name must not contain more than three digits (`0-9`).
- The substring after the dot must be one of the following extensions: `txt`, `exe`, or `dll`.

### Examples

- `file_name_check("example.txt")` returns `'Yes'` because the file name is valid.
- `file_name_check("1example.dll")` returns `'No'` because the name should start with a Latin alphabet letter.

## Installation

This project does not require any external dependencies, so you can use it directly without installing additional packages.

## Usage

To use the `file_name_check` function, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the code from `main.py` into your Python environment or script.
3. Call the `file_name_check` function with a string argument representing the file name you want to validate.

### Example Usage

```python
def file_name_check(file_name):
    # Check if there is exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    # Split the file name into name and extension
    name, extension = file_name.rsplit('.', 1)
    # Check if the name part is not empty and starts with a letter
    if not name or not name[0].isalpha():
        return 'No'
    # Count the number of digits in the name part
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

## Conclusion

This software provides a simple yet effective way to validate file names based on predefined rules. It can be easily integrated into larger applications where file naming conventions need to be enforced.