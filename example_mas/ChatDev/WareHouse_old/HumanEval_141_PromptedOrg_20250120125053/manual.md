# File Name Validator

This software provides a function to validate file names based on specific criteria. It is designed to ensure that file names adhere to a set of rules, making them valid for certain applications or systems.

## Main Functionality

The core functionality of this software is encapsulated in the `file_name_check` function. This function takes a string representing a file's name and returns 'Yes' if the file's name is valid, and 'No' otherwise. The criteria for a valid file name are:

- The file name must contain exactly one dot ('.').
- The substring before the dot must not be empty and must start with a letter from the Latin alphabet ('a'-'z' and 'A'-'Z').
- The substring after the dot must be one of the following: ['txt', 'exe', 'dll'].
- There must not be more than three digits ('0'-'9') in the file's name.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

## Usage

To use the `file_name_check` function, follow these steps:

1. **Clone the Repository:**
   - Clone the repository containing the `main.py` file to your local machine.

2. **Run the Function:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the `main.py` file.
   - Run the Python script using the command: `python main.py`.

3. **Example Usage:**
   - The script includes example usage of the `file_name_check` function. You can modify the examples or add new ones to test different file names.
   - Example:
     ```python
     print(file_name_check("example.txt"))  # Output: 'Yes'
     print(file_name_check("1example.dll")) # Output: 'No'
     ```

4. **Modify and Extend:**
   - You can modify the `main.py` file to include additional test cases or integrate the function into a larger application.

## Documentation

The function is documented within the code, providing a clear understanding of its purpose and usage. You can refer to the comments and docstrings in the `main.py` file for more details.

## Support

For any issues or questions regarding the usage of this software, please contact our support team. We are here to assist you in ensuring the software meets your needs effectively.