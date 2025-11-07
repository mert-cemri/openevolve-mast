manual.md

```
# Find Closest Elements

A Python utility to find and return the two closest numbers from a list of floating-point numbers. The numbers are returned in ascending order.

## Main Function

The main function provided by this utility is `find_closest_elements`, which takes a list of floating-point numbers and returns a tuple containing the two closest numbers in ascending order.

### Function Signature

```python
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
```

### Parameters

- `numbers`: A list of floating-point numbers with a minimum length of two.

### Returns

- A tuple of two floating-point numbers that are the closest to each other in the list, ordered from smallest to largest.

### Example Usage

```python
from main import find_closest_elements

# Example list of numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]

# Find the closest elements
closest_pair = find_closest_elements(numbers)

print(closest_pair)  # Output: (2.0, 2.2)
```

## Installation

This utility does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Ensure Python is installed** on your system. You can download Python from [python.org](https://www.python.org/downloads/).

3. **Run the script** using Python:

   ```bash
   python main.py
   ```

## How to Use

1. **Prepare your list of numbers**: Ensure your list contains at least two floating-point numbers.

2. **Call the function**: Use the `find_closest_elements` function with your list as the argument.

3. **Receive the result**: The function will return a tuple of the two closest numbers in ascending order.

## Additional Information

- This utility is designed to work with floating-point numbers and assumes that the input list is non-empty and contains at least two numbers.
- The function sorts the list internally to efficiently find the closest pair of numbers.

For any issues or further assistance, please contact our support team.
```