# File Name Check Software

This software provides a function to validate file names based on specific criteria. It is designed to ensure that file names adhere to a set of rules, making them suitable for certain applications or systems.

## Main Functionality

The core functionality of this software is encapsulated in the `file_name_check` function. This function evaluates a given file name string and determines if it is valid based on the following criteria:

1. **Digit Limitation**: The file name must not contain more than three digits ('0'-'9').
2. **Dot Requirement**: The file name must contain exactly one dot ('.').
3. **Name Validity**: The substring before the dot must not be empty and must start with a letter from the Latin alphabet ('a'-'z' or 'A'-'Z').
4. **Extension Validity**: The substring after the dot must be one of the following: 'txt', 'exe', or 'dll'.

### Example Usage

- `file_name_check("example.txt")` returns `'Yes'` because the file name meets all the criteria.
- `file_name_check("1example.dll")` returns `'No'` because the name does not start with a letter.

## Installation

This software does not require any external dependencies, making it straightforward to use. You can simply copy the code into your Python environment and start using it.

### Requirements

- Python 3.x

### Installation Steps

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Directory**: Change your working directory to where the code is located.
   ```bash
   cd <directory-name>
   ```
3. **Run the Code**: You can directly run the Python script containing the `file_name_check` function.

## How to Use

1. **Import the Function**: If you have saved the function in a separate file, import it into your script.
   ```python
   from main import file_name_check
   ```
2. **Call the Function**: Pass the file name you want to check as a string argument to the function.
   ```python
   result = file_name_check("example.txt")
   print(result)  # Output: 'Yes'
   ```

## Documentation

For further details on the implementation and examples, please refer to the comments within the code. The function is designed to be self-explanatory with inline comments explaining each step of the validation process.

This software is a simple yet effective tool for validating file names, ensuring they meet specific criteria for use in various applications.