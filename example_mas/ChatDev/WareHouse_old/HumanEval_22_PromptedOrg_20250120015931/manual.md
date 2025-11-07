# Filter Integers

This software module provides a simple utility function to filter integers from a list of mixed data types in Python.

## Main Function

The main function provided by this module is `filter_integers`, which takes a list of any Python values and returns a list containing only the integer values.

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

This module does not require any external dependencies, so installation is straightforward. You only need Python installed on your system.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing `main.py`.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run a Python interactive shell or create a Python script to use the `filter_integers` function.

### Example in Python Interactive Shell

```bash
$ python
```

```python
>>> from main import filter_integers
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
```

### Example in a Python Script

Create a file named `example.py`:

```python
from main import filter_integers

result = filter_integers(['a', 3.14, 5])
print(result)  # Output: [5]

result = filter_integers([1, 2, 3, 'abc', {}, []])
print(result)  # Output: [1, 2, 3]
```

Run the script:

```bash
$ python example.py
```

## Documentation

This module is straightforward and does not require additional documentation beyond the examples provided. The function is designed to be intuitive and easy to integrate into larger projects where filtering integer values from a list is necessary.