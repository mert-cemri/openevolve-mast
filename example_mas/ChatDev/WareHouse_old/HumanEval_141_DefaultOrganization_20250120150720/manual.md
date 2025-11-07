manual.md

```
# File Name Validator

This software provides a function to validate file names based on specific criteria. It is designed to ensure that file names meet certain standards, making it easier to manage and organize files effectively.

## Main Functionality

The core functionality of this software is encapsulated in the `file_name_check` function. This function takes a string representing a file's name and returns 'Yes' if the file's name is valid according to the following criteria, or 'No' otherwise:

- The file name should not contain more than three digits ('0'-'9').
- The file name must contain exactly one dot '.'.
- The substring before the dot should not be empty and must start with a letter from the Latin alphabet ('a'-'z' and 'A'-'Z').
- The substring after the dot should be one of the following: ['txt', 'exe', 'dll'].

### Examples

- `file_name_check("example.txt")` returns 'Yes'
- `file_name_check("1example.dll")` returns 'No' (the name should start with a Latin alphabet letter)

## Installation

This project does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Run the Function:**

   You can use the `file_name_check` function by importing it into your Python script or by running it directly in a Python shell.

   Example usage in a Python script:

   ```python
   from main import file_name_check

   result = file_name_check("example.txt")
   print(result)  # Output: 'Yes'
   ```

4. **Testing:**

   You can test the function with different file names to ensure it behaves as expected.

## Documentation

For further details on the function and its implementation, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and criteria used for file name validation.

## Support

If you encounter any issues or have questions, please feel free to reach out to our support team or open an issue in the repository.

```