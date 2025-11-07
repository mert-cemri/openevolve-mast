# Collatz Odd Numbers Extractor

This software provides a function to extract odd numbers from the Collatz sequence of a given positive integer. The Collatz conjecture is a mathematical sequence that starts with any positive integer and follows specific rules to eventually reach the number 1.

## Main Functionality

The main function provided by this software is `get_odd_collatz(n)`, which takes a positive integer `n` as input and returns a sorted list of odd numbers present in the Collatz sequence starting from `n`.

### Collatz Sequence

The Collatz sequence is defined as follows:
- Start with any positive integer `n`.
- If the current term is even, the next term is half of the current term.
- If the current term is odd, the next term is three times the current term plus one.
- The sequence continues until it reaches the number 1.

### Example

For example, calling `get_odd_collatz(5)` will return `[1, 5]` because the Collatz sequence for 5 is `[5, 16, 8, 4, 2, 1]`, and the odd numbers in this sequence are 5 and 1.

## Installation

No external dependencies are required to run this software. It is implemented in pure Python.

## How to Use

1. **Clone the Repository**: First, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Directory**: Change your directory to where the `main.py` file is located.

   ```bash
   cd <repository-directory>
   ```

3. **Run the Function**: You can use the function by importing it into your Python script or interactive session.

   ```python
   from main import get_odd_collatz

   result = get_odd_collatz(5)
   print(result)  # Output: [1, 5]
   ```

4. **Modify and Test**: Feel free to modify the code and test it with different values of `n` to see how the Collatz sequence behaves.

## Documentation

For further understanding of the Collatz conjecture and its implications, you can refer to mathematical resources or online documentation that explains the conjecture in detail.

This software is a simple implementation to demonstrate the extraction of odd numbers from the Collatz sequence and can be used for educational purposes or as a utility in larger projects.