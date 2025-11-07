manual.md

```
# Largest Prime Factor Finder

This software provides a simple function to find the largest prime factor of a given integer. It is designed to handle numbers greater than 1 that are not prime themselves.

## Main Function

### `largest_prime_factor(n: int) -> int`

- **Description**: This function takes an integer `n` as input and returns the largest prime factor of `n`.
- **Assumptions**: 
  - The input `n` is greater than 1.
  - The input `n` is not a prime number.
- **Examples**:
  - `largest_prime_factor(13195)` returns `29`.
  - `largest_prime_factor(2048)` returns `2`.

## Installation

### Environment Setup

This software does not require any external dependencies, making it straightforward to set up and use. You only need Python installed on your system.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: If the code is hosted in a repository, clone it to your local machine using:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to where the `main.py` file is located:
   ```bash
   cd <directory-path>
   ```

## Usage

To use the `largest_prime_factor` function, follow these steps:

1. **Open a Python Environment**: You can use a Python IDE, or simply run Python in your terminal.

2. **Import the Function**: If you are using an interactive Python environment, import the function from `main.py`:
   ```python
   from main import largest_prime_factor
   ```

3. **Call the Function**: Pass the integer you want to analyze as an argument to the function:
   ```python
   result = largest_prime_factor(13195)
   print(result)  # Output will be 29
   ```

## Testing

You can test the function using the examples provided in the docstring. Simply call the function with different values of `n` to verify its correctness.

## Documentation

For further details on Python usage and best practices, refer to the official [Python documentation](https://docs.python.org/3/).

```