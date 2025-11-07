# Sort Array User Manual

Welcome to the Sort Array software! This tool is designed to sort arrays of integers based on specific criteria, providing a simple yet effective solution for organizing your data.

## Main Functions

The primary function of this software is `sort_array`, which sorts an array of integers according to the following rules:

1. **Non-negative Integers**: These are sorted based on the number of ones in their binary representation. If two numbers have the same number of ones, they are further sorted by their decimal value.

2. **Negative Integers**: These are sorted solely by their decimal value.

### Function Signature

```python
def sort_array(arr):
    """
    Sort an array of integers based on the number of ones in their binary representation for non-negative numbers.
    For numbers with the same number of ones, sort by decimal value.
    Negative numbers should be sorted by their decimal value.
    Args:
    arr (list of int): The list of integers to sort.
    Returns:
    list of int: The sorted list of integers.
    """
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Python Installation**: Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the source code repository, clone it to your local machine.

3. **Run the Code**: Navigate to the directory containing `main.py` and execute it using Python.

```bash
python main.py
```

## How to Use

To use the `sort_array` function, follow these steps:

1. **Import the Function**: If you are using this in a larger project, import the function from `main.py`.

```python
from main import sort_array
```

2. **Call the Function**: Pass a list of integers to the `sort_array` function.

```python
result = sort_array([1, 5, 2, 3, 4])
print(result)  # Output: [1, 2, 3, 4, 5]
```

3. **Interpret the Results**: The function will return a new list of integers sorted according to the specified rules.

### Examples

- Sorting a mix of non-negative integers:

```python
print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
```

- Sorting negative integers:

```python
print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
```

- Sorting a list with zero:

```python
print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
```

## Conclusion

The Sort Array software provides a simple yet powerful way to sort arrays of integers based on binary representation and decimal value. With no external dependencies, it is easy to integrate into your projects. Enjoy using the software, and feel free to reach out for support if needed!