# Monotonic Function User Manual

This software provides a simple utility function to determine if a list of numbers is monotonically increasing or decreasing.

## Main Function

The primary function of this software is:

- **monotonic(l: list) -> bool**: This function takes a list of numbers as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise.

### Function Details

- **Monotonically Increasing**: A list is considered monotonically increasing if each element is greater than or equal to the preceding element.
- **Monotonically Decreasing**: A list is considered monotonically decreasing if each element is less than or equal to the preceding element.

#### Example Usage

```python
>>> monotonic([1, 2, 4, 20])
True
>>> monotonic([1, 20, 4, 10])
False
>>> monotonic([4, 1, 0, -10])
True
```

## Installation

This software does not require any external dependencies. You only need Python installed on your system to run the function.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can run the function by executing the `main.py` file in a Python environment. Use the Python interactive shell or include the function in your own Python scripts.

### Example

To use the function in a Python script:

```python
from main import monotonic

# Test the function with a list
result = monotonic([1, 2, 4, 20])
print(result)  # Output: True
```

## Documentation

For further details on how to use the function, refer to the docstring provided in the `main.py` file. The docstring includes example usage and expected outputs for different input scenarios.

This software is designed to be simple and efficient, providing a straightforward solution for checking the monotonicity of a list of numbers.