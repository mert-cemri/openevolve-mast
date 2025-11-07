# SumProduct Software

This software provides a simple utility function to calculate the sum and product of a list of integers. It is designed to be lightweight and requires no external dependencies.

## Main Functionality

The core functionality of this software is encapsulated in the `sum_product` function. This function takes a list of integers as input and returns a tuple containing two elements:
- The sum of all integers in the list.
- The product of all integers in the list.

### Example Usage

```python
from main import sum_product

# Example 1: Empty list
result = sum_product([])
print(result)  # Output: (0, 1)

# Example 2: List with integers
result = sum_product([1, 2, 3, 4])
print(result)  # Output: (10, 24)
```

## Installation

This software does not require any external libraries or dependencies. You only need Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Ensure Python is installed** on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the script** using Python. No additional setup is required.

## How to Use

1. **Import the Function**: Import the `sum_product` function from the `main.py` file.

2. **Call the Function**: Pass a list of integers to the `sum_product` function to get the sum and product.

3. **Handle the Output**: The function returns a tuple with the sum and product, which you can use as needed in your application.

## Documentation

### Function Signature

```python
def sum_product(numbers: List[int]) -> Tuple[int, int]:
```

- **Parameters**:
  - `numbers`: A list of integers for which the sum and product are to be calculated.

- **Returns**:
  - A tuple containing the sum and product of the integers in the list. If the list is empty, it returns `(0, 1)`.

### Edge Cases

- **Empty List**: The function handles empty lists by returning `(0, 1)`, where 0 is the sum and 1 is the product.

## Additional Information

This software is designed to be simple and efficient for basic numerical operations. It can be easily integrated into larger projects where such functionality is required. If you have any questions or need further assistance, please feel free to contact our support team.