# Happy String Checker

This software provides a simple function to determine whether a given string is "happy" based on specific criteria. A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.

## Main Function

### `is_happy(s)`

- **Description**: This function checks if a string `s` is happy. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct.
- **Parameters**: 
  - `s` (str): The string to be checked.
- **Returns**: 
  - `bool`: Returns `True` if the string is happy, otherwise `False`.

#### Examples:
- `is_happy('a')` => `False`
- `is_happy('aa')` => `False`
- `is_happy('abcd')` => `True`
- `is_happy('aabb')` => `False`
- `is_happy('adb')` => `True`
- `is_happy('xyy')` => `False`

## Installation

This software does not require any external packages. It is implemented purely in Python and can be run in any standard Python environment.

### Quick Install

1. **Ensure Python is installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

4. **Run the code**: You can directly run the `main.py` file to test the function:
   ```bash
   python main.py
   ```

## Usage

To use the `is_happy` function, you can import it into your Python script and pass a string to it. Here is a simple example:

```python
from main import is_happy

# Test the function with different strings
print(is_happy('abcd'))  # Output: True
print(is_happy('aabb'))  # Output: False
```

## Documentation

This software is straightforward and does not require extensive documentation. The function is self-contained and can be easily integrated into larger projects where string analysis is needed.

For any further questions or support, please contact the development team at ChatDev.