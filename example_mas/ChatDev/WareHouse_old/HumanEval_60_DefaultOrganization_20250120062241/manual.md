# Sum to N Function

This software provides a simple Python function, `sum_to_n`, which calculates the sum of all integers from 1 to a given number `n`. This function is useful for mathematical computations where the sum of a series of consecutive numbers is required.

## Main Functionality

The main functionality of this software is encapsulated in the `sum_to_n` function. This function takes a single integer input `n` and returns the sum of all integers from 1 to `n` using the formula:

\[ \text{Sum} = \frac{n \times (n + 1)}{2} \]

### Example Usage

```python
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
```

## Installation

This software does not require any external dependencies beyond a standard Python environment. You can run the function in any Python 3.x environment.

### Quick Start

1. **Ensure Python is installed**: Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the `main.py` file containing the `sum_to_n` function.

3. **Run the Function**: You can use the function directly in a Python script or an interactive Python shell.

## How to Use

1. **Open a Python Environment**: You can use any Python IDE or the command line interface.

2. **Import the Function**: If you have saved the `main.py` file in your working directory, you can import the function using:

   ```python
   from main import sum_to_n
   ```

3. **Call the Function**: Use the function by passing an integer value to it:

   ```python
   result = sum_to_n(10)
   print(result)  # Output will be 55
   ```

This software is designed to be simple and efficient, utilizing a mathematical formula to compute the sum, which ensures optimal performance even for large values of `n`. Enjoy using the `sum_to_n` function for your computational needs!