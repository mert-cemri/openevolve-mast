# Change Base Function

This software provides a simple utility function to convert a given integer from base 10 to another base, where the base is less than 10. This is useful for applications that require base conversions, such as computer science education, digital systems, and more.

## Main Functionality

The main function provided by this software is `change_base(x: int, base: int) -> str`. This function takes an integer `x` in base 10 and converts it to a string representation in the specified `base`.

### Function Signature

```python
def change_base(x: int, base: int) -> str:
```

### Parameters

- `x` (int): The integer number in base 10 that you want to convert.
- `base` (int): The base to which you want to convert the number. It must be between 2 and 9, inclusive.

### Returns

- `str`: The string representation of the number `x` in the specified base.

### Example Usage

```python
>>> change_base(8, 3)
'22'
>>> change_base(8, 2)
'1000'
>>> change_base(7, 2)
'111'
```

## Installation

This software does not require any external dependencies, so you can use it directly in your Python environment. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone or Download the Code**: Obtain the `main.py` file containing the `change_base` function.

2. **Run the Function**: You can use the function in your Python scripts or interactive environment by importing it from `main.py`.

3. **Example Script**: Create a Python script or use an interactive Python shell to test the function.

```python
from main import change_base

# Example usage
result = change_base(8, 3)
print(result)  # Output: '22'
```

## Notes

- The function raises a `ValueError` if the base is not between 2 and 9.
- The function handles the conversion process by repeatedly dividing the number by the base and collecting remainders, which are then reversed to form the final string representation.

This utility is designed to be simple and efficient for small base conversions, making it a handy tool for educational purposes and small-scale applications.