```markdown
# Largest Prime Factor Finder

This software module provides a function to find the largest prime factor of a given integer. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The main function provided by this module is `largest_prime_factor(n: int) -> int`. This function takes an integer `n` as input and returns the largest prime factor of `n`. It assumes that `n` is greater than 1 and is not a prime number itself.

### Example Usage

```python
from main import largest_prime_factor

# Example 1
result = largest_prime_factor(13195)
print(result)  # Output: 29

# Example 2
result = largest_prime_factor(2048)
print(result)  # Output: 2
```

## Installation

### Environment Setup

Since this module does not require any external dependencies, setting up the environment is straightforward. You only need Python installed on your system.

1. **Install Python**: If you haven't already, download and install Python from the official [Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

```bash
git clone <repository-url>
```

3. **Navigate to the Directory**: Change your working directory to the location of the `main.py` file.

```bash
cd <repository-directory>
```

## How to Use

1. **Import the Function**: In your Python script, import the `largest_prime_factor` function from the `main.py` file.

2. **Call the Function**: Pass the integer for which you want to find the largest prime factor as an argument to the function.

3. **Get the Result**: The function will return the largest prime factor of the given integer.

### Example

```python
from main import largest_prime_factor

number = 600851475143
largest_factor = largest_prime_factor(number)
print(f"The largest prime factor of {number} is {largest_factor}.")
```

## Additional Information

- **Assumptions**: The input integer `n` should be greater than 1 and not a prime number.
- **Efficiency**: The function efficiently reduces the number by dividing out factors, starting with the smallest prime number, 2, and then checking odd numbers up to the square root of the remaining number.

This module is a simple yet powerful tool for finding the largest prime factor of a number, suitable for educational purposes, mathematical computations, or integration into larger projects.
```