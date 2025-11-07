# Find Closest Elements

This software provides a function to find the two closest numbers in a list of floating-point numbers. The function returns these two numbers in ascending order.

## Main Functionality

The main function of this software is:

- **find_closest_elements(numbers: List[float]) -> Tuple[float, float]:** This function takes a list of floating-point numbers as input and returns a tuple containing the two numbers that are closest to each other in the list. The numbers in the tuple are returned in ascending order.

### Example Usage

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list to ensure closest elements are adjacent
    sorted_numbers = sorted(numbers)
    # Initialize variables to store the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    # Iterate through the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between adjacent numbers
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        # Update the closest pair if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    return closest_pair

# Example
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

## How to Use

1. **Prepare your environment:**
   - Make sure Python is installed on your system.

2. **Run the code:**
   - Copy the code provided in the example usage section into a Python file, e.g., `main.py`.
   - Run the file using the command `python main.py` in your terminal or command prompt.

3. **Input:**
   - The function `find_closest_elements` expects a list of floating-point numbers with at least two elements.

4. **Output:**
   - The function returns a tuple containing the two closest numbers from the list, in ascending order.

## Documentation

For further information, please refer to the inline comments in the code which explain the logic and flow of the function. This software is designed to be simple and efficient for finding the closest pair of numbers in a list.