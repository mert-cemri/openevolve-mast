# Truncate Number

This software module provides a simple function to truncate a floating-point number and return its decimal part. It is designed to be lightweight and efficient, with no external dependencies required.

## Quick Install

No installation of external dependencies is required for this module. It is implemented purely in Python and can be used directly.

## 🤔 What is this?

The `truncate_number` function is a utility that takes a positive floating-point number as input and returns the decimal part of that number. This can be useful in various applications where you need to separate the integer and decimal parts of a number.

### Main Function

- **truncate_number(number: float) -> float**: This function takes a positive floating-point number and returns the decimal part of the number. For example, given the input `3.5`, it will return `0.5`.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `truncate_number` function.

2. **Import the Function**: In your Python script, import the `truncate_number` function from the `main.py` file.

   ```python
   from main import truncate_number
   ```

3. **Use the Function**: Call the `truncate_number` function with a positive floating-point number as an argument.

   ```python
   result = truncate_number(3.5)
   print(result)  # Output: 0.5
   ```

## Example

Here is a simple example of how to use the `truncate_number` function:

```python
# Import the function
from main import truncate_number

# Example usage
number = 7.89
decimal_part = truncate_number(number)
print(f"The decimal part of {number} is {decimal_part}")
```

This will output:

```
The decimal part of 7.89 is 0.89
```

## Documentation

The function is straightforward and does not require additional documentation. The code is self-explanatory, and the function is designed to be used in any Python environment without additional setup.

Feel free to integrate this function into your projects where you need to handle floating-point numbers and extract their decimal parts.