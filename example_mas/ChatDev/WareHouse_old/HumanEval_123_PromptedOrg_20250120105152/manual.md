# Odd Collatz Sequence Finder

This software provides a function to compute the odd numbers in the Collatz sequence for a given positive integer. The Collatz conjecture is a famous mathematical sequence that eventually reaches 1, regardless of the starting integer.

## Main Functionality

The main function provided by this software is `get_odd_collatz(n)`. This function takes a positive integer `n` as input and returns a sorted list of the odd numbers that appear in the Collatz sequence starting from `n`.

### How the Collatz Sequence Works

1. Start with any positive integer `n`.
2. If `n` is even, the next term is `n / 2`.
3. If `n` is odd, the next term is `3 * n + 1`.
4. Repeat the process until the sequence reaches 1.

### Example

For example, calling `get_odd_collatz(5)` will return `[1, 5]` because the Collatz sequence for 5 is `[5, 16, 8, 4, 2, 1]`, and the odd numbers in this sequence are 5 and 1.

## Installation

This software does not require any external dependencies, so there is no need to install additional packages. You can directly use the provided Python code.

## Usage

To use the `get_odd_collatz` function, follow these steps:

1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file, for example, `main.py`.
3. Call the `get_odd_collatz` function with a positive integer as an argument.

### Example Code

```python
def get_odd_collatz(n):
    odd_numbers = set()  # Use a set to avoid duplicates and for automatic sorting
    while n != 1:
        if n % 2 == 1:  # Check if the number is odd
            odd_numbers.add(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    odd_numbers.add(1)  # Add 1 as it is always part of the sequence
    return sorted(odd_numbers)

# Example usage
print(get_odd_collatz(5))  # Output: [1, 5]
```

## Conclusion

This software provides a simple yet effective way to explore the odd numbers in the Collatz sequence for any positive integer. It is a useful tool for mathematical exploration and understanding the behavior of the Collatz conjecture.