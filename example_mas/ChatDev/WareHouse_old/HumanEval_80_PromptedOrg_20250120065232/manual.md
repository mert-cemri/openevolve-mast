# Happy String Checker

This software provides a function to determine if a given string is "happy." A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.

## Main Function

### `is_happy(s)`

- **Description**: This function checks if the input string `s` is happy.
- **Parameters**: 
  - `s` (str): The string to be checked.
- **Returns**: 
  - `bool`: Returns `True` if the string is happy, otherwise returns `False`.

#### Examples:
- `is_happy("a")` => `False`
- `is_happy("aa")` => `False`
- `is_happy("abcd")` => `True`
- `is_happy("aabb")` => `False`
- `is_happy("adb")` => `True`
- `is_happy("xyy")` => `False`

## Installation

This software is implemented in Python. To use it, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Quick Install

There are no additional dependencies required for this software. Simply clone the repository or download the `main.py` file to your local machine.

## Usage

1. **Clone the Repository**: 
   - Use `git clone <repository-url>` to clone the repository to your local machine.
   
2. **Navigate to the Directory**:
   - Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Function**:
   - Open a Python interpreter or create a new Python script.
   - Import the `is_happy` function from `main.py`.
   - Call the function with your desired string input.

Example:
```python
from main import is_happy

print(is_happy("abcd"))  # Output: True
print(is_happy("aabb"))  # Output: False
```

## Documentation

For further details on how the function works, refer to the docstring provided within the `main.py` file. The docstring includes a description of the function, its parameters, return values, and example usage.

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to help you with any queries related to the Happy String Checker software.