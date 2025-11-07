# any_int Function User Manual

## Introduction

The `any_int` function is a simple utility designed to evaluate three numbers and determine if one of them is equal to the sum of the other two, provided all numbers are integers. This function is useful in scenarios where you need to validate the relationship between three integer values.

## Main Functionality

- **Function Name:** `any_int`
- **Parameters:** 
  - `x`: First number (expected to be an integer)
  - `y`: Second number (expected to be an integer)
  - `z`: Third number (expected to be an integer)
- **Returns:** 
  - `True` if one of the numbers is equal to the sum of the other two and all numbers are integers.
  - `False` in any other cases, including when any of the numbers is not an integer.

### Examples

- `any_int(5, 2, 7)` ➞ `True` (because 5 + 2 = 7)
- `any_int(3, 2, 2)` ➞ `False` (no number is the sum of the other two)
- `any_int(3, -2, 1)` ➞ `True` (because 3 + (-2) = 1)
- `any_int(3.6, -2.2, 2)` ➞ `False` (because not all numbers are integers)

## Installation

This function does not require any external dependencies, making it easy to integrate into your existing Python projects. Simply copy the function code into your Python script or module.

## How to Use

1. **Copy the Function Code:**

   Copy the following code into your Python script:

   ```python
   def any_int(x, y, z):
       # Check if all inputs are integers
       if not all(isinstance(i, int) for i in (x, y, z)):
           return False
       # Check if any one of the numbers is equal to the sum of the other two
       return x == y + z or y == x + z or z == x + y
   ```

2. **Call the Function:**

   Use the function by passing three numbers as arguments. For example:

   ```python
   result = any_int(5, 2, 7)
   print(result)  # Output: True
   ```

3. **Interpret the Result:**

   - If the function returns `True`, it means one of the numbers is the sum of the other two, and all numbers are integers.
   - If the function returns `False`, it means either the condition is not met or one or more numbers are not integers.

## Conclusion

The `any_int` function is a straightforward tool for validating the relationship between three integer values. It is easy to use, requires no additional libraries, and can be seamlessly integrated into any Python project.