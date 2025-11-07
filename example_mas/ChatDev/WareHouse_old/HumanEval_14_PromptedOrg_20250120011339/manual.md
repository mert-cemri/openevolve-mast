# All Prefixes Function

This software provides a simple function to generate all prefixes of a given string. It is implemented in Python and does not require any external dependencies.

## Main Functionality

The main function of this software is `all_prefixes`, which takes a single string as input and returns a list of all prefixes of that string, ordered from shortest to longest.

### Function Definition

```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]
```

### Example Usage

```python
>>> all_prefixes('abc')
['a', 'ab', 'abc']
```

## Installation

This software does not require any external libraries or dependencies. It is implemented in pure Python, and you can run it in any environment where Python is installed.

### Quick Install

Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function in a Python script or an interactive Python session. Simply import the function and call it with your desired string.

### Example

```python
from main import all_prefixes

result = all_prefixes('hello')
print(result)  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

## Documentation

The function is straightforward and self-contained. For further details or questions, please refer to the docstring within the code or contact support.

## Support

For any issues or questions, please contact our support team. We are here to help you make the most out of this software.