# Prime Factorization Software

This software provides a function to factorize a given integer into its prime factors. The function returns a list of prime factors in ascending order, with each factor appearing as many times as it divides the number.

## Main Functionality

The main function provided by this software is `factorize(n: int) -> List[int]`. This function takes an integer `n` as input and returns a list of its prime factors.

### Example Usage

```python
from main import factorize

print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

## Installation

To use this software, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Setting Up the Environment

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change your current directory to the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies:**

   This project does not have any external dependencies, so you can directly proceed to use the software.

## How to Use

1. **Import the Function:**

   Import the `factorize` function from the `main.py` file in your Python script:

   ```python
   from main import factorize
   ```

2. **Call the Function:**

   Call the `factorize` function with an integer argument to get its prime factors:

   ```python
   factors = factorize(56)
   print(factors)  # Output: [2, 2, 2, 7]
   ```

3. **Run Tests:**

   You can test the function using the provided examples in the docstring:

   ```python
   import doctest
   doctest.testmod()
   ```

   This will run the examples provided in the docstring and verify that the function works as expected.

## Documentation

For further details and documentation, please refer to the docstring provided in the `main.py` file. The docstring includes example usage and expected outputs for the `factorize` function.

## Support

For any issues or questions, please contact our support team or open an issue in the repository. We are here to help you with any problems you may encounter while using the software.