manual.md

```
# iscube Function

A simple Python function to determine if a given integer is a perfect cube of another integer.

## Overview

The `iscube` function is designed to check whether a given integer is a perfect cube of some integer. This means that the function will return `True` if the input integer can be expressed as \( n^3 \) for some integer \( n \), and `False` otherwise.

### Key Features

- **Simple and Efficient**: The function uses basic arithmetic operations to determine if a number is a perfect cube.
- **Handles Negative Numbers**: The function correctly identifies negative perfect cubes.
- **No External Dependencies**: The function is implemented using pure Python, requiring no additional libraries.

## Installation

Since the `iscube` function is a standalone Python function with no external dependencies, you only need to have Python installed on your system to use it. There are no additional installation steps required.

### Prerequisites

- Python 3.x

## Usage

To use the `iscube` function, follow these steps:

1. **Clone or Download the Code**: Obtain the `main.py` file containing the `iscube` function.

2. **Run the Function**: You can run the function by executing the `main.py` file in a Python environment. Here's how you can use the function in a Python script or interactive session:

```python
# Import the iscube function from the main.py file
from main import iscube

# Test the function with various inputs
print(iscube(1))    # Output: True
print(iscube(2))    # Output: False
print(iscube(-1))   # Output: True
print(iscube(64))   # Output: True
print(iscube(0))    # Output: True
print(iscube(180))  # Output: False
```

### Example

Here's an example of how you might use the `iscube` function in a Python script:

```python
def main():
    numbers = [1, 2, -1, 64, 0, 180]
    for number in numbers:
        if iscube(number):
            print(f"{number} is a perfect cube.")
        else:
            print(f"{number} is not a perfect cube.")

if __name__ == "__main__":
    main()
```

## Conclusion

The `iscube` function is a straightforward utility for checking if an integer is a perfect cube. With no dependencies and a simple implementation, it is easy to integrate into any Python project where such functionality is needed.
```