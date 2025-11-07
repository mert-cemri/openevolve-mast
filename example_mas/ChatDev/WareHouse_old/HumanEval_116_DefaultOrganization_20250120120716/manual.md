# Sort Array User Manual

Welcome to the Sort Array software! This software provides a function to sort arrays of integers based on specific criteria related to their binary representation. This manual will guide you through the main functions of the software, how to install any necessary dependencies, and how to use the software effectively.

## Main Functions

The core function of this software is `sort_array`, which sorts an array of integers according to the following rules:

1. **Non-negative Integers**: These are sorted based on the number of ones in their binary representation in ascending order. If two numbers have the same number of ones, they are sorted by their decimal value.

2. **Negative Integers**: These are sorted by their decimal value in ascending order.

### Function Signature

```python
def sort_array(arr):
    """
    Sort an array of integers according to the number of ones in their binary
    representation in ascending order for non-negative integers. For similar number of ones,
    sort based on decimal value. Negative numbers should be sorted by their decimal value.
    
    Args:
    arr (list): A list of integers.
    
    Returns:
    list: A sorted list of integers.
    """
```

### Example Usage

```python
# Example usage of sort_array function
print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
```

## Installation

### Environment Setup

This software is implemented in Python and does not require any additional dependencies beyond the standard Python library. Ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Quick Install

Since there are no external dependencies, you can directly use the software by running the `main.py` file.

## How to Use

1. **Clone the Repository**: If you have access to the repository, clone it to your local machine.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory containing `main.py`.

3. **Run the Script**: Execute the script using Python to see the function in action.

   ```bash
   python main.py
   ```

4. **Modify the Input**: You can modify the input array in the `main.py` file to test the function with different data.

## Conclusion

This software provides a simple yet effective way to sort arrays of integers based on binary representation and decimal values. It is designed to be easy to use and requires no additional setup beyond having Python installed. Enjoy using the Sort Array software!