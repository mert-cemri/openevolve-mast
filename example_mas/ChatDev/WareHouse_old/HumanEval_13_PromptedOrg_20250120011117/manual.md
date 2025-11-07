# Greatest Common Divisor (GCD) Calculator

This software module provides a function to calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The GCD is the largest positive integer that divides each of the integers without leaving a remainder.

## Main Function

The primary function provided by this module is:

- `greatest_common_divisor(a: int, b: int) -> int`: This function takes two integers `a` and `b` as input and returns their greatest common divisor.

### Example Usage

```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```

## Installation

To use this software, you need to have Python installed on your system. The module does not have any external dependencies, so no additional packages are required.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted in a version control system, clone the repository to your local machine.

3. **Navigate to the project directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

## How to Use

1. **Open a Python environment**: You can use a Python interpreter, a Jupyter notebook, or any Python IDE of your choice.

2. **Import the function**: In your Python environment, import the `greatest_common_divisor` function from the `main.py` file.

   ```python
   from main import greatest_common_divisor
   ```

3. **Call the function**: Use the function by passing two integers as arguments to calculate their GCD.

   ```python
   result = greatest_common_divisor(25, 15)
   print(result)  # Output: 5
   ```

## Documentation

This module is straightforward and does not require additional documentation beyond the examples provided. The function implements the Euclidean algorithm, which is efficient and widely used for computing the GCD.

For any further questions or support, please contact the development team.