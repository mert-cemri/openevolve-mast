# CheckDictCase User Manual

## Introduction

The `check_dict_case` function is a simple Python utility designed to evaluate the case consistency of dictionary keys. It checks whether all keys in a given dictionary are either all lowercase or all uppercase strings. If the dictionary is empty or contains keys that do not meet these criteria, the function returns `False`.

## Main Functionality

- **Function Name**: `check_dict_case`
- **Purpose**: To determine if all keys in a dictionary are uniformly in lowercase or uppercase.
- **Returns**: 
  - `True` if all keys are strings in either all lowercase or all uppercase.
  - `False` if the dictionary is empty or if the keys are mixed case, non-string, or a combination of these.

### Examples

- `check_dict_case({"a":"apple", "b":"banana"})` returns `True`.
- `check_dict_case({"a":"apple", "A":"banana", "B":"banana"})` returns `False`.
- `check_dict_case({"a":"apple", 8:"banana", "a":"apple"})` returns `False`.
- `check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})` returns `False`.
- `check_dict_case({"STATE":"NC", "ZIP":"12345" })` returns `True`.

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Setup

1. **Ensure Python is installed**: Verify that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can directly run the `main.py` file to test the function.
   ```bash
   python main.py
   ```

## Usage

To use the `check_dict_case` function, simply import it into your Python script and pass a dictionary as an argument. Here is an example of how to use it:

```python
from main import check_dict_case

# Example dictionary
example_dict = {"a": "apple", "b": "banana"}

# Check if all keys are in the same case
result = check_dict_case(example_dict)

print(result)  # Output: True
```

## Conclusion

The `check_dict_case` function is a lightweight and efficient tool for checking the case consistency of dictionary keys in Python. With no external dependencies, it is easy to integrate into any Python project. Whether you are working on data validation or simply need to ensure uniformity in your dictionary keys, this function provides a straightforward solution.