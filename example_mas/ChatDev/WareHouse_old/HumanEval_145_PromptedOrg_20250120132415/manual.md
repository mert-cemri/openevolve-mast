# Order By Points

This software provides a function to sort a list of integers based on the sum of their digits. If multiple integers have the same digit sum, they are ordered based on their original index in the list.

## Main Functionality

The main function provided by this software is `order_by_points`, which sorts a list of integers according to the sum of their digits. This function is useful for applications where sorting based on digit sum is required.

### Function: `order_by_points`

- **Input**: A list of integers.
- **Output**: A list of integers sorted in ascending order based on the sum of their digits. If two numbers have the same digit sum, they are ordered by their original position in the list.

#### Example Usage

```python
>>> order_by_points([1, 11, -1, -11, -12])
[-1, -11, 1, -12, 11]

>>> order_by_points([])
[]
```

## Installation

To use this software, you need to have Python installed on your system. The function does not require any external dependencies, so no additional packages need to be installed.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from [python.org](https://www.python.org/).

2. **Clone the repository or download the script**: Obtain the `main.py` file containing the `order_by_points` function.

3. **Run the script**: You can execute the script in a Python environment to use the `order_by_points` function.

## How to Use

1. **Import the function**: If you have the `main.py` file, you can import the function into your Python script or interactive session.

   ```python
   from main import order_by_points
   ```

2. **Call the function**: Pass a list of integers to the `order_by_points` function to get the sorted list.

   ```python
   sorted_list = order_by_points([1, 11, -1, -11, -12])
   print(sorted_list)  # Output: [-1, -11, 1, -12, 11]
   ```

## Documentation

This function is straightforward and does not require additional documentation beyond the examples provided. If you have any questions or need further assistance, please contact our support team.

## Support

For any issues or questions, please reach out to our support team through our official website or contact us via email. We are here to help you with any challenges you might face while using our software.