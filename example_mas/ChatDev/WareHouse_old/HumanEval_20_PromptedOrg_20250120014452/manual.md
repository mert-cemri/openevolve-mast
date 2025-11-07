# Find Closest Elements

This software provides a function to find the two closest numbers in a list of floating-point numbers. It is designed to be simple and efficient, ensuring that users can quickly identify the closest pair of numbers from any given list.

## Main Functionality

The main function of this software is:

- **find_closest_elements(numbers: List[float]) -> Tuple[float, float]:** This function takes a list of floating-point numbers as input and returns a tuple containing the two numbers that are closest to each other in value. The numbers in the tuple are returned in ascending order.

### Example Usage

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers.")
    # Sort the list to make it easier to find the closest elements
    numbers.sort()
    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[1])
    # Iterate through the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair

# Example
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
```

## Installation

This software does not require any external dependencies, making it easy to use in any Python environment. Simply ensure that you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the script**: Save the `main.py` script to your local machine.

3. **Run the script**: You can execute the script using a Python interpreter to test the function with your own list of numbers.

## How to Use

1. **Prepare your list of numbers**: Ensure your list contains at least two floating-point numbers.

2. **Call the function**: Use the `find_closest_elements` function by passing your list as an argument.

3. **Receive the result**: The function will return a tuple with the two closest numbers in ascending order.

## Documentation

This software is straightforward and does not require extensive documentation. The function is self-contained and does not rely on any external libraries or frameworks. For any further questions or support, please contact our support team.