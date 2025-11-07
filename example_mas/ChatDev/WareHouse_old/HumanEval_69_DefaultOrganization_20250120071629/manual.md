manual.md

```
# Search Function Software

This software provides a function to find the greatest integer in a list that has a frequency greater than or equal to its value. It is designed to be simple and efficient, requiring no external dependencies.

## Main Functionality

The main functionality of this software is encapsulated in the `search` function. This function takes a non-empty list of positive integers as input and returns the greatest integer that meets the specified frequency condition. If no such integer exists, it returns -1.

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

No external dependencies are required for this software. It is implemented in Python and can be run in any standard Python environment.

### Quick Setup

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing the `main.py` file.

4. Run the Python script using the command:
   ```bash
   python main.py
   ```

## Usage

To use the `search` function, you can import it into your Python script or interactive session. Here is an example of how to use it:

```python
from main import search

# Example list
lst = [4, 1, 2, 2, 3, 1]

# Call the search function
result = search(lst)

# Print the result
print("The greatest integer with the required frequency is:", result)
```

## Documentation

For further details on how the function works, please refer to the comments within the `main.py` file. The function is designed to be self-explanatory with inline comments explaining each step of the process.

## Support

If you encounter any issues or have questions about the software, please contact our support team at support@chatdev.com.

```