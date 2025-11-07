# Find Closest Elements

This software provides a function to find the two closest numbers in a list of floating-point numbers. It is designed to be simple and efficient, requiring no external dependencies.

## Main Function

The main function of this software is `find_closest_elements`, which takes a list of floating-point numbers and returns a tuple containing the two numbers that are closest to each other in ascending order.

### Function Signature

```python
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
```

### Parameters

- `numbers` (List[float]): A list of floating-point numbers. The list must contain at least two numbers.

### Returns

- `Tuple[float, float]`: A tuple containing the two closest numbers in ascending order.

### Examples

```python
>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
(2.0, 2.2)

>>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
(2.0, 2.0)
```

## Installation

This software does not require any external packages. It only requires Python to be installed on your system.

### Quick Install

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the `main.py` file is located.

3. **Run the Function**: You can use the function by importing it into your Python script or by running it directly in a Python interactive shell.

### Example Usage

```python
from main import find_closest_elements

numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
closest_pair = find_closest_elements(numbers)
print(closest_pair)  # Output: (2.0, 2.2)
```

## Documentation

For further details on how the function works, please refer to the docstring within the `main.py` file. It provides a comprehensive explanation of the function's purpose, parameters, and return values.

This software is designed to be straightforward and efficient, making it easy to integrate into larger projects or use as a standalone utility for finding the closest pair of numbers in a list.