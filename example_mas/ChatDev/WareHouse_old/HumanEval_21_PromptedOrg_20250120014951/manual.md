# Rescale to Unit

This software module provides a function to rescale a list of numbers to the unit interval [0, 1]. It is designed to transform any given list of floating-point numbers such that the smallest number becomes 0 and the largest number becomes 1, with all other numbers scaled linearly between these two values.

## Quick Install

No external dependencies are required for this module. It is implemented purely in Python and can be used directly in any Python environment.

## 🤔 What is this?

The `rescale_to_unit` function is a simple utility that applies a linear transformation to a list of numbers. This transformation ensures that the smallest number in the list is mapped to 0 and the largest number is mapped to 1. This is useful in various data normalization tasks where you need to scale data to a standard range.

### Main Function

- **`rescale_to_unit(numbers: List[float]) -> List[float]`**

  - **Parameters:**
    - `numbers`: A list of floating-point numbers with at least two elements.

  - **Returns:**
    - A new list of numbers where the smallest number is 0 and the largest number is 1, with all other numbers scaled linearly between them.

  - **Example:**
    ```python
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    ```

## How to Use

1. **Ensure you have Python installed**: This module requires Python to run. You can download and install Python from [python.org](https://www.python.org/).

2. **Create a Python script or open a Python environment**: You can use this function in any Python script or interactive environment like Jupyter Notebook or Python's IDLE.

3. **Copy the function code**: Copy the `rescale_to_unit` function from the provided code snippet into your script or environment.

4. **Call the function with your data**: Pass a list of floating-point numbers to the `rescale_to_unit` function to get the rescaled list.

## Example Usage

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ 
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_value = min(numbers)
    max_value = max(numbers)
    return [(x - min_value) / (max_value - min_value) for x in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This simple and efficient function can be integrated into larger data processing pipelines or used standalone for quick data normalization tasks.