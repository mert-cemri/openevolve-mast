# Bracket Nesting Checker

This software provides a function to check if a given string of square brackets contains a valid subsequence where at least one bracket is nested. It is a simple utility that can be used to validate bracket sequences in strings.

## Main Functionality

The main function provided by this software is `is_nested(string)`. This function takes a string as input, which contains only square brackets (`[` and `]`), and returns a boolean value:

- `True` if there is a valid subsequence of brackets where at least one bracket is nested.
- `False` otherwise.

### Example Usage

```python
print(is_nested('[[]]'))        # Output: True
print(is_nested('[]]]]]]][[[[[]'))  # Output: False
print(is_nested('[][]'))        # Output: False
print(is_nested('[]'))          # Output: False
print(is_nested('[[][]]'))      # Output: True
print(is_nested('[[]][['))      # Output: True
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/).

No additional packages are required, so there is no need to install anything via `pip` or `conda`.

## How to Use

1. **Clone or Download the Repository:**

   You can clone the repository using Git or download the ZIP file and extract it to your desired location.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

   ```bash
   cd path/to/directory
   ```

3. **Run the Script:**

   You can run the script using Python to test the `is_nested` function with different inputs.

   ```bash
   python main.py
   ```

   Alternatively, you can import the `is_nested` function into another Python script and use it as needed.

4. **Modify and Extend:**

   Feel free to modify the `main.py` file to test additional cases or integrate the function into larger projects.

## Documentation

This software is straightforward and does not require extensive documentation. The function `is_nested` is designed to be intuitive and easy to use. For any further questions or support, please refer to the comments within the code for guidance on its logic and implementation.