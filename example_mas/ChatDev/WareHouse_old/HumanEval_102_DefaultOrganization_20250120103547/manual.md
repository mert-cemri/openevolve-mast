# Choose_Num User Manual

Welcome to the Choose_Num software! This software provides a simple function to determine the largest even integer within a specified range of two positive numbers. This manual will guide you through the installation process, introduce the main function, and provide instructions on how to use it.

## Main Function

The core functionality of this software is encapsulated in the `choose_num` function. This function takes two positive integers, `x` and `y`, and returns the largest even integer within the inclusive range `[x, y]`. If no even integer exists within this range, the function returns `-1`.

### Function Definition

```python
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.
    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
```

### Example Usage

- `choose_num(12, 15)` returns `14`
- `choose_num(13, 12)` returns `-1`

## Installation

This software does not require any external dependencies, making the installation process straightforward. You only need to have Python installed on your system.

### Step-by-Step Installation

1. **Ensure Python is Installed**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the source code by cloning the repository or downloading it as a ZIP file from the source.

3. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

## How to Use

1. **Open a Python Environment**: You can use any Python environment such as IDLE, PyCharm, or simply the command line.

2. **Import the Function**: In your Python script or interactive shell, import the `choose_num` function from the `main.py` file.

   ```python
   from main import choose_num
   ```

3. **Call the Function**: Use the `choose_num` function by passing two positive integers as arguments.

   ```python
   result = choose_num(12, 15)
   print(result)  # Output: 14
   ```

4. **Interpret the Result**: The function will return the largest even integer within the specified range or `-1` if no such number exists.

## Conclusion

The Choose_Num software provides a simple yet effective way to find the largest even integer within a given range of numbers. With no external dependencies, it is easy to install and use. We hope this manual helps you get started quickly and efficiently. If you have any questions or need further assistance, please feel free to reach out to our support team.