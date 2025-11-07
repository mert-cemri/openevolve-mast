# CheckDictCase User Manual

Welcome to the CheckDictCase software! This tool is designed to evaluate the keys of a dictionary to determine if they are all in lowercase or all in uppercase. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it.

## Main Functions

The primary function of this software is `check_dict_case`, which performs the following tasks:

- **Input**: A dictionary with keys and values.
- **Output**: A boolean value (`True` or `False`).
  - Returns `True` if all keys are strings and either all are in lowercase or all are in uppercase.
  - Returns `False` if the dictionary is empty, contains non-string keys, or if the keys are a mix of lowercase and uppercase.

### Examples

- `check_dict_case({"a":"apple", "b":"banana"})` returns `True`.
- `check_dict_case({"a":"apple", "A":"banana", "B":"banana"})` returns `False`.
- `check_dict_case({"a":"apple", 8:"banana", "a":"apple"})` returns `False`.
- `check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})` returns `False`.
- `check_dict_case({"STATE":"NC", "ZIP":"12345" })` returns `True`.

## Installation

This software does not require any external dependencies, making the installation process straightforward. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the source code by cloning the repository or downloading the ZIP file.

3. **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the directory where the source code is located.

## How to Use

To use the `check_dict_case` function, follow these steps:

1. **Open a Python Environment**: You can use any Python environment such as IDLE, PyCharm, or VSCode.

2. **Import the Function**: If you are using the function in a different script, make sure to import it.

3. **Call the Function**: Pass a dictionary as an argument to the `check_dict_case` function.

```python
# Example usage
from main import check_dict_case

result = check_dict_case({"a": "apple", "b": "banana"})
print(result)  # Output: True
```

4. **Interpret the Result**: The function will return `True` or `False` based on the criteria mentioned above.

## Conclusion

The CheckDictCase software is a simple yet effective tool for verifying the case consistency of dictionary keys. With no external dependencies, it is easy to set up and use. We hope this manual helps you get started quickly and effectively. If you have any questions or need further assistance, please feel free to reach out.