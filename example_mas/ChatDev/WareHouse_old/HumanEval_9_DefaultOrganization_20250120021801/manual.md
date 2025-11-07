# Rolling Max Software

This software provides a simple utility function to generate a list of rolling maximum elements from a given list of integers. It is designed to be lightweight and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this software is `rolling_max`, which takes a list of integers as input and returns a list of the rolling maximum values up to each point in the sequence.

### Function Definition

```python
def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
```

### Example Usage

```python
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
```

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change into the directory containing the `main.py` file.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Code**: You can directly run the Python script using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: Import the `rolling_max` function from the `main.py` file into your Python script or interactive session.

   ```python
   from main import rolling_max
   ```

2. **Call the Function**: Pass a list of integers to the `rolling_max` function to get the rolling maximum list.

   ```python
   result = rolling_max([1, 2, 3, 2, 3, 4, 2])
   print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
   ```

## Documentation

For further details on the implementation and usage of the `rolling_max` function, please refer to the docstring provided within the code. The function is straightforward and designed to be used with minimal setup.

## Support

For any issues or questions regarding the software, please contact our support team or refer to the documentation provided within the code. We are committed to providing assistance to ensure the software meets your needs.