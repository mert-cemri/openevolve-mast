# Order By Points User Manual

Welcome to the Order By Points software! This application provides a simple yet effective way to sort a list of integers based on the sum of their digits. This user manual will guide you through the main functions of the software, how to set up the environment, and how to use the application.

## Main Functions

The primary function of this software is `order_by_points`, which sorts a list of integers in ascending order based on the sum of their digits. If two numbers have the same digit sum, they retain their original order in the list.

### Function Definition

```python
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index in the original list.
    Parameters:
    nums (list): A list of integers.
    Returns:
    list: A list of integers sorted by the sum of their digits.
    """
```

### Example Usage

```python
# Example usage:
print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
print(order_by_points([]))  # Output: []
```

## Installation

This software does not require any external packages, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download Python from the official website [here](https://www.python.org/downloads/).

2. **Clone the repository**: If the code is hosted on a version control system, clone the repository to your local machine.

3. **Navigate to the project directory**: Open your terminal or command prompt and navigate to the directory where the `main.py` file is located.

## Usage

To use the `order_by_points` function, follow these steps:

1. **Open the `main.py` file**: This file contains the implementation of the `order_by_points` function.

2. **Modify the input list**: Change the list of integers in the example usage section to your desired list.

3. **Run the script**: Execute the script using Python by running the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

4. **View the output**: The sorted list will be printed to the console.

## Conclusion

The Order By Points software is a straightforward tool for sorting integers based on the sum of their digits. With no external dependencies, it is easy to set up and use. We hope this user manual helps you get started quickly and effectively. If you have any questions or need further assistance, please feel free to reach out to our support team.