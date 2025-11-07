# Truncate Number

This software provides a simple function to extract the decimal part of a given positive floating-point number. It is designed to be straightforward and efficient, with no external dependencies required.

## Main Function

The main function of this software is `truncate_number`, which takes a positive floating-point number as input and returns the decimal part of that number.

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

### How It Works

- **Input:** A positive floating-point number.
- **Output:** The decimal part of the input number.

The function works by calculating the integer part of the number using the `int()` function, which truncates the decimal part. It then subtracts this integer part from the original number to isolate and return the decimal part.

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed:** You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository:** Obtain the `main.py` file containing the `truncate_number` function.

3. **Run the function:** You can use the function in your Python scripts by importing it from `main.py`.

## Usage

To use the `truncate_number` function, follow these steps:

1. **Import the function in your script:**

   ```python
   from main import truncate_number
   ```

2. **Call the function with a positive floating-point number:**

   ```python
   result = truncate_number(3.5)
   print(result)  # Output: 0.5
   ```

This function is useful in scenarios where you need to separate the decimal part of a number from its integer part, such as in financial calculations or data analysis tasks.

## Documentation

For further information and examples, refer to the inline documentation within the `main.py` file. The function includes a docstring that explains its purpose and provides an example of its usage.