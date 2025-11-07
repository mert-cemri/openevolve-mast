# Odd Collatz Sequence Finder

This software provides a function to compute the odd numbers in the Collatz sequence for a given positive integer. The Collatz conjecture is a mathematical sequence that starts with any positive integer and follows specific rules to eventually reach the number 1.

## Main Function

The main function provided by this software is `get_odd_collatz(n)`, which takes a positive integer `n` as input and returns a sorted list of odd numbers that appear in the Collatz sequence starting from `n`.

### Function Details

- **Function Name:** `get_odd_collatz`
- **Input:** A positive integer `n`.
- **Output:** A sorted list of odd numbers in the Collatz sequence starting from `n`.

### Example

For example, calling `get_odd_collatz(5)` will return `[1, 5]` because the Collatz sequence for 5 is `[5, 16, 8, 4, 2, 1]`, and the odd numbers in this sequence are 5 and 1.

## Installation

This software is implemented in Python and does not require any external dependencies. You can use it directly in your Python environment.

### Quick Start

1. **Ensure Python is installed** on your system. You can download it from [python.org](https://www.python.org/).

2. **Clone or download the repository** containing the `main.py` file.

3. **Run the function** in a Python environment:

   ```python
   from main import get_odd_collatz

   result = get_odd_collatz(5)
   print(result)  # Output: [1, 5]
   ```

## Usage

To use the `get_odd_collatz` function, simply import it into your Python script or interactive session and call it with a positive integer as the argument. The function will return a list of odd numbers in the Collatz sequence for that integer.

### Example Usage

```python
# Import the function from the main module
from main import get_odd_collatz

# Get the odd numbers in the Collatz sequence for 10
odd_numbers = get_odd_collatz(10)
print(odd_numbers)  # Output: [1, 5]
```

## Conclusion

This software provides a simple yet effective way to explore the odd numbers in the Collatz sequence for any positive integer. It is easy to use and requires no additional setup beyond having Python installed. Enjoy exploring the fascinating world of Collatz sequences!