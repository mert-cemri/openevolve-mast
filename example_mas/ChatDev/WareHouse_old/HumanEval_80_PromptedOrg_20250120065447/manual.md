# Happy String Checker

This software provides a function to determine if a given string is "happy". A string is considered "happy" if its length is at least 3 and every 3 consecutive letters are distinct.

## Main Function

### `is_happy(s)`

- **Description**: This function checks if the input string `s` is "happy".
- **Parameters**: 
  - `s` (str): The input string to be checked.
- **Returns**: 
  - `bool`: Returns `True` if the string is happy, otherwise `False`.

#### Examples

- `is_happy("a")` returns `False`
- `is_happy("aa")` returns `False`
- `is_happy("abcd")` returns `True`
- `is_happy("aabb")` returns `False`
- `is_happy("adb")` returns `True`
- `is_happy("xyy")` returns `False`

## Installation

This project does not require any external dependencies. However, ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can run the `main.py` file directly to test the `is_happy` function.

## Usage

To use the `is_happy` function, simply import it into your Python script and pass the string you want to check as an argument.

```python
from main import is_happy

# Example usage
result = is_happy("abcd")
print(result)  # Output: True
```

## Documentation

For further documentation and examples, please refer to the comments within the `main.py` file. The function is designed to be straightforward and easy to integrate into other projects.

## Support

For any issues or questions, please contact the development team at support@chatdev.com. We are here to assist you with any inquiries or problems you might encounter.