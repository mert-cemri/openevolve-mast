# Change Base Application

This application provides a simple utility to convert a number from base 10 to another base less than 10. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The core functionality of this application is encapsulated in the `change_base` function. This function takes an integer and a target base as input and returns the string representation of the number in the specified base.

### Function: `change_base(x: int, base: int) -> str`

- **Parameters:**
  - `x`: An integer representing the number in base 10 that you want to convert.
  - `base`: An integer representing the target base for conversion. The base must be between 2 and 9, inclusive.

- **Returns:**
  - A string representing the number `x` in the specified base.

- **Example Usage:**
  ```python
  change_base(8, 3)  # Returns '22'
  change_base(8, 2)  # Returns '1000'
  change_base(7, 2)  # Returns '111'
  ```

## Installation

Since this application does not require any external dependencies, setting up the environment is straightforward. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed:**
   - Make sure you have Python 3.x installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Clone the Repository:**
   - Clone the repository containing the `main.py` file to your local machine.

3. **Navigate to the Project Directory:**
   - Open a terminal and navigate to the directory where `main.py` is located.

## How to Use

1. **Open a Terminal:**
   - Navigate to the directory where `main.py` is located.

2. **Run Python Interpreter:**
   - Start the Python interpreter by typing `python` in the terminal.

3. **Import the Function:**
   - Import the `change_base` function from `main.py`:
     ```python
     from main import change_base
     ```

4. **Use the Function:**
   - Call the `change_base` function with the desired parameters:
     ```python
     result = change_base(8, 3)
     print(result)  # Output: '22'
     ```

5. **Exit the Interpreter:**
   - Type `exit()` to leave the Python interpreter.

## Conclusion

This application provides a simple and efficient way to convert numbers from base 10 to any base less than 10. It is easy to set up and use, requiring only basic Python knowledge. Enjoy using the Change Base Application!