# Any_Int Function User Manual

## Introduction

The `any_int` function is a simple Python utility designed to evaluate three numbers and determine if one of them is equal to the sum of the other two, provided all numbers are integers. This function is useful in scenarios where you need to validate arithmetic relationships between integers.

## Main Functionality

- **Function Name**: `any_int`
- **Purpose**: To check if one of the three input numbers is equal to the sum of the other two, and ensure all numbers are integers.
- **Returns**: 
  - `True` if one of the numbers is equal to the sum of the other two and all numbers are integers.
  - `False` in any other cases.

### Examples

- `any_int(5, 2, 7)` ➞ `True` (because 5 + 2 = 7)
- `any_int(3, 2, 2)` ➞ `False` (no number is the sum of the other two)
- `any_int(3, -2, 1)` ➞ `True` (because 3 + (-2) = 1)
- `any_int(3.6, -2.2, 2)` ➞ `False` (because not all numbers are integers)

## Installation

The `any_int` function does not require any external dependencies beyond Python itself. Therefore, there is no need to install additional packages. Ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Verify Installation**: Open a terminal or command prompt and run:
   ```bash
   python --version
   ```
   This should display the installed Python version.

## Usage

To use the `any_int` function, follow these steps:

1. **Create a Python File**: Create a new Python file, e.g., `main.py`.

2. **Copy the Function Code**: Copy the following code into your `main.py` file:

   ```python
   def any_int(x, y, z):
       # Check if all inputs are integers
       if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
           # Check if one number is the sum of the other two
           if x == y + z or y == x + z or z == x + y:
               return True
       return False
   ```

3. **Call the Function**: You can call the function with different sets of numbers to check the condition. For example:

   ```python
   print(any_int(5, 2, 7))  # Output: True
   print(any_int(3, 2, 2))  # Output: False
   ```

4. **Run the Script**: Execute the script by running the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

## Conclusion

The `any_int` function is a straightforward utility for checking arithmetic relationships between integers. It is easy to integrate into any Python project that requires such functionality. Since it has no external dependencies, it is lightweight and easy to use.