# Filter Integers

This software module provides a simple function to filter integers from a list of various Python values. It is designed to be straightforward and efficient, allowing users to easily extract integer values from mixed-type lists.

## Main Function

The main function provided by this module is `filter_integers`.

### `filter_integers(values: List[Any]) -> List[int]`

- **Description**: This function takes a list of any Python values and returns a new list containing only the integer values from the original list.
- **Parameters**: 
  - `values`: A list containing elements of any data type.
- **Returns**: A list containing only the integer elements from the input list.

#### Example Usage

```python
from main import filter_integers

# Example 1
result1 = filter_integers(['a', 3.14, 5])
print(result1)  # Output: [5]

# Example 2
result2 = filter_integers([1, 2, 3, 'abc', {}, []])
print(result2)  # Output: [1, 2, 3]
```

## Installation

This module does not require any external dependencies, making it easy to integrate into any Python project.

### Quick Install

Since there are no external dependencies, you can directly use the module by including the `main.py` file in your project.

## How to Use

1. **Include the Module**: Ensure that the `main.py` file is in your project directory.
2. **Import the Function**: Use the `from main import filter_integers` statement to import the function into your script.
3. **Call the Function**: Pass a list of mixed-type values to the `filter_integers` function to obtain a list of integers.

## Documentation

This module is designed to be simple and self-explanatory. The function is documented with a docstring that includes usage examples. For further assistance, refer to the example usage section above.

Feel free to integrate this module into your projects where filtering integers from a list is required. It is a lightweight and efficient solution for handling such tasks.