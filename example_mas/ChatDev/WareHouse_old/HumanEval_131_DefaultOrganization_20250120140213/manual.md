# Digits Product Calculator

This software provides a simple function to calculate the product of odd digits in a given positive integer. If all digits are even, the function will return 0.

## Main Functionality

The main function of this software is:

- **digits(n):** Given a positive integer `n`, this function returns the product of its odd digits. If all digits are even, it returns 0.

### Examples

- `digits(1)` returns `1`
- `digits(4)` returns `0`
- `digits(235)` returns `15`

## Installation

This software does not require any external dependencies, making it easy to set up and use. Simply ensure you have Python installed on your system.

### Quick Install

1. **Ensure Python is installed:** You can download and install Python from [python.org](https://www.python.org/).

2. **Clone or download the repository:** Obtain the `main.py` file containing the function.

3. **Run the function:** Use a Python interpreter to execute the function with your desired input.

## How to Use

1. **Open a terminal or command prompt.**

2. **Navigate to the directory containing `main.py`.**

3. **Run the Python interpreter:**

   ```bash
   python
   ```

4. **Import the function and use it:**

   ```python
   from main import digits
   result = digits(235)
   print(result)  # Output will be 15
   ```

5. **Exit the Python interpreter:**

   ```python
   exit()
   ```

## Documentation

The function is straightforward and does not require additional configuration or dependencies. For any further questions or support, please refer to the comments within the `main.py` file, which provide a brief overview of the function's logic and usage.