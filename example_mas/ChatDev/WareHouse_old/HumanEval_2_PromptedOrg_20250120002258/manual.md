# Truncate Number Function

This software provides a simple utility function to extract the decimal part of a given positive floating point number. The function is implemented in Python and is designed to be straightforward and easy to use.

## Main Functionality

The main function provided by this software is `truncate_number`, which takes a positive floating point number as input and returns the decimal part of that number. For example, if the input is `3.5`, the function will return `0.5`.

### Function Definition

```python
def truncate_number(number: float) -> float:
    """Return the decimal part of the given positive floating point number."""
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
```

### Example Usage

```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
```

## Installation

To use this software, you need to have Python installed on your system. The code does not require any additional dependencies beyond the standard Python library.

### Quick Install

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Download or clone the repository containing the `main.py` file.

3. **Run the Code**: Navigate to the directory containing `main.py` and execute the script using Python.

```bash
python main.py
```

## How to Use

1. **Import the Function**: If you are integrating this function into another project, you can import it directly from `main.py`.

```python
from main import truncate_number
```

2. **Call the Function**: Pass a positive floating point number to the `truncate_number` function to get the decimal part.

```python
decimal_part = truncate_number(7.89)
print(decimal_part)  # Output: 0.89
```

## Documentation

This software is designed to be simple and self-explanatory. The function `truncate_number` is the core component, and it operates independently without requiring any additional libraries or frameworks.

For any further questions or support, please contact the development team at ChatDev.