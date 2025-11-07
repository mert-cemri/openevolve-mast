# Filter Integers Software

This software provides a simple utility function to filter integers from a list containing various types of Python values. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this software is encapsulated in the `filter_integers` function. This function takes a list of any Python values and returns a new list containing only the integer values from the original list.

### Function Definition

```python
def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]
```

### Example Usage

- Input: `['a', 3.14, 5]`
- Output: `[5]`

- Input: `[1, 2, 3, 'abc', {}, []]`
- Output: `[1, 2, 3]`

## Installation

This software does not require any external dependencies, making it straightforward to use. Simply ensure you have Python installed on your system.

### Installing Python

If you do not have Python installed, you can download it from the official [Python website](https://www.python.org/downloads/). Follow the installation instructions provided for your operating system.

## How to Use

1. **Clone or Download the Repository**: Obtain the `main.py` file containing the `filter_integers` function.

2. **Run the Function**: You can use the function directly in your Python scripts or interactive environment.

   ```python
   from main import filter_integers

   # Example usage
   result = filter_integers(['a', 3.14, 5])
   print(result)  # Output: [5]
   ```

3. **Testing**: You can test the function using the provided examples in the function's docstring. Simply run the examples in a Python environment to verify the functionality.

## Documentation

This software is designed to be simple and self-explanatory. The function is documented with examples to demonstrate its usage. For any further questions or support, please refer to the comments and docstrings within the code.

## Support

For any issues or questions regarding the use of this software, please contact the development team at ChatDev. We are committed to providing support and ensuring the software meets your needs.