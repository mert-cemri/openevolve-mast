manual.md

```
# CheckDictCase

A simple Python utility to verify if all keys in a dictionary are either all lowercase strings or all uppercase strings.

## Overview

The `check_dict_case` function is designed to help you determine the case consistency of dictionary keys. It checks if all keys are strings and whether they are all in lowercase or uppercase. If the dictionary is empty or contains non-string keys, the function will return `False`.

## Features

- **Case Consistency Check**: Determines if all keys in a dictionary are either all lowercase or all uppercase strings.
- **Validation**: Ensures that all keys are strings before performing the case check.
- **Empty Dictionary Handling**: Returns `False` if the dictionary is empty.

## Installation

This utility does not require any external dependencies. You only need Python installed on your system.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**: (if applicable)
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Ensure Python is Installed**: Verify that Python is installed on your system by running:
   ```bash
   python --version
   ```

3. **Run the Script**: No additional installation steps are required. You can directly use the function in your Python environment.

## Usage

To use the `check_dict_case` function, follow these steps:

1. **Import the Function**: Ensure the function is available in your script or Python environment.
   ```python
   from main import check_dict_case
   ```

2. **Call the Function**: Pass a dictionary to the function to check the case consistency of its keys.
   ```python
   result = check_dict_case({"a": "apple", "b": "banana"})
   print(result)  # Output: True

   result = check_dict_case({"a": "apple", "A": "banana", "B": "banana"})
   print(result)  # Output: False
   ```

## Examples

Here are some examples to illustrate the usage of the `check_dict_case` function:

- **All Lowercase Keys**:
  ```python
  print(check_dict_case({"a": "apple", "b": "banana"}))  # Output: True
  ```

- **Mixed Case Keys**:
  ```python
  print(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))  # Output: False
  ```

- **Non-String Key**:
  ```python
  print(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))  # Output: False
  ```

- **All Uppercase Keys**:
  ```python
  print(check_dict_case({"STATE": "NC", "ZIP": "12345"}))  # Output: True
  ```

## Conclusion

The `check_dict_case` function is a straightforward utility for checking the case consistency of dictionary keys. It is easy to use and integrates seamlessly into any Python project without requiring additional dependencies.
```