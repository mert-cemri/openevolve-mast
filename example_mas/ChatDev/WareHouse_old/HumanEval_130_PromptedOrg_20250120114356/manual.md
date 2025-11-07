# Tribonacci Sequence Calculator

This software module provides a function to calculate the first `n + 1` numbers of the Tribonacci sequence based on specific recurrence relations. The Tribonacci sequence is a variation of the well-known Fibonacci sequence, with its own unique rules for calculation.

## Main Functionality

The main function provided by this module is `tri(n)`, which calculates the first `n + 1` numbers of the Tribonacci sequence. The sequence is defined by the following rules:

- `tri(1) = 3`
- `tri(n) = 1 + n / 2`, if `n` is even.
- `tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1)`, if `n` is odd.

### Example

For example, calling `tri(3)` will return `[1, 3, 2, 8]`.

## Installation

This module does not require any external dependencies, so you can use it directly in your Python environment. Simply ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository:**

   If the code is hosted in a repository, clone it using:
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory:**

   Change into the directory containing the `main.py` file:
   ```bash
   cd <directory-name>
   ```

3. **Run the Code:**

   You can run the code directly using Python:
   ```bash
   python main.py
   ```

## How to Use

1. **Import the Function:**

   To use the `tri` function in your own scripts, import it from the module:
   ```python
   from main import tri
   ```

2. **Call the Function:**

   Pass a non-negative integer `n` to the function to get the first `n + 1` numbers of the Tribonacci sequence:
   ```python
   result = tri(3)
   print(result)  # Output: [1, 3, 2, 8]
   ```

## Documentation

For further details on how the function works, refer to the docstring provided within the `tri` function in `main.py`. This will give you insights into the logic and examples of how the sequence is calculated.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided within the code comments.