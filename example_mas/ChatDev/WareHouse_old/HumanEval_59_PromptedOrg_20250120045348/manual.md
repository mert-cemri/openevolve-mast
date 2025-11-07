# Largest Prime Factor Finder

This software module provides a function to find the largest prime factor of a given integer. It is designed to be simple and efficient, with no external dependencies required.

## Main Function

The main function provided by this module is `largest_prime_factor(n: int) -> int`. This function takes an integer `n` as input and returns the largest prime factor of `n`. It assumes that `n` is greater than 1 and is not a prime number.

### Example Usage

```python
from main import largest_prime_factor

# Example 1
result1 = largest_prime_factor(13195)
print(result1)  # Output: 29

# Example 2
result2 = largest_prime_factor(2048)
print(result2)  # Output: 2
```

## Installation

### Environment Setup

This module does not require any external dependencies, so setting up the environment is straightforward. You only need to have Python installed on your system.

1. **Install Python**: If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Directory**: Change your directory to the location where the `main.py` file is located.

   ```bash
   cd <directory-name>
   ```

## How to Use

1. **Import the Function**: Import the `largest_prime_factor` function from the `main.py` file.

   ```python
   from main import largest_prime_factor
   ```

2. **Call the Function**: Pass an integer greater than 1 (and not a prime) to the function to get its largest prime factor.

   ```python
   result = largest_prime_factor(13195)
   print(result)  # Output: 29
   ```

3. **Run the Script**: You can also run the script directly to test the function with different inputs.

   ```bash
   python main.py
   ```

## Conclusion

This module provides a simple and efficient way to find the largest prime factor of a given integer. With no external dependencies, it is easy to set up and use. Simply import the function and call it with your desired input to get the result.