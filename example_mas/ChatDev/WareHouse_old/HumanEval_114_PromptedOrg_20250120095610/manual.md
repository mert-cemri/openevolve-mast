# MinSubArraySum User Manual

## Introduction

The `minSubArraySum` function is a Python utility designed to find the minimum sum of any non-empty sub-array within a given array of integers. This function is particularly useful in scenarios where you need to identify the smallest possible sum that can be obtained from contiguous elements in an array.

### Main Functionality

- **Function Name**: `minSubArraySum`
- **Purpose**: To compute the minimum sum of any non-empty sub-array from a list of integers.
- **Input**: A list of integers `nums`.
- **Output**: An integer representing the minimum sum of any non-empty sub-array.

### Example Usage

- `minSubArraySum([2, 3, 4, 1, 2, 4])` returns `1`.
- `minSubArraySum([-1, -2, -3])` returns `-6`.

## Installation

This software does not require any external dependencies. It is implemented purely in Python, and you can run it in any standard Python environment.

### Quick Start

1. **Ensure you have Python installed**: This script requires Python to run. You can download and install Python from [python.org](https://www.python.org/downloads/).

2. **Download the Script**: Save the `main.py` file containing the `minSubArraySum` function to your local machine.

3. **Run the Script**: You can execute the script using a Python interpreter. Open a terminal or command prompt, navigate to the directory containing `main.py`, and run the following command:

   ```bash
   python main.py
   ```

   You can also directly use the function in a Python interactive shell or integrate it into your own Python scripts.

## How to Use

1. **Import the Function**: If you want to use the function in another script, you can import it as follows:

   ```python
   from main import minSubArraySum
   ```

2. **Call the Function**: Pass a list of integers to the function to get the minimum sub-array sum.

   ```python
   result = minSubArraySum([2, 3, 4, 1, 2, 4])
   print(result)  # Output: 1
   ```

3. **Modify and Experiment**: Feel free to modify the input list to test different scenarios and understand how the function behaves with various datasets.

## Conclusion

The `minSubArraySum` function is a simple yet powerful tool for finding the minimum sum of contiguous elements in an array. With no external dependencies, it is easy to integrate into any Python project. Enjoy exploring the possibilities with this utility!