# Even Odd Count

A simple Python function to count the number of even and odd digits in an integer.

## Overview

The `even_odd_count` function takes an integer as input and returns a tuple containing the count of even and odd digits in the number. This function handles both positive and negative integers.

### Example Usage

- `even_odd_count(-12)` returns `(1, 1)`
- `even_odd_count(123)` returns `(1, 2)`

## Installation

This software does not require any external dependencies. It is implemented in pure Python, and you can run it in any standard Python environment.

### Requirements

- Python 3.x

## How to Use

1. **Clone or Download the Repository:**

   You can clone the repository using Git or download the files directly.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change your working directory to where the `main.py` file is located.

   ```bash
   cd <directory-path>
   ```

3. **Run the Function:**

   You can use the function in a Python script or an interactive Python session. Here is an example of how to use it:

   ```python
   from main import even_odd_count

   # Example usage
   result = even_odd_count(-12)
   print(result)  # Output: (1, 1)

   result = even_odd_count(123)
   print(result)  # Output: (1, 2)
   ```

## Documentation

The function is straightforward and does not require additional configuration. It processes the input integer by converting it to a string, iterating over each digit, and counting how many are even and how many are odd.

### Function Definition

```python
def even_odd_count(num):
    """
    Given an integer, return a tuple that has the number of even and odd digits respectively.

    Parameters:
    num (int): The integer to be processed.

    Returns:
    tuple: A tuple containing two integers, the first is the count of even digits, and the second is the count of odd digits.
    """
```

## Support

For any issues or questions, please contact our support team at support@chatdev.com. We are here to help you with any problems you may encounter while using the software.