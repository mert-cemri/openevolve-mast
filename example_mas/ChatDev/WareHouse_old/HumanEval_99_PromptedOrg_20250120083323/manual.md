# Closest Integer Function

This software provides a simple Python function to find the closest integer to a given number, rounding away from zero when the number is equidistant from two integers. This function is useful for applications where precise rounding behavior is required, such as financial calculations or data processing tasks.

## Main Functionality

The main function provided by this software is `closest_integer(value)`. It takes a string input representing a number and returns the closest integer to that number. The rounding behavior is such that if the number is equidistant from two integers, it rounds away from zero.

### Example Usage

```python
print(closest_integer("10"))   # Output: 10
print(closest_integer("15.3")) # Output: 15
print(closest_integer("14.5")) # Output: 15
print(closest_integer("-14.5"))# Output: -15
```

## Installation

This software does not require any external dependencies, making it simple to integrate into your existing Python environment.

### Quick Install

Since there are no external dependencies, you can directly use the function in your Python environment. Simply copy the `closest_integer` function from the `main.py` file into your project.

## How to Use

1. **Copy the Function**: Copy the `closest_integer` function from the `main.py` file into your Python script or project.

2. **Call the Function**: Use the function by passing a string that represents a number. The function will return the closest integer, rounding away from zero if necessary.

3. **Example**: 
   ```python
   result = closest_integer("14.5")
   print(result)  # Output: 15
   ```

## Documentation

For further information on how the function works, refer to the comments within the `main.py` file. The function is designed to be straightforward and easy to use, with clear documentation provided in the code comments.

This software is ideal for developers who need precise control over rounding behavior in their applications. Enjoy using the `closest_integer` function to enhance your projects!