# CountNums User Manual

Welcome to the CountNums software, a simple Python application designed to count the number of integers in an array whose sum of digits is greater than 0. This manual will guide you through the main functions of the software, how to install it, and how to use it effectively.

## Main Functions

The primary function of this software is `count_nums`, which takes an array of integers and returns the count of elements whose sum of digits is greater than 0. This function is useful for analyzing arrays of integers and filtering them based on the sum of their digits.

### Function Details

- **`count_nums(arr)`**: 
  - **Input**: A list of integers.
  - **Output**: An integer representing the count of elements with a sum of digits greater than 0.
  - **Example Usage**:
    - `count_nums([])` returns `0`
    - `count_nums([-1, 11, -11])` returns `1`
    - `count_nums([1, 1, 2])` returns `3`

## Installation

The CountNums software does not require any external dependencies, making it easy to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If you have access to the repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to where the `main.py` file is located:
   ```bash
   cd <repository-directory>
   ```

4. **Run the Script**: Execute the script using Python:
   ```bash
   python main.py
   ```

## How to Use

To use the CountNums software, follow these simple steps:

1. **Prepare Your Data**: Have your list of integers ready that you want to analyze.

2. **Call the Function**: Use the `count_nums` function by passing your list of integers as an argument.

3. **View the Result**: The function will return the count of numbers whose sum of digits is greater than 0.

### Example

Here's a quick example of how you can use the software:

```python
# Example usage
print(count_nums([]))  # Output: 0
print(count_nums([-1, 11, -11]))  # Output: 1
print(count_nums([1, 1, 2]))  # Output: 3
```

## Conclusion

The CountNums software is a straightforward tool for analyzing arrays of integers based on the sum of their digits. With no external dependencies, it is easy to set up and use. We hope this manual helps you get the most out of the software. If you have any questions or need further assistance, please feel free to reach out.