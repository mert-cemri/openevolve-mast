manual.md

```
# Largest Prime Factor Finder

This software module provides a function to find the largest prime factor of a given integer. It is designed to be simple and efficient, with no external dependencies required.

## Main Functionality

The primary function provided by this module is:

- `largest_prime_factor(n: int)`: This function takes an integer `n` as input and returns the largest prime factor of `n`. It assumes that `n` is greater than 1 and is not a prime number itself.

### Example Usage

```python
from main import largest_prime_factor

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

## Installation

This software does not require any external dependencies, making it straightforward to set up and use. Simply ensure you have Python installed on your system.

### Step-by-Step Installation Guide

1. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where `main.py` is located.

3. **Run the Script**: You can directly run the script using Python. For example:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function**: Import the `largest_prime_factor` function from the `main.py` file into your Python script or interactive session.

2. **Call the Function**: Pass an integer greater than 1 (which is not a prime) to the function to get its largest prime factor.

3. **Example**: 
   ```python
   from main import largest_prime_factor

   result = largest_prime_factor(13195)
   print(f"The largest prime factor of 13195 is {result}")
   ```

## Additional Information

- **Assumptions**: The function assumes that the input number `n` is greater than 1 and is not a prime number itself.

- **Performance**: The algorithm efficiently finds the largest prime factor by iteratively dividing the number by its smallest factors.

- **No External Libraries**: This module is self-contained and does not require any additional Python packages or libraries.

Feel free to reach out for support or further inquiries about the software.
```