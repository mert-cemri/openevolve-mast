# Closest Integer Function

This software provides a simple function to determine the closest integer to a given number represented as a string. The function handles rounding away from zero when the number is equidistant from two integers.

## Main Functionality

The primary function of this software is:

- **closest_integer(value):** This function takes a string input representing a number and returns the closest integer. If the number is equidistant from two integers, it rounds away from zero.

### Examples

```python
>>> closest_integer("10")
10
>>> closest_integer("15.3")
15
>>> closest_integer("14.5")
15
>>> closest_integer("-14.5")
-15
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

To use the function, simply include the `main.py` file in your project and import the `closest_integer` function.

## Usage

1. **Import the Function:**

   To use the `closest_integer` function, you need to import it from the `main.py` file.

   ```python
   from main import closest_integer
   ```

2. **Call the Function:**

   Pass a string representing a number to the function to get the closest integer.

   ```python
   result = closest_integer("15.3")
   print(result)  # Output: 15
   ```

3. **Handling Edge Cases:**

   The function correctly handles rounding away from zero for numbers equidistant from two integers.

   ```python
   print(closest_integer("14.5"))  # Output: 15
   print(closest_integer("-14.5")) # Output: -15
   ```

## Documentation

For further details and examples, please refer to the comments within the `main.py` file. The function is straightforward and designed to be easy to integrate into larger projects where rounding behavior is crucial.

Feel free to modify and extend the function to suit your specific needs. If you encounter any issues or have questions, please contact our support team for assistance.