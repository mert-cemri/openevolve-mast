# Truncate Number

This software provides a simple utility function to extract the decimal part of a given positive floating-point number. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this software is `truncate_number`, which takes a positive floating-point number as input and returns its decimal part. This can be useful in various applications where you need to separate the integer and decimal parts of a number.

### Function Definition

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
```

## Installation

### Environment Setup

Since this software does not require any external dependencies, setting up the environment is straightforward. You only need to have Python installed on your system.

1. **Install Python**: If you haven't already, download and install Python from the official [Python website](https://www.python.org/downloads/).

2. **Verify Installation**: Open a terminal or command prompt and run the following command to verify that Python is installed correctly:
   ```bash
   python --version
   ```

3. **Clone the Repository**: If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

4. **Navigate to the Project Directory**: Change your directory to where the `main.py` file is located:
   ```bash
   cd <project-directory>
   ```

## Usage

To use the `truncate_number` function, follow these steps:

1. **Open a Python Interpreter**: You can use the terminal or any Python IDE of your choice.

2. **Import the Function**: If you are using the function in a different script, make sure to import it:
   ```python
   from main import truncate_number
   ```

3. **Call the Function**: Pass a positive floating-point number to the function to get the decimal part:
   ```python
   result = truncate_number(3.5)
   print(result)  # Output: 0.5
   ```

## Example

Here's a quick example of how to use the `truncate_number` function:

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

## Conclusion

This software provides a simple yet effective way to extract the decimal part of a floating-point number. With no external dependencies, it is easy to integrate into any Python project. Enjoy using the `truncate_number` function in your applications!