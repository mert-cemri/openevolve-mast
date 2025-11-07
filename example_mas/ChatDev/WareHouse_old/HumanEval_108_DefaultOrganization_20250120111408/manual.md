# CountNums User Manual

Welcome to the CountNums software! This application is designed to help you count the number of integers in an array where the sum of the digits is greater than zero. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it.

## Quick Install

To get started with CountNums, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Step 1: Clone the Repository

First, clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of the repository.

### Step 2: Navigate to the Project Directory

Navigate to the directory where the project is located:

```bash
cd <project-directory>
```

Replace `<project-directory>` with the actual directory name.

### Step 3: Install Dependencies

Currently, there are no additional dependencies required for this project. However, if any dependencies are added in the future, they will be listed in the `requirements.txt` file. You can install them using:

```bash
pip install -r requirements.txt
```

## Main Functionality

The main functionality of the CountNums software is encapsulated in the `count_nums` function. This function takes an array of integers as input and returns the number of elements where the sum of the digits is greater than zero.

### Function Definition

```python
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
```

### How It Works

- The function iterates over each integer in the input array.
- For each integer, it calculates the sum of its digits.
- If the sum of the digits is greater than zero, it increments the count.
- Finally, it returns the count of such integers.

## How to Use

To use the `count_nums` function, follow these steps:

1. Open a Python interpreter or create a Python script.
2. Import the `count_nums` function from the `main.py` file.
3. Call the `count_nums` function with an array of integers as the argument.

### Example Usage

```python
from main import count_nums

# Example 1
result1 = count_nums([])
print(result1)  # Output: 0

# Example 2
result2 = count_nums([-1, 11, -11])
print(result2)  # Output: 1

# Example 3
result3 = count_nums([1, 1, 2])
print(result3)  # Output: 3
```

## Conclusion

The CountNums software is a simple yet powerful tool for counting integers based on the sum of their digits. We hope this manual helps you get started with using the software effectively. If you have any questions or need further assistance, please feel free to reach out to our support team.