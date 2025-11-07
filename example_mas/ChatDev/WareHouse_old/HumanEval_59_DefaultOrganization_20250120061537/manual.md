manual.md

```
# Largest Prime Factor Finder

This software provides a simple and efficient way to find the largest prime factor of a given integer. It is designed to handle numbers greater than 1 that are not prime themselves.

## Main Functionality

The core functionality of this software is encapsulated in the `largest_prime_factor` function. This function takes an integer input `n` and returns the largest prime factor of `n`.

### Function Signature

```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
```

### Example Usage

```python
>>> largest_prime_factor(13195)
29
>>> largest_prime_factor(2048)
2
```

## Installation

To use this software, you need to have Python installed on your system. The software does not require any additional Python packages, so there is no need for a `requirements.txt` file.

### Step-by-Step Installation Guide

1. **Install Python**: Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone or download the repository containing the `main.py` file.

3. **Run the Code**: Navigate to the directory containing `main.py` and run the Python script using the command:

   ```bash
   python main.py
   ```

   You can also import the `largest_prime_factor` function into your own Python scripts and use it as needed.

## How to Use

1. **Import the Function**: If you want to use the function in your own script, import it as follows:

   ```python
   from main import largest_prime_factor
   ```

2. **Call the Function**: Pass an integer greater than 1 that is not a prime to the function to get its largest prime factor.

   ```python
   result = largest_prime_factor(600851475143)
   print(result)  # Output will be the largest prime factor
   ```

## Additional Information

- **Assumptions**: The function assumes that the input `n` is greater than 1 and is not a prime number.

- **Performance**: The function efficiently finds the largest prime factor by iteratively dividing the number by its smallest factors.

For any further questions or support, please contact our support team.
```