manual.md

```
# Choose Num

A simple Python function to find the largest even integer within a specified range.

## Overview

The `choose_num` function is designed to take two positive integers, `x` and `y`, and return the largest even integer within the inclusive range `[x, y]`. If no even number exists within this range, the function returns `-1`.

### Function Definition

```python
def choose_num(x, y):
    """
    This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. 
    If there's no such number, then the function should return -1.
    """
```

### Example Usage

- `choose_num(12, 15)` returns `14`
- `choose_num(13, 12)` returns `-1`

## Installation

This function does not require any external libraries or dependencies, making it easy to integrate into any Python environment.

### Quick Install

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1. **Clone or Download the Repository**

   You can clone the repository using Git or download the ZIP file and extract it to your desired location.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**

   Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

   ```bash
   cd path/to/directory
   ```

3. **Run the Function**

   You can run the function by executing the `main.py` file in a Python environment. For example, you can use the Python interactive shell or include the function in your own Python script.

   ```python
   from main import choose_num

   result = choose_num(12, 15)
   print(result)  # Output: 14
   ```

4. **Modify and Test**

   Feel free to modify the function or test it with different inputs to suit your needs.

## Documentation

For further documentation or to report issues, please refer to the project's repository or contact the development team.

```