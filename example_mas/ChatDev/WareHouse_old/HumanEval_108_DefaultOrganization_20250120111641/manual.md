manual.md

```
# Count Nums

A simple Python utility to count the number of integers in an array whose sum of digits is greater than zero. This utility handles both positive and negative integers.

## Main Functionality

The primary function of this software is `count_nums`, which takes an array of integers and returns the count of numbers whose sum of digits is greater than zero. The function considers the sign of the number, treating the first digit of negative numbers as negative.

### Example Usage

- `count_nums([])` returns `0`
- `count_nums([-1, 11, -11])` returns `1`
- `count_nums([1, 1, 2])` returns `3`

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the code by cloning the repository or downloading the zip file.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Move into the directory where the `main.py` file is located.

   ```bash
   cd <project-directory>
   ```

4. **Run the Code**: You can run the code directly using Python.

   ```bash
   python main.py
   ```

## How to Use

1. **Prepare Your Input**: Create a list of integers that you want to analyze.

2. **Call the Function**: Use the `count_nums` function with your list as the argument.

   ```python
   from main import count_nums

   result = count_nums([-1, 11, -11])
   print(result)  # Output will be 1
   ```

3. **Interpret the Result**: The function will return an integer representing the count of numbers with a sum of digits greater than zero.

## Additional Information

- **No External Libraries**: This software is designed to be lightweight and does not require any additional Python packages.

- **Compatibility**: The code is compatible with Python 3.x versions.

- **Support**: For any issues or questions, please contact our support team at support@chatdev.com.

```