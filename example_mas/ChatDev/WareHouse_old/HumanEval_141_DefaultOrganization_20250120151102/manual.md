# File Name Validator

This software provides a function to validate file names based on specific criteria. It is designed to ensure that file names adhere to a set of rules, making them valid for certain applications or systems.

## Main Function

The primary function of this software is `file_name_check`, which evaluates a file name string and determines its validity based on the following criteria:

- The file name should not contain more than three digits ('0'-'9').
- The file name must contain exactly one dot ('.').
- The substring before the dot should not be empty and must start with a letter from the Latin alphabet ('a'-'z' and 'A'-'Z').
- The substring after the dot should be one of the following: ['txt', 'exe', 'dll'].

### Example Usage

```python
print(file_name_check("example.txt"))  # Output: 'Yes'
print(file_name_check("1example.dll")) # Output: 'No'
```

## Installation

This software does not require any external dependencies, making it straightforward to use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `file_name_check` function.

3. **Run the script**: Use a Python interpreter to execute the script and test the function with different file names.

## How to Use

1. **Open a terminal or command prompt**.

2. **Navigate to the directory** where `main.py` is located.

3. **Run the Python script**: Use the command `python main.py` to execute the script.

4. **Test the function**: Modify the script to include different file name strings and observe the output to determine if they are valid or not.

## Documentation

The function is documented with inline comments explaining each step of the validation process. This should provide sufficient guidance for understanding how the function works and how to modify it if necessary.

For further assistance or inquiries, please contact our support team.