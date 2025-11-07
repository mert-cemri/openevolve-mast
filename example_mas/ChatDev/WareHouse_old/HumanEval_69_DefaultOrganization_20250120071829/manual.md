manual.md

```
# Search Function Software

This software provides a function to find the greatest integer in a list of positive integers that meets specific frequency criteria. The function is designed to be simple and efficient, requiring no external dependencies.

## Main Functionality

The core functionality of this software is encapsulated in the `search` function. This function takes a list of positive integers as input and returns the greatest integer that is greater than zero and has a frequency greater than or equal to the value of the integer itself. If no such integer exists, the function returns -1.

### Function Definition

```python
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    '''
```

### Examples

- `search([4, 1, 2, 2, 3, 1])` returns `2`
- `search([1, 2, 2, 3, 3, 3, 4, 4, 4])` returns `3`
- `search([5, 5, 4, 4, 4])` returns `-1`

## Installation

This software does not require any external dependencies, making it easy to integrate into your existing Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

3. **Run the Function**: You can use the function by importing it into your Python script or interactive shell. Here’s an example of how to use it:

```python
from main import search

# Example usage
result = search([4, 1, 2, 2, 3, 1])
print(result)  # Output: 2
```

4. **Modify the Input**: You can test the function with different lists of positive integers to see how it behaves with various inputs.

## Documentation

For further details on the function and its implementation, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the function.

## Support

If you encounter any issues or have questions about using this software, please feel free to reach out to our support team at support@chatdev.com.

```