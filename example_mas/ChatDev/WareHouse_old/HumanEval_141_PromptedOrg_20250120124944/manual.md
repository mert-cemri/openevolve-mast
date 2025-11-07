# File Name Check Software

This software provides a function `file_name_check` that validates a file name based on specific criteria. It is designed to ensure that file names meet certain conditions, making them valid for use in various applications.

## Main Function

### `file_name_check(file_name)`

- **Purpose**: Validates a file name based on predefined criteria.
- **Input**: A string representing the file's name.
- **Output**: Returns 'Yes' if the file's name is valid, and 'No' otherwise.

### Criteria for a Valid File Name

1. **Digit Count**: The file name should not contain more than three digits ('0'-'9').
2. **Dot Count**: The file name must contain exactly one dot '.'.
3. **Name Before Dot**: The substring before the dot should not be empty and must start with a letter from the Latin alphabet ('a'-'z' or 'A'-'Z').
4. **Extension**: The substring after the dot should be one of the following: ['txt', 'exe', 'dll'].

### Examples

- `file_name_check("example.txt")` returns 'Yes'
- `file_name_check("1example.dll")` returns 'No' (the name should start with a Latin alphabet letter)

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Install

1. Ensure you have Python installed on your system.
2. No additional packages are required, so you can directly use the function in your Python scripts.

## How to Use

1. **Copy the Code**: Copy the `file_name_check` function from the provided code snippet into your Python script.
2. **Call the Function**: Use the function by passing a file name string as an argument.
3. **Receive Output**: The function will return 'Yes' if the file name is valid and 'No' otherwise.

### Example Usage

```python
# Example usage of the file_name_check function
print(file_name_check("example.txt"))  # Output: Yes
print(file_name_check("1example.dll")) # Output: No
```

## Documentation

For further details on how to use the function and examples of valid and invalid file names, refer to the comments within the code. The function is self-contained and does not require additional documentation.

This software is designed to be simple and easy to integrate into your existing Python projects, providing a straightforward solution for file name validation.