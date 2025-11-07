manual.md

```
# Prime Number Finder

This software provides a simple function to find all prime numbers less than a given non-negative integer. It is designed to be efficient and easy to use, with no external dependencies required.

## Quick Install

There are no external dependencies required for this software. You only need Python installed on your system to run the code.

## 🤔 What is this?

This software includes a function `count_up_to(n)` that takes a non-negative integer `n` and returns a list of all prime numbers less than `n`. Prime numbers are numbers greater than 1 that have no divisors other than 1 and themselves.

### Main Function

- **count_up_to(n):** This function returns a list of prime numbers less than the specified integer `n`.

### Example Usage

Here are some examples of how to use the `count_up_to` function:

```python
# Import the function from the main.py file
from main import count_up_to

# Example 1
result = count_up_to(5)
print(result)  # Output: [2, 3]

# Example 2
result = count_up_to(11)
print(result)  # Output: [2, 3, 5, 7]

# Example 3
result = count_up_to(0)
print(result)  # Output: []

# Example 4
result = count_up_to(20)
print(result)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]

# Example 5
result = count_up_to(1)
print(result)  # Output: []

# Example 6
result = count_up_to(18)
print(result)  # Output: [2, 3, 5, 7, 11, 13, 17]
```

## 📖 Documentation

The function `count_up_to(n)` is implemented in the `main.py` file. It uses an internal helper function `is_prime(num)` to determine if a number is prime. The function iterates through all numbers less than `n` and checks if they are prime, collecting them into a list which is then returned.

### How to Use

1. Ensure you have Python installed on your system.
2. Save the provided code into a file named `main.py`.
3. Use the function `count_up_to(n)` by importing it into your Python script or interactive session.
4. Call the function with your desired non-negative integer to get a list of prime numbers less than that integer.

This software is designed to be straightforward and efficient, making it easy to integrate into larger projects or use as a standalone tool for finding prime numbers.
```