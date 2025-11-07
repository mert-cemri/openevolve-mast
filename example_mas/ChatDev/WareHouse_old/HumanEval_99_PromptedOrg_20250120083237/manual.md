# Closest Integer Function

This software provides a Python function to determine the closest integer to a given number represented as a string. The function rounds away from zero when the number is equidistant from two integers.

## Main Functionality

The main function of this software is `closest_integer(value)`, which:

- Takes a string input representing a number.
- Converts the string to a float.
- Returns the closest integer to the given number.
- Rounds away from zero if the number is equidistant from two integers.

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

This software does not require any external dependencies. You only need Python installed on your system to use this function.

### Quick Install

Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository or Download the Script**

   You can clone the repository or simply download the `main.py` file containing the function.

2. **Run the Script**

   You can run the script in a Python environment. Open a terminal or command prompt and navigate to the directory containing `main.py`. Then, run the Python interpreter:

   ```bash
   python
   ```

3. **Import and Use the Function**

   Import the function from the script and use it with your desired input:

   ```python
   from main import closest_integer

   print(closest_integer("10"))   # Output: 10
   print(closest_integer("15.3")) # Output: 15
   print(closest_integer("14.5")) # Output: 15
   print(closest_integer("-14.5"))# Output: -15
   ```

## Documentation

For further details on Python usage and syntax, refer to the [official Python documentation](https://docs.python.org/3/).

This software is designed to be simple and efficient, providing a straightforward solution to rounding numbers represented as strings to the nearest integer, with a specific rounding rule for equidistant cases.