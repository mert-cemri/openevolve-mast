# Get Positive Numbers

This software provides a simple utility function to filter and return only the positive numbers from a given list of integers.

## Main Functionality

The primary function of this software is:

- `get_positive(l: list)`: This function takes a list of integers as input and returns a new list containing only the positive integers from the input list.

### Example Usage

```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

## Installation

This software does not require any external dependencies, making it straightforward to use. You can simply download the `main.py` file and run it in any Python environment.

### Requirements

- Python 3.x

## How to Use

1. **Download the Code**: Obtain the `main.py` file containing the function definition.

2. **Run the Code**: You can run the code in any Python environment. Open a Python shell or script and import the function:

   ```python
   from main import get_positive
   ```

3. **Call the Function**: Use the `get_positive` function by passing a list of integers as an argument:

   ```python
   positive_numbers = get_positive([-1, 2, -4, 5, 6])
   print(positive_numbers)  # Output: [2, 5, 6]
   ```

## Additional Information

- **No External Libraries**: This software is self-contained and does not require any additional Python packages beyond the standard library.

- **Simple and Efficient**: The function uses list comprehension for efficient filtering of positive numbers.

Feel free to modify and integrate this function into your projects as needed. If you have any questions or need further assistance, please contact our support team.