# Filter Integers

This software module provides a simple function to filter integers from a list of various Python values. It is designed to be lightweight and requires no external dependencies.

## Main Functionality

The primary function of this module is `filter_integers`, which takes a list of any Python values and returns a new list containing only the integer values from the original list.

### Function Signature

```python
def filter_integers(values: List[Any]) -> List[int]:
```

### Example Usage

```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
```

## Installation

Since this module does not require any external dependencies, you can use it directly in your Python environment without any additional installation steps.

### Quick Start

1. **Download the `main.py` file**: Ensure you have the `main.py` file containing the `filter_integers` function.

2. **Run Python**: You can use this function in any Python environment. Simply import the function and use it as demonstrated in the example usage.

## How to Use

1. **Import the Function**: First, ensure that the `main.py` file is in your working directory. Then, import the function into your Python script or interactive session.

    ```python
    from main import filter_integers
    ```

2. **Call the Function**: Pass a list of mixed Python values to the `filter_integers` function to get a list of integers.

    ```python
    integers = filter_integers(['a', 3.14, 5, 7, 'hello', 10])
    print(integers)  # Output: [5, 7, 10]
    ```

## Additional Information

- **No External Libraries**: This module is designed to be simple and does not require any external libraries or packages.

- **Python Compatibility**: The function is compatible with Python 3.x versions.

Feel free to use and integrate this function into your projects where filtering integers from a list is needed. If you have any questions or need further assistance, please contact our support team.