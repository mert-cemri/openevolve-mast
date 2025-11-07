# Largest Divisor Finder

This software provides a simple function to find the largest divisor of a given integer `n` that is smaller than `n` itself. It is a straightforward utility function implemented in Python.

## Main Functionality

The main function provided by this software is `largest_divisor(n: int) -> int`. This function takes an integer `n` as input and returns the largest integer that divides `n` evenly and is smaller than `n`.

### Example Usage

```python
>>> largest_divisor(15)
5
```

In this example, the largest divisor of 15 that is smaller than 15 is 5.

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional dependencies beyond Python itself.

### Steps to Install Python

1. **Download Python**: Visit the official [Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**: Follow the installation instructions provided on the Python website for your specific operating system.

3. **Verify Installation**: Open a terminal or command prompt and run the following command to verify that Python is installed correctly:

   ```bash
   python --version
   ```

   This should display the version of Python that you installed.

## How to Use

1. **Create a Python File**: Create a new file named `main.py` and copy the following code into it:

   ```python
   def largest_divisor(n: int) -> int:
       """ For a given number n, find the largest number that divides n evenly, smaller than n
       >>> largest_divisor(15)
       5
       """
       for i in range(n-1, 0, -1):
           if n % i == 0:
               return i
       return 1  # In case n is 1, the largest divisor smaller than n is 1
   ```

2. **Run the Code**: Open a terminal or command prompt, navigate to the directory containing `main.py`, and run the following command:

   ```bash
   python main.py
   ```

3. **Test the Function**: You can test the function by calling it with different values of `n` and printing the result. For example:

   ```python
   print(largest_divisor(15))  # Output: 5
   ```

## Documentation

The function is self-documented with a docstring that explains its purpose and provides an example. For further information or questions, you can refer to the Python documentation for general Python programming guidance.

This software is designed to be simple and easy to use, providing a specific utility function without any unnecessary complexity.