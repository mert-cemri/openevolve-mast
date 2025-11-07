# Sum Squares User Manual

Welcome to the Sum Squares application! This software provides a simple function to calculate the sum of squared numbers from a given list, where each element is first rounded up to the nearest integer (ceiling). This manual will guide you through the main functions of the software, how to install it, and how to use it effectively.

## Main Function

The core functionality of this software is encapsulated in the `sum_squares` function. This function takes a list of numbers as input and returns the sum of the squares of these numbers after rounding each number up to the nearest integer.

### Function Definition

```python
def sum_squares(lst):
    """
    You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    """
    import math
    return sum(math.ceil(x) ** 2 for x in lst)
```

### Example Usage

- For `lst = [1, 2, 3]`, the output will be `14`.
- For `lst = [1, 4, 9]`, the output will be `98`.
- For `lst = [1, 3, 5, 7]`, the output will be `84`.
- For `lst = [1.4, 4.2, 0]`, the output will be `29`.
- For `lst = [-2.4, 1, 1]`, the output will be `6`.

## Installation

This software does not require any external dependencies beyond Python itself. The necessary Python module `math` is part of the standard library.

### Prerequisites

- Python 3.x

### Installation Steps

1. **Clone the Repository**: Download or clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Script**: You can run the script directly using Python. No additional installation steps are required.

## How to Use

1. **Open a Python Environment**: You can use any Python environment like IDLE, PyCharm, or simply the command line.

2. **Import the Function**: If you are using the function in another script, make sure to import it.

   ```python
   from main import sum_squares
   ```

3. **Call the Function**: Pass a list of numbers to the `sum_squares` function and print or store the result.

   ```python
   result = sum_squares([1.4, 4.2, 0])
   print(result)  # Output will be 29
   ```

## Conclusion

The Sum Squares application is a straightforward tool designed to perform a specific mathematical operation efficiently. With no external dependencies, it is easy to set up and use. Should you have any questions or require further assistance, please feel free to reach out to our support team. Happy computing!