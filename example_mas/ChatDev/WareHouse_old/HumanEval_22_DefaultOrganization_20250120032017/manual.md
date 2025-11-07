```markdown
# Filter Integers Application

This application provides a simple utility function to filter integers from a list of mixed data types in Python. It is designed to be lightweight and requires no external dependencies.

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
```

### Usage Examples

- `filter_integers(['a', 3.14, 5])` will return `[5]`.
- `filter_integers([1, 2, 3, 'abc', {}, []])` will return `[1, 2, 3]`.

## Installation

This application does not require any external packages, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the repository to your local machine.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.

## How to Use

1. **Open the Terminal**: Open your command line interface.
2. **Run the Python Script**: Execute the script using Python by running the following command:
   ```bash
   python main.py
   ```
3. **Use the Function**: You can modify the `main.py` file to include test cases or use the function in your own scripts by importing it.

## Documentation

For further details on how to use the function or integrate it into larger projects, refer to the inline documentation provided in the `main.py` file. The function is designed to be intuitive and easy to integrate into any Python project requiring integer filtering from mixed-type lists.

```