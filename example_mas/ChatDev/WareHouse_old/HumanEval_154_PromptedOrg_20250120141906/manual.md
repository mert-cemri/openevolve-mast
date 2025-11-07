# CycPattern Check

This software provides a function to check if any rotation of a given second word is a substring of a first word. It is implemented in Python and does not require any external dependencies.

## Main Function

### `cycpattern_check(a, b)`

- **Description**: This function takes two words as input and returns `True` if any rotation of the second word is a substring of the first word. Otherwise, it returns `False`.

- **Parameters**:
  - `a` (str): The first word in which to check for the substring.
  - `b` (str): The second word whose rotations are checked as substrings in the first word.

- **Returns**: `bool` - `True` if any rotation of `b` is a substring of `a`, otherwise `False`.

- **Examples**:
  - `cycpattern_check("abcd", "abd")` returns `False`
  - `cycpattern_check("hello", "ell")` returns `True`
  - `cycpattern_check("whassup", "psus")` returns `False`
  - `cycpattern_check("abab", "baa")` returns `True`
  - `cycpattern_check("efef", "eeff")` returns `False`
  - `cycpattern_check("himenss", "simen")` returns `True`

## Installation

This software does not require any external dependencies. You only need Python installed on your system to run the function.

## Usage

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can use the function by importing it into your Python script or by running it directly in a Python interactive shell.

   ```python
   from main import cycpattern_check

   result = cycpattern_check("hello", "ell")
   print(result)  # Output: True
   ```

## Documentation

For further details on how the function works, please refer to the comments within the `main.py` file. The function is straightforward and does not require additional configuration or setup.

## Support

If you encounter any issues or have questions regarding the usage of this software, please contact our support team for assistance.