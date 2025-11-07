# Factorize

A simple Python module to factorize an integer into its prime factors.

## Introduction

This software provides a function to decompose a given integer into its prime factors. The function returns a list of prime factors in ascending order, with each factor appearing as many times as it divides the number.

## Main Function

### `factorize(n: int) -> List[int]`

- **Description**: This function takes an integer `n` and returns a list of its prime factors.
- **Parameters**: 
  - `n` (int): The integer to be factorized.
- **Returns**: 
  - `List[int]`: A list of prime factors of `n`, sorted in ascending order.

#### Example Usage

```python
>>> factorize(8)
[2, 2, 2]

>>> factorize(25)
[5, 5]

>>> factorize(70)
[2, 5, 7]
```

## Installation

This module does not require any external dependencies, so you can use it directly in your Python environment.

### Quick Install

1. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your current directory to where the `main.py` file is located.
   ```bash
   cd <directory-name>
   ```

3. **Run the Code**: You can directly run the `main.py` file or import the `factorize` function into your own scripts.

## How to Use

1. **Import the Function**: If you want to use the `factorize` function in your own Python script, you can import it as follows:
   ```python
   from main import factorize
   ```

2. **Call the Function**: Pass the integer you want to factorize to the `factorize` function.
   ```python
   factors = factorize(56)
   print(factors)  # Output: [2, 2, 2, 7]
   ```

## Documentation

For further details and examples, please refer to the docstring provided within the `main.py` file. The docstring includes usage examples and a brief description of the function's purpose and behavior.

This module is designed to be simple and straightforward, making it easy to integrate into larger projects or use as a standalone utility for prime factorization tasks.