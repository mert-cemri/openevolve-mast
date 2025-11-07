# Happy String Checker

This software provides a function to determine if a given string is "happy." A string is considered happy if its length is at least 3 and every 3 consecutive letters are distinct.

## Main Functionality

The main function provided by this software is `is_happy(s)`, which checks if a string `s` is happy according to the defined criteria.

### Function: `is_happy(s)`

- **Input**: A string `s`.
- **Output**: Returns `True` if the string is happy, otherwise returns `False`.

#### Examples:

- `is_happy("a")` => `False`
- `is_happy("aa")` => `False`
- `is_happy("abcd")` => `True`
- `is_happy("aabb")` => `False`
- `is_happy("adb")` => `True`
- `is_happy("xyy")` => `False`

## Installation

This software does not require any external dependencies. It is implemented in Python and can be run in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can use the function in a Python script or an interactive Python session.

   Example usage in a Python script:
   ```python
   from main import is_happy

   result = is_happy("abcd")
   print(result)  # Output: True
   ```

4. **Testing**: You can test the function with different strings to check if they are happy.

## Documentation

For further information and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed to be easily integrated into other Python projects.

Feel free to modify and extend the function to suit your specific needs.