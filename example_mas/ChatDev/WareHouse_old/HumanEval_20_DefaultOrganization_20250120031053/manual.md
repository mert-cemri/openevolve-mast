manual.md

```
# Find Closest Elements

This software provides a function to find and return two numbers from a list that are closest to each other. The numbers are returned in order, with the smaller number first.

## Main Function

### `find_closest_elements(numbers: List[float]) -> Tuple[float, float]`

- **Description**: This function takes a list of floating-point numbers and returns a tuple containing the two numbers that are closest to each other in the list. The numbers in the tuple are ordered such that the smaller number comes first.
- **Parameters**: 
  - `numbers`: A list of floating-point numbers with a length of at least two.
- **Returns**: A tuple containing two floating-point numbers that are closest to each other.

### Example Usage

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers to ensure the closest pair is found in order
    numbers.sort()
    # Initialize variables to store the closest pair and the smallest difference
    closest_pair = (numbers[0], numbers[1])
    smallest_diff = abs(numbers[1] - numbers[0])
    # Iterate through the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        current_diff = abs(numbers[i + 1] - numbers[i])
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair

# Example
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

## Installation

This software does not require any external dependencies beyond the standard Python library. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## How to Use

1. **Clone the Repository**: Clone the repository to your local machine using `git clone <repository-url>`.
2. **Navigate to the Directory**: Open a terminal and navigate to the directory containing the `main.py` file.
3. **Run the Script**: Execute the script using Python to test the function with different lists of numbers.

```bash
python main.py
```

## Documentation

For further information and documentation, please refer to the comments within the code for detailed explanations of the logic and functionality.

```