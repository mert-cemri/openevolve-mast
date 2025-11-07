# Truncate Number Application

This application provides a simple function to truncate a floating point number and return its decimal part. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The main function of this application is `truncate_number`, which takes a positive floating point number as input and returns its decimal part. This function is useful for scenarios where you need to separate the integer part from the decimal part of a number.

### Function Definition

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
```

## Installation

### Environment Setup

Since this application does not require any external dependencies, setting up the environment is straightforward. You only need Python installed on your system.

### Installing Python

If you do not have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/). Follow the instructions for your operating system to install Python.

## Usage

To use the `truncate_number` function, follow these steps:

1. **Open a Python Environment:**
   - You can use any Python environment such as IDLE, PyCharm, VSCode, or simply the command line.

2. **Import the Function:**
   - If you have saved the function in a file named `main.py`, you can import it using:
     ```python
     from main import truncate_number
     ```

3. **Call the Function:**
   - Use the function by passing a positive floating point number as an argument:
     ```python
     result = truncate_number(3.5)
     print(result)  # Output: 0.5
     ```

## Example

Here's a quick example of how to use the `truncate_number` function:

```python
# Import the function
from main import truncate_number

# Define a number
number = 7.89

# Get the decimal part
decimal_part = truncate_number(number)

# Print the result
print(f"The decimal part of {number} is {decimal_part}.")
```

This will output:

```
The decimal part of 7.89 is 0.89.
```

## Conclusion

This application provides a simple yet effective way to extract the decimal part of a floating point number. With no external dependencies, it is easy to integrate into any Python project.