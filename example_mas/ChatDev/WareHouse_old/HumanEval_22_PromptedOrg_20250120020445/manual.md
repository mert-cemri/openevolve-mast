# Filter Integers Software

This software provides a simple utility function to filter integers from a list of various Python values. It is designed to be lightweight and requires no external dependencies.

## Main Function

The core functionality of this software is encapsulated in the `filter_integers` function. This function takes a list of any Python values and returns a new list containing only the integer values from the original list.

### Function Definition

```python
def filter_integers(values: List[Any]) -> List[int]:
    """ 
    Filter given list of any python values only for integers.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]
```

### Usage Examples

- `filter_integers(['a', 3.14, 5])` will return `[5]`
- `filter_integers([1, 2, 3, 'abc', {}, []])` will return `[1, 2, 3]`

## Installation

This software does not require any external dependencies, making it easy to integrate into any Python project. Simply include the `main.py` file in your project directory.

### Requirements

There are no external dependencies required for this software. The `requirements.txt` file is provided for completeness but is empty.

## How to Use

1. **Include the `main.py` file in your project directory.**

2. **Import the function in your Python script:**

   ```python
   from main import filter_integers
   ```

3. **Call the `filter_integers` function with a list of values:**

   ```python
   result = filter_integers(['a', 3.14, 5])
   print(result)  # Output: [5]
   ```

4. **Run your script to see the filtered list of integers.**

This software is designed to be straightforward and efficient, providing a quick solution for filtering integers from a list of mixed data types.