# Count Nums User Manual

Welcome to the Count Nums software, a simple Python application designed to count the number of integers in an array whose sum of digits is greater than zero. This manual will guide you through the installation process, introduce the main function of the software, and provide instructions on how to use it.

## Main Functionality

The primary function of this software is `count_nums`, which takes an array of integers as input and returns the number of elements that have a sum of digits greater than zero. The function handles both positive and negative integers, considering the sign of the first digit in negative numbers.

### Example Usage

- `count_nums([])` returns `0`
- `count_nums([-1, 11, -11])` returns `1`
- `count_nums([1, 1, 2])` returns `3`

## Installation

This software does not require any external dependencies, making the installation process straightforward. You only need to have Python installed on your system.

### Step-by-Step Installation Guide

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the source code by cloning the repository or downloading it as a ZIP file.

3. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the source code is located.

## How to Use

Once you have the software set up, you can use the `count_nums` function in your Python scripts or interactive sessions. Here’s how you can do it:

1. **Open a Python Environment**: You can use a Python shell, Jupyter Notebook, or any Python IDE.

2. **Import the Function**: If you are using the function in a different script, make sure to import it:
   ```python
   from main import count_nums
   ```

3. **Call the Function**: Pass an array of integers to the `count_nums` function and capture the result:
   ```python
   result = count_nums([-1, 11, -11])
   print(result)  # Output will be 1
   ```

## Conclusion

The Count Nums software is a simple yet effective tool for counting integers based on the sum of their digits. With no external dependencies, it is easy to set up and use in any Python environment. We hope this manual helps you get started quickly and efficiently. If you have any questions or need further assistance, please feel free to reach out.