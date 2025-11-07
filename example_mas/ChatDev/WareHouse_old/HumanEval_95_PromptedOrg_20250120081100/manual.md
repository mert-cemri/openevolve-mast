# CheckDictCase User Manual

## Introduction

The `check_dict_case` function is a simple utility designed to evaluate the keys of a dictionary. It determines whether all keys are either in lowercase or uppercase. This function is useful for ensuring consistency in dictionary key formatting, which can be crucial for data processing and validation tasks.

### Main Functionality

- **check_dict_case(d):** This function takes a dictionary `d` as input and returns:
  - `True` if all keys are strings and either all are in lowercase or all are in uppercase.
  - `False` if the dictionary is empty, contains non-string keys, or if the keys are a mix of lowercase and uppercase.

### Examples

- `check_dict_case({"a":"apple", "b":"banana"})` returns `True`.
- `check_dict_case({"a":"apple", "A":"banana", "B":"banana"})` returns `False`.
- `check_dict_case({"a":"apple", 8:"banana", "a":"apple"})` returns `False`.
- `check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})` returns `False`.
- `check_dict_case({"STATE":"NC", "ZIP":"12345" })` returns `True`.

## Installation

### Environment Setup

This function does not require any external dependencies, making it straightforward to integrate into any Python environment. Ensure you have Python installed on your system.

### Installation Steps

1. **Clone the Repository:**
   If the function is part of a larger project, clone the repository using:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd <project-directory>
   ```

3. **Install Python (if not already installed):**
   Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

4. **No Additional Dependencies:**
   Since there are no external dependencies, you can directly use the function in your Python scripts.

## Usage

To use the `check_dict_case` function, follow these steps:

1. **Import the Function:**
   If the function is part of a module, import it into your script:
   ```python
   from main import check_dict_case
   ```

2. **Call the Function:**
   Pass a dictionary to the function and capture the result:
   ```python
   result = check_dict_case({"a": "apple", "b": "banana"})
   print(result)  # Output: True
   ```

3. **Integrate into Your Application:**
   Use the function as needed within your application to ensure dictionary key consistency.

## Conclusion

The `check_dict_case` function is a lightweight and efficient tool for validating dictionary key formats. Its simplicity and lack of dependencies make it easy to integrate into any Python project. Use this function to maintain consistency and avoid errors related to key formatting in your data processing tasks.