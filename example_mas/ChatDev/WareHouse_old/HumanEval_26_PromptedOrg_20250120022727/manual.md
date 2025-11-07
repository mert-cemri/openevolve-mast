manual.md

```
# Remove Duplicates Software

This software provides a simple utility function to remove duplicate elements from a list of integers, keeping only the elements that appear once and maintaining their original order.

## Main Functionality

The main function provided by this software is `remove_duplicates`, which takes a list of integers as input and returns a new list with all elements that occur more than once removed. The order of the remaining elements is preserved as in the input list.

### Function Signature

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
```

### Example Usage

```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```

In this example, the number `2` appears more than once in the input list, so it is removed from the output list.

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need to have Python installed on your system.

### Prerequisites

- Python 3.x

### Installation Steps

1. Ensure Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Clone or download the repository containing the `main.py` file.

3. Navigate to the directory containing the `main.py` file.

## How to Use

1. Open a terminal or command prompt.

2. Navigate to the directory where `main.py` is located.

3. Run a Python interactive shell or create a Python script to use the `remove_duplicates` function.

### Example in Python Interactive Shell

```bash
$ python
```

```python
>>> from main import remove_duplicates
>>> result = remove_duplicates([1, 2, 3, 2, 4])
>>> print(result)
[1, 3, 4]
```

### Example in a Python Script

Create a file named `example.py` and add the following code:

```python
from main import remove_duplicates

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```

Run the script:

```bash
$ python example.py
```

This will output:

```
[1, 3, 4]
```

## Conclusion

This software provides a simple and efficient way to remove duplicate integers from a list while preserving the order of unique elements. It is easy to integrate into any Python project without the need for additional dependencies.
```