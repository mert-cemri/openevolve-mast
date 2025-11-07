# Count Nums User Manual

Welcome to the Count Nums software! This software provides a simple function to count the number of integers in an array whose sum of digits is greater than zero. This user manual will guide you through the installation process, introduce the main function, and demonstrate how to use the software.

## Main Function

The core functionality of this software is provided by the `count_nums` function. This function takes an array of integers and returns the number of elements where the sum of the digits is greater than zero. It considers the sign of the number when calculating the sum of digits.

### Function Signature

```python
def count_nums(arr):
    """
    Takes an array of integers and returns the number of elements with a sum of digits > 0.
    """
```

### Example Usage

- `count_nums([])` returns `0`
- `count_nums([-1, 11, -11])` returns `1`
- `count_nums([1, 1, 2])` returns `3`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Follow the steps below to get started:

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Directory

Change into the project directory:

```bash
cd <project-directory>
```

### Step 3: Install Python

Ensure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 4: Verify No Dependencies

Since there are no external dependencies, you can proceed to use the software directly.

## How to Use

To use the `count_nums` function, follow these steps:

1. Open a Python interpreter or create a Python script.
2. Import the `count_nums` function from the `main.py` file.
3. Call the `count_nums` function with an array of integers as the argument.

### Example

```python
from main import count_nums

# Example array
arr = [-1, 11, -11]

# Call the function
result = count_nums(arr)

# Print the result
print(f"The number of elements with a sum of digits > 0 is: {result}")
```

## Conclusion

The Count Nums software is a straightforward tool for counting integers in an array based on the sum of their digits. With no external dependencies, it is easy to set up and use. We hope this manual helps you get started quickly and effectively. If you have any questions or need further assistance, please feel free to reach out.