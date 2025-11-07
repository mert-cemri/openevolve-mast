manual.md

```
# Happy String Checker

This software provides a simple utility function to check if a given string is "happy". A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.

## Main Functionality

The main functionality of this software is encapsulated in the `is_happy` function. This function takes a string as input and returns a boolean value indicating whether the string is happy or not.

### Function: `is_happy(s)`

- **Description**: Checks if the input string `s` is happy.
- **Parameters**: 
  - `s` (str): The input string to check.
- **Returns**: 
  - `bool`: `True` if the string is happy, `False` otherwise.

### Examples

- `is_happy("a")` returns `False`
- `is_happy("aa")` returns `False`
- `is_happy("abcd")` returns `True`
- `is_happy("aabb")` returns `False`
- `is_happy("adb")` returns `True`
- `is_happy("xyy")` returns `False`

## Installation

This project does not require any external dependencies, so no installation of additional packages is necessary. You only need Python installed on your machine.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can run the function in a Python environment or script by importing the `is_happy` function from `main.py`.

   ```python
   from main import is_happy

   print(is_happy("abcd"))  # Example usage
   ```

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is well-documented to provide clarity on its usage and behavior.

## Support

If you encounter any issues or have questions, please contact our support team at support@chatdev.com.

```