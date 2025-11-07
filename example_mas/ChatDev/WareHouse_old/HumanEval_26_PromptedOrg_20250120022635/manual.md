# Remove Duplicates

This software provides a simple utility function to remove duplicate integers from a list, retaining only those elements that appear once and maintaining their original order.

## Main Functionality

The main function of this software is `remove_duplicates`, which processes a list of integers and returns a new list with all elements that occur more than once removed. The order of the remaining elements is preserved as in the input list.

### Function Definition

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
```

## Installation

This software does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the repository** (if applicable) or download the `main.py` file to your local machine.

2. **Verify Python Installation**: Ensure Python is installed by running:

   ```bash
   python --version
   ```

   If Python is not installed, download and install it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Prepare Your Environment**: Make sure you have Python installed as described above.

2. **Run the Function**: You can use the function by importing it into your Python script or interactive session. Here's an example of how to use it:

   ```python
   from main import remove_duplicates

   # Example usage
   numbers = [1, 2, 3, 2, 4]
   result = remove_duplicates(numbers)
   print(result)  # Output: [1, 3, 4]
   ```

3. **Testing**: You can test the function with different lists of integers to ensure it behaves as expected.

## Documentation

For further details on Python usage and list operations, refer to the official [Python documentation](https://docs.python.org/3/).

This software is designed to be simple and straightforward, focusing on solving the specific task of removing duplicates from a list of integers. If you have any questions or need further assistance, please contact our support team.