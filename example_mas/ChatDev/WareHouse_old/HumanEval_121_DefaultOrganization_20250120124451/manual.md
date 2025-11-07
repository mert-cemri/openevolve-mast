manual.md

```
# Solution Function

This software provides a simple function to calculate the sum of all odd elements that are located at even positions in a given list of integers. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The core functionality of this software is encapsulated in the `solution` function. This function takes a non-empty list of integers as input and returns the sum of all odd integers that are located at even indices (0-based) in the list.

### Examples

- `solution([5, 8, 7, 1])` returns `12`
- `solution([3, 3, 3, 3, 3])` returns `9`
- `solution([30, 13, 24, 321])` returns `0`

## Installation

Since this project does not require any external libraries, there is no need to install additional dependencies. You can directly use the function in any Python environment.

### Requirements

- Python 3.x

## Usage

To use the `solution` function, follow these steps:

1. Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Save the provided code in a file named `main.py`.

3. Run the Python script or import the function into your own Python script.

### Example Usage

Here is how you can use the `solution` function in a Python script:

```python
from main import solution

# Example list
numbers = [5, 8, 7, 1]

# Calculate the sum of odd elements at even positions
result = solution(numbers)

# Print the result
print("The sum of odd elements at even positions is:", result)
```

This will output:

```
The sum of odd elements at even positions is: 12
```

## Conclusion

This software provides a straightforward and efficient way to calculate the sum of odd numbers at even positions in a list. With no external dependencies, it is easy to integrate into any Python project.
```