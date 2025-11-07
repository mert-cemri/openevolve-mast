# Rescale to Unit

This software provides a simple utility function to rescale a list of numbers to a unit scale, where the smallest number becomes 0 and the largest becomes 1. This is useful for normalizing data for various applications, such as machine learning preprocessing.

## Main Functionality

The main function provided by this software is `rescale_to_unit`, which takes a list of floating-point numbers and returns a new list where the numbers are linearly transformed to fit within the range [0, 1].

### Function Definition

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
```

### How It Works

- **Input**: A list of floating-point numbers with at least two elements.
- **Output**: A list of numbers rescaled to the range [0, 1].

The function calculates the minimum and maximum values in the list, computes the range, and then applies a linear transformation to each number in the list.

## Installation

This software does not require any external dependencies beyond Python itself. You can use it directly by including the `main.py` file in your project.

### Quick Install

1. Ensure you have Python installed on your system.
2. Clone or download the `main.py` file to your project directory.

## Usage

To use the `rescale_to_unit` function, simply import it into your Python script and call it with a list of numbers.

### Example

```python
from main import rescale_to_unit

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This example demonstrates how to import and use the function to rescale a list of numbers.

## Documentation

For further information and examples, please refer to the inline documentation within the `main.py` file. The function is designed to be straightforward and easy to integrate into your existing projects.