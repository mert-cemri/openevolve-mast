manual.md

```
# Rescale to Unit

A simple Python function to linearly transform a list of numbers such that the smallest number becomes 0 and the largest becomes 1.

## Overview

The `rescale_to_unit` function takes a list of floating-point numbers and applies a linear transformation. This transformation rescales the list so that the smallest number becomes 0 and the largest becomes 1, with all other numbers proportionally adjusted between these two values.

## Main Function

### rescale_to_unit

- **Description**: Transforms a list of numbers to a scale where the smallest number is 0 and the largest is 1.
- **Input**: A list of floats with at least two elements.
- **Output**: A list of floats rescaled to the unit interval [0, 1].

#### Example Usage

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    return [(num - min_val) / range_val for num in numbers]

# Example
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

## Installation

### Environment Setup

This function does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Move into the directory where the code is located.

   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can directly run the Python script containing the `rescale_to_unit` function.

   ```bash
   python main.py
   ```

## Usage

1. **Import the Function**: Ensure the function is imported into your script or interactive session.

   ```python
   from main import rescale_to_unit
   ```

2. **Call the Function**: Pass a list of floats to the function and receive the rescaled list.

   ```python
   rescaled_numbers = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
   print(rescaled_numbers)
   ```

## Notes

- The input list must contain at least two elements.
- The function assumes all elements in the list are numeric and comparable.
- The function does not handle cases where all numbers in the list are the same, as this would result in a division by zero error.

```