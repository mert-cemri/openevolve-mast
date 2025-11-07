# CountNums User Manual

Welcome to the CountNums software! This application provides a simple yet powerful function to analyze arrays of integers and determine how many elements have a sum of digits greater than zero.

## Main Functionality

The core functionality of this software is encapsulated in the `count_nums` function. This function takes an array of integers as input and returns the number of elements in the array for which the sum of their digits is greater than zero. The function handles both positive and negative integers, considering the sign of the first digit in negative numbers.

### Function Definition

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

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed**: You can download and install Python from the [official website](https://www.python.org/downloads/).

2. **Clone or download the repository**: Obtain the source code by cloning the repository or downloading it as a ZIP file.

3. **Navigate to the project directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

## How to Use

1. **Open the `main.py` file**: You can use any text editor or IDE of your choice.

2. **Modify the input array**: Change the array passed to the `count_nums` function to test different cases.

3. **Run the script**: Execute the script using Python by running the following command in your terminal or command prompt:

   ```bash
   python main.py
   ```

4. **View the output**: The result will be printed to the console, showing the number of elements with a sum of digits greater than zero.

## Documentation

For further details on the implementation and examples, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and make any necessary modifications.

Thank you for using CountNums! We hope this tool proves useful in your projects. If you have any questions or need support, please feel free to reach out.