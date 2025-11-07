# File Name Check Software

This software provides a function to validate file names based on specific criteria. It is designed to ensure that file names adhere to a set of rules, making them suitable for certain applications or systems.

## Main Function

The primary function of this software is `file_name_check(file_name)`. This function takes a string representing a file's name and returns 'Yes' if the file's name is valid, and 'No' otherwise. The validation criteria are as follows:

- The file name must contain exactly one dot ('.').
- The substring before the dot must not be empty and must start with a letter from the Latin alphabet ('a'-'z' or 'A'-'Z').
- The substring after the dot must be one of the following: 'txt', 'exe', 'dll'.
- The file name must not contain more than three digits ('0'-'9').

### Examples

- `file_name_check("example.txt")` returns 'Yes'
- `file_name_check("1example.dll")` returns 'No' (the name should start with a Latin alphabet letter)

## Installation

This software does not require any external dependencies. You can use it directly in your Python environment.

### Quick Start

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change into the directory containing the `main.py` file:

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function:**

   You can use the function in your Python scripts or interactively in a Python shell. Here is an example of how to use it:

   ```python
   from main import file_name_check

   print(file_name_check("example.txt"))  # Output: 'Yes'
   print(file_name_check("1example.dll")) # Output: 'No'
   ```

## Usage

To use the `file_name_check` function, simply import it into your Python script and call it with the file name you wish to validate. The function will return 'Yes' if the file name is valid according to the specified criteria, and 'No' otherwise.

## Documentation

For further details on how the function works, you can refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and criteria used for file name validation.

## Support

If you encounter any issues or have questions about the software, please feel free to reach out to our support team. We are here to help you ensure that your file names meet the necessary standards.