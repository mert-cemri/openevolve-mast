# Find Closest Elements

This software provides a function to find the two closest numbers in a list of floating-point numbers. It is designed to be simple and efficient, requiring no external dependencies.

## Main Functionality

The main function of this software is:

- `find_closest_elements(numbers: List[float]) -> Tuple[float, float]`: This function takes a list of floating-point numbers as input and returns a tuple containing the two numbers that are closest to each other in value. The returned numbers are ordered such that the smaller number comes first.

### Example Usage

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    # Initialize the minimum difference as infinity and the closest pair
    min_diff = float('inf')
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    # Iterate through the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        # Calculate the difference between consecutive numbers
        diff = sorted_numbers[i + 1] - sorted_numbers[i]
        # Update the closest pair if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    return closest_pair

# Example
result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
print(result)  # Output: (2.0, 2.2)
```

## Installation

This software does not require any external dependencies, so there is no need to install additional packages. Simply ensure you have Python installed on your system.

## How to Use

1. **Prepare Your Environment:**
   - Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Run the Code:**
   - Copy the function `find_closest_elements` into your Python script or interactive environment.
   - Call the function with a list of floating-point numbers to find the two closest numbers.

3. **Example:**
   - Use the provided example in the "Example Usage" section to test the function.

## Documentation

This software is straightforward and does not require extensive documentation. The function is self-contained and can be easily integrated into larger projects where finding the closest pair of numbers is necessary.

For any further inquiries or support, please contact our support team.