manual.md

```
# Check Dict Case

A simple Python utility to check the case consistency of dictionary keys.

## Overview

The `check_dict_case` function is designed to evaluate a dictionary and determine if all its keys are either in lowercase or uppercase. It returns `True` if all keys are consistently in one case, and `False` otherwise. Additionally, it returns `False` if the dictionary is empty or if any key is not a string.

## Main Function

### check_dict_case

- **Purpose**: To check if all keys in a dictionary are either all lowercase or all uppercase strings.
- **Parameters**: 
  - `d` (dict): The dictionary to evaluate.
- **Returns**: 
  - `True` if all keys are strings and are either all lowercase or all uppercase.
  - `False` if the dictionary is empty, contains non-string keys, or if the keys are mixed case.

### Examples

```python
check_dict_case({"a": "apple", "b": "banana"})  # Returns: True
check_dict_case({"a": "apple", "A": "banana", "B": "banana"})  # Returns: False
check_dict_case({"a": "apple", 8: "banana", "a": "apple"})  # Returns: False
check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})  # Returns: False
check_dict_case({"STATE": "NC", "ZIP": "12345"})  # Returns: True
```

## Installation

No external dependencies are required for this utility. It is implemented in pure Python.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing `main.py`.

3. **Run the Function**: You can test the function by running a Python interpreter and importing the function.

```bash
python
```

```python
from main import check_dict_case

# Test the function with different dictionaries
print(check_dict_case({"a": "apple", "b": "banana"}))  # Should print: True
```

## Documentation

For further details and updates, please refer to the source code documentation within the `main.py` file.

```