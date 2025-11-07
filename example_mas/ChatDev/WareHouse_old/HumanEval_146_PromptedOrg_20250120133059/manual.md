# SpecialFilter

A Python function to filter numbers based on specific criteria.

## Overview

The `specialFilter` function is designed to take an array of numbers as input and return the count of elements that satisfy the following conditions:
- The number is greater than 10.
- Both the first and last digits of the number are odd (1, 3, 5, 7, 9).

### Example Usage

```python
specialFilter([15, -73, 14, -15])  # Returns: 1
specialFilter([33, -2, -3, 45, 21, 109])  # Returns: 2
```

## Installation

This software does not require any external dependencies, making it simple to set up and use. You only need Python installed on your machine.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine. Otherwise, copy the `main.py` file to your working directory.

2. **Run the Function**: You can use the function by importing it into your Python script or running it directly in a Python environment.

### Example

```python
from main import specialFilter

# Define your list of numbers
numbers = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]

# Call the specialFilter function
result = specialFilter(numbers)

# Print the result
print(f"The count of numbers meeting the criteria is: {result}")
```

## Documentation

The `specialFilter` function is straightforward and does not require additional configuration or setup. It processes a list of integers and returns an integer representing the count of numbers meeting the specified criteria.

### Function Definition

```python
def specialFilter(nums):
    """
    Takes an array of numbers as input and returns the number of elements 
    that are greater than 10 and both first and last digits of a number are odd.
    """
```

- **Parameters**: 
  - `nums`: List of integers.

- **Returns**: 
  - Integer count of numbers that meet the criteria.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided within the code comments.