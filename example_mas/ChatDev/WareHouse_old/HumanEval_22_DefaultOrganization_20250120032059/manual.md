# Filter Integers User Manual

Welcome to the Filter Integers software! This software provides a simple and efficient way to filter integer values from a list containing various types of Python values. This manual will guide you through the installation process, introduce the main function of the software, and demonstrate how to use it effectively.

## Main Functionality

The primary function of this software is `filter_integers`, which takes a list of any Python values and returns a new list containing only the integer values. This function is useful when you need to extract integer data from a mixed list of values.

### Function Definition

```python
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from the official website: [python.org](https://www.python.org/).

2. **Clone or download the repository**: Obtain the `main.py` file containing the `filter_integers` function.

3. **No additional dependencies**: There are no additional packages to install, as the software relies solely on Python's standard library.

## How to Use

1. **Prepare your list**: Create a list of values that may include integers, strings, floats, dictionaries, lists, etc.

2. **Call the function**: Use the `filter_integers` function to filter out only the integer values from your list.

### Example Usage

```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]

# Example usage
example_list = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
filtered_integers = filter_integers(example_list)
print(filtered_integers)  # Output: [5, 1, 2, 3]
```

## Conclusion

The Filter Integers software is a straightforward tool designed to help you extract integer values from mixed-type lists. With no external dependencies, it is easy to integrate into your existing Python projects. We hope this manual has provided you with the necessary information to install and use the software effectively. If you have any questions or need further assistance, please feel free to reach out.