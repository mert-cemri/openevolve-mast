manual.md

```
# File Name Checker

A simple Python utility to validate file names based on specific criteria. This tool ensures that file names meet certain conditions, making it useful for applications that require strict file naming conventions.

## Main Functionality

The primary function of this software is `file_name_check`, which takes a string representing a file's name and returns 'Yes' if the file's name is valid, and 'No' otherwise. The validation criteria are as follows:

- The file name should not contain more than three digits ('0'-'9').
- The file name must contain exactly one dot '.'.
- The substring before the dot should not be empty and must start with a letter from the Latin alphabet ('a'-'z' and 'A'-'Z').
- The substring after the dot should be one of the following: ['txt', 'exe', 'dll'].

### Examples

- `file_name_check("example.txt")` returns `'Yes'`.
- `file_name_check("1example.dll")` returns `'No'` (the name should start with a Latin alphabet letter).

## Installation

This project does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Setting Up the Environment

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If you have access to the repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:

   ```bash
   cd <project-directory>
   ```

4. **Run the script**: You can directly run the `main.py` file to test the function.

   ```bash
   python main.py
   ```

## Usage

To use the `file_name_check` function, simply import it into your Python script and call it with the file name you wish to validate.

```python
from main import file_name_check

result = file_name_check("example.txt")
print(result)  # Output: 'Yes'
```

This function is designed to be straightforward and easy to integrate into larger projects where file name validation is necessary.

## Documentation

For further details on the implementation and examples, please refer to the comments within the `main.py` file. The function is well-documented to help you understand the logic and adapt it if necessary.

```