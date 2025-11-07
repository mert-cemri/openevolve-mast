manual.md

```
# Fib4 Sequence Calculator

This software provides a function to compute the n-th element of the Fib4 number sequence, a sequence similar to the Fibonacci sequence but with a different set of rules.

## Main Functionality

The main functionality of this software is to compute the n-th element of the Fib4 sequence. The Fib4 sequence is defined as follows:
- fib4(0) -> 0
- fib4(1) -> 0
- fib4(2) -> 2
- fib4(3) -> 0
- fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4

The function `fib4(n: int) -> int` efficiently computes the n-th element of the sequence without using recursion.

## Quick Install

This software does not require any external dependencies, so no installation of additional packages is necessary. Simply ensure you have Python installed on your system.

## How to Use

1. **Clone or Download the Repository**: Start by cloning or downloading the repository containing the `main.py` file.

2. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Run the Script**: Execute the script using Python. You can do this by running the following command in your terminal:

   ```bash
   python main.py
   ```

   This will execute the example usage within the script and print the results for `fib4(5)`, `fib4(6)`, and `fib4(7)`.

4. **Use the Function**: To compute the Fib4 sequence for a different value of `n`, modify the calls to `fib4()` in the `if __name__ == "__main__":` block at the end of the `main.py` file.

## Example Usage

Here is an example of how to use the `fib4` function:

```python
# Example usage
if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
```

Modify the numbers in the `fib4()` function calls to compute the Fib4 sequence for other values of `n`.

## Documentation

For further details on the implementation, please refer to the comments within the `main.py` file. The code is well-documented to help you understand the logic and flow of the computation.

```