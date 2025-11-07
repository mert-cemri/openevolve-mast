# Total Match User Manual

Welcome to the Total Match software! This application provides a simple function to compare two lists of strings and determine which list has fewer total characters. This manual will guide you through the installation process, introduce the main function of the software, and provide instructions on how to use it.

## Main Functionality

The primary function of this software is `total_match`, which compares two lists of strings and returns the list with the fewer total number of characters. If both lists have the same number of characters, the function will return the first list.

### Function Definition

```python
def total_match(lst1, lst2):
    '''
    Compare two lists of strings and return the list with fewer total characters.
    If both lists have the same number of characters, return the first list.
    
    Parameters:
    lst1 (list of str): First list of strings.
    lst2 (list of str): Second list of strings.
    
    Returns:
    list of str: The list with fewer total characters or the first list if they are equal.
    '''
```

### Examples

- `total_match([], [])` ➞ `[]`
- `total_match(['hi', 'admin'], ['hI', 'Hi'])` ➞ `['hI', 'Hi']`
- `total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])` ➞ `['hi', 'admin']`
- `total_match(['hi', 'admin'], ['hI', 'hi', 'hi'])` ➞ `['hI', 'hi', 'hi']`
- `total_match(['4'], ['1', '2', '3', '4', '5'])` ➞ `['4']`

## Installation

To use the Total Match software, you need to have Python installed on your system. The software does not require any additional dependencies, so there is no need for a `requirements.txt` file.

### Quick Install

1. **Ensure Python is installed**: You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `total_match` function.

## How to Use

1. **Open your Python environment**: You can use any Python IDE or a simple text editor with command line access.

2. **Import the function**: Ensure that the `main.py` file is in your working directory or adjust the import path accordingly.

3. **Call the function**: Use the `total_match` function by passing two lists of strings as arguments.

```python
from main import total_match

# Example usage
result = total_match(['hi', 'admin'], ['hI', 'Hi'])
print(result)  # Output: ['hI', 'Hi']
```

## Conclusion

The Total Match software is a straightforward tool for comparing lists of strings based on their total character count. With no additional dependencies required, it is easy to set up and use. We hope this manual helps you get started quickly and effectively. If you have any questions or need further assistance, please feel free to reach out.