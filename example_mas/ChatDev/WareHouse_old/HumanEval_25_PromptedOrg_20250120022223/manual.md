# Factorize

This software provides a simple function to factorize a given integer into its prime factors. The function returns a list of prime factors in ascending order, with each factor appearing as many times as it divides the input number.

## Main Functionality

The main function provided by this software is:

- `factorize(n: int) -> List[int]`: This function takes an integer `n` as input and returns a list of its prime factors. The factors are listed in ascending order, and each factor appears as many times as it divides the number.

### Example Usage

```python
from main import factorize

# Factorize the number 8
print(factorize(8))  # Output: [2, 2, 2]

# Factorize the number 25
print(factorize(25))  # Output: [5, 5]

# Factorize the number 70
print(factorize(70))  # Output: [2, 5, 7]
```

## Installation

This software does not require any external dependencies. It is implemented in pure Python, and you can run it in any Python environment.

### Quick Install

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Clone the repository or download the `main.py` file to your local machine.

3. You can now use the `factorize` function by importing it from the `main.py` file.

## How to Use

1. Open your Python environment (e.g., Python shell, Jupyter notebook, or any Python IDE).

2. Import the `factorize` function from the `main.py` file.

3. Call the `factorize` function with an integer argument to get its prime factors.

4. The function will return a list of prime factors, which you can print or use in further calculations.

## Documentation

The function is documented with docstrings, providing examples of how to use it. You can view the documentation by calling `help(factorize)` in your Python environment.

This software is designed to be simple and efficient, making it easy to integrate into larger projects or use as a standalone tool for factorizing integers.