# Increment List Function

This software provides a simple function to increment each element of a list by 1. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Function

The main function of this software is `incr_list`, which takes a list of integers as input and returns a new list with each element incremented by 1.

### Function Signature

```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1."""
```

### Example Usage

```python
>>> incr_list([1, 2, 3])
[2, 3, 4]
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Script**: You can run the script directly using Python.

```bash
python main.py
```

## How to Use

1. **Import the Function**: Import the `incr_list` function from the `main.py` file into your Python script or interactive session.

```python
from main import incr_list
```

2. **Call the Function**: Pass a list of integers to the `incr_list` function to get a new list with each element incremented by 1.

```python
result = incr_list([1, 2, 3])
print(result)  # Output: [2, 3, 4]
```

## Documentation

For further details on how to use the function, refer to the docstring provided within the `main.py` file. The docstring includes example usage and expected output.

This software is designed to be simple and straightforward, making it easy to integrate into larger projects or use as a standalone utility.